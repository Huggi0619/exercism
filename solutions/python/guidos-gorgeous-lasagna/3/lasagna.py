
EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


def bake_time_remaining(actual_time):
    '''calculate the remaining bake time'''
    return EXPECTED_BAKE_TIME - actual_time

def preparation_time_in_minutes(number_of_layers):
    '''calculate the preparation time in minutes'''
    return number_of_layers * PREPARATION_TIME

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    '''calculates the time spent in the kitchen'''
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time

# Test the code
print(bake_time_remaining(30)) # should print 10
print(preparation_time_in_minutes(2)) # should print 4
print(elapsed_time_in_minutes(3, 20)) # should print 26