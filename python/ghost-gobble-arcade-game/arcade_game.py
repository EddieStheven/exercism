def eat_ghost(power_pellet_active,touching_ghost):
    """
        O pacman tem poder E está tocando o fantasma
    """
    return power_pellet_active and touching_ghost

print(eat_ghost(False,True))

def score(touching_power_pellet, touching_dot):
    """
        O pacman está tocando o poder OU está tocando o ponto
    """
    return touching_power_pellet or touching_dot

print(score(True,True))

def lose(power_pallet_activate, touching_ghost):
    """
        O pacman está com poder ativiado e não está tocando o fantasma
    """
    return touching_ghost and not power_pallet_activate

print(lose(False,True))

def win (has_eaten_all_dots, power_pellet_active, touching_ghost):
    """
        O pacman comeu todos os pontos E NÃO ( está com poder ativado E tocou no fantasma )
    """
    return has_eaten_all_dots and not lose( power_pellet_active, touching_ghost)

print(win(False,True,False))

