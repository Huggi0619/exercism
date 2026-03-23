def square(number):
    if 1 <= number <= 64:
        amount = 2 ** (number-1) # mit Feldnummer potenzieren
    
    else:
        raise ValueError("square must be between 1 and 64")
    return amount

def total():
    totalAmount = 0
    numberSquare = 1
    for i in range(64):
        totalAmount = totalAmount + 2 ** (numberSquare-1)
        numberSquare = numberSquare + 1
    return totalAmount

print(square(5))
print(total())

