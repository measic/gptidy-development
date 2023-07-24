# Practice with a try statement
while True:
    try:
        number = int(input('Please enter an integer: '))
        break
    except ValueError:
        print("That wasn't an integer, try again...")
        
print("Your number is", number)