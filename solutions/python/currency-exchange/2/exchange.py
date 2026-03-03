
def exchange_money(budget, exchange_rate):
    """calculate the exchanged money"""
    return budget / exchange_rate

def get_change(budget, exchanging_value):
    """claculate the remaining budget"""
    return budget - exchanging_value

def get_value_of_bills(denomination, number_of_bills):
    """calculate the complete value of the bills"""
    return denomination * number_of_bills

def get_number_of_bills(amount, denomination):
    """calculate the number of bills which can be paid with the amount of money"""
    return amount // denomination

def get_leftover_of_bills(amount, denomination):
    """

    :param amount: float - the total starting value.
    :param denomination: int - the value of a single bill.
    :return: float - the amount that is "leftover", given the current denomination.
    """
    return amount % denomination
    pass

def exchangeable_value(budget, exchange_rate, spread, denomination):
    """calculate the complete exchangebla value"""
    actual_rate = exchange_rate + exchange_rate * spread / 100
    total_value = budget / actual_rate
    number_of_bills = total_value // denomination
    return(number_of_bills * denomination)

# test the programm
print(exchange_money(100000, 0.8)) # expected 125000

print(get_leftover_of_bills(127.5, 20))  # expected 7.5

print(exchangeable_value(1000, 1.20, 10, 20))  # expected 740

print(exchangeable_value(1500, 0.84, 25, 10))  # expected 1420