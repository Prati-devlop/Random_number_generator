import random
number = random.randint(1, 20)
print('Hello! What is your name?')
Name = input()
guessTaken=0
print('Well, ' + Name + ', I am thinking of a number between 1 and 20.')
while guessTaken < 6:
    print('Take a guess of a number')
    guess =input()
    if guess=="0":  
        print(guess, "is not a valid guess")
    elif guess.isdigit() == False: 
        print(guess, "is not a valid guess")
    elif int(guess) >20:
        print(guess, "is not a valid guess")
    else : 
        guessTaken = guessTaken + 1
        if int(guess) < number:
            print('Your guess is too low.')
        if int(guess) > number:
            print('Your guess is too high.')
        if int(guess) == number:
            break
if int(guess) == number:
    guessTaken = str(guessTaken)
    print('Well done, ' + Name + '! You guessed my number in ' + guessTaken + ' guesses!')
elif int(guess) != number:
                number = str(number)
                print('Nope,bad luck. The number I was thinking of was ' + number)
