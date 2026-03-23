def square(number):
    if 1 <= number <= 64:
        AMOUNT = 2 ** (number-1) # mit Feldnummer potenzieren
    
    else:
        raise ValueError("square must be between 1 and 64")
    return AMOUNT

def total():
    TOTAL_AMOUNT = 0
    for i in range(64):
        TOTAL_AMOUNT = TOTAL_AMOUNT + 2 ** i
    return TOTAL_AMOUNT

print(square(5))
print(total())