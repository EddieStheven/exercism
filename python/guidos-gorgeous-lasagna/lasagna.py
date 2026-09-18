EXPECTED_BAKE_TIME = 40

def bake_time_remaining(bake_time):

    """
        Tempo restante pra lasanha ficar pronta
    """

    return EXPECTED_BAKE_TIME - bake_time
       
bake_time_remaining(30)

def preparation_time_in_minutes(number_of_layers):

    """
        Preparação da lasanha por camada, 2 minutos por camada
    """

    return number_of_layers * 2

preparation_time_in_minutes(4)

def elapsed_time_in_minutes(number_of_layers,elapsed_bake_time):

    """Calculate the elapsed cooking time.
    
    Parameters:
        number_of_layers (int): The number of layers in the lasagna.
        elapsed_bake_time (int): Time the lasagna has been baking in the oven.
    
    Returns:
        int: The total time elapsed (in minutes) preparing and baking.

    This function takes two integers representing the number of lasagna 
    layers and the time already spent baking the lasagna. It calculates 
    the total elapsed minutes spent cooking (preparing + baking).
    
    """

    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time

elapsed_time_in_minutes(3,20)