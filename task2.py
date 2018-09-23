x = '*'

#Generating unrepeated random numbers between 0 and 9
import random

computer_random_numbers = random.sample(range(0,10),3)

print(computer_random_numbers)

while (x == '*'):

    user_random_numbers = []
    check = 0
    count = 0

    #a loop that Prompts the user to enter 3 numbers
    for i in range (3):
        x = int(input("Enter a number: "))
        user_random_numbers.append(x)

    print(user_random_numbers)

    #nested for loops to compare computer's numbers with user's numbers
    for i in range (3):
        if user_random_numbers[i] == computer_random_numbers[i]:
            count = count + 1
        for n in range (3):
            if user_random_numbers[i] == computer_random_numbers[n]:
                    check = check + 1

    #if all the numbers match
    if count == 3:
        print("Congrats!")
        computer_random_numbers = random.sample(range(0,10),3)
        #print(computer_random_numbers)

    #if one or two numbers match
    elif count == 1 or count == 2:
        print("Match")

    #if one or more numbers match but in an incorrect order
    elif check == 1 or check == 2:
        print("Close")

    #if no numbers match
    elif count == 0 and check == 0:
        print("Nope!")

    x = input('Press * to try again or Press any key to exit: ')
