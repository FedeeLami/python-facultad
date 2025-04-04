def imprimir_ranking(stadistics):
    jugadores = list(stadistics.keys())
    
    def obtener_puntos(jugador):
        return stadistics[jugador]['points']
    
    jugadores.sort(key=obtener_puntos, reverse=True)
    
    print(f"{'Jugador':<9} {'Kills':<7} {'Asistencias':<13} {'Muertes':<9} {'MVPs':<6} {'Puntos':<8}")
    print("-" * 60)
    
    for jugador in jugadores:
        stats = stadistics[jugador]
        print(f"{jugador:<9} {stats['kills']:<7} {stats['assists']:<13} {stats['deaths']:<9} {stats['mvp']:<6} {stats['points']:<8}")
    
    print("-" * 60)

def actualizar_estadisticas(rounds, stadistics):
    stad_mvps = {player: {'mvp': 0, 'points': 0} for player in stadistics}
    
    for i, round in enumerate(rounds, 1):
        max_score = 0
        max_player = ''
        
        for player, data in round.items():
            stadistics[player]['kills'] += data['kills']
            stadistics[player]['assists'] += data['assists']
            
            if data['deaths']:
                stadistics[player]['deaths'] += 1
            
            round_points = (data['kills'] * 3) + data['assists']
            if data['deaths']:
                stadistics[player]['points'] -= 1
            
            stadistics[player]['points'] += round_points
            stad_mvps[player]['points'] += round_points
            
            if round_points > max_score:
                max_score = round_points
                max_player = player
        
        stadistics[max_player]['mvp'] += 1
        stad_mvps[max_player]['mvp'] += 1
        
        print(f"Ronda {i}:")
        imprimir_ranking(stadistics)
        
        for player in stad_mvps:
            stad_mvps[player]['mvp'] = 0
            stad_mvps[player]['points'] = 0
