
def square(number):
    if 1 <= number <= 64:
        amount = 2 ** (number-1) # mit Feldnummer potenzieren
    
    else:
        raise ValueError("square must be between 1 and 64")
    return amount

def total():
    total_amount = 0
    for field in range(0, 64):
        total_amount = total_amount + 2 ** field
    return total_amount

print(square(5))
print(total())