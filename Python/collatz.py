def collatz(x):
    if (x % 2 == 0):
        x = (x / 2)
        return x
    else:
        x = (x * 3 + 1)
        return x

try:
    number = int(input('Enter number:'))
except ValueError:
    number = int(input('Please enter a number:'))
    
while number > 1:
        number = int(collatz(number))
        print(number)
