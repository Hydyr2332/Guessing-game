# Importing
import random

# A function that checks if the user entered the correct number
def is_valid(n):
    return n.isdigit() and 1 <= int(n) <= 100

# Acquaintance
print('-------------------------------')
print('The computer guessed a number, from 1 to 100 try to guess!')
print('You now have 100 points in your account for every mistake you make, you lose 15 points for every win of 20 points')


# Variable that prompts to continue the game
play_again = ''
# Variable for game counting
game = 0
# Variable for attempts
attemts = 0
# List of successful attempts
attemts_lst = []

# Points
point = 100

# Variable and a list of all attempts made
record_attemts = 0
record_attemts_lst = []



# Main cycle
while play_again == '':

    # Variable for random digits
    pc_number = random.randrange(10, 99)

    # Flag to stop the inner loop
    flag = True





    # Internal cycle
    while flag:

        # Collect and display data (points, user record)
        print('-------------------------------')
        print(f'Earned points: {point}')
        print(f'Record: {attemts}')

        print('-------------------------------')

        if point >= 0:

            # The user guesses a random number
            user = input('Enter a number between 10 and 99: ')

            # The main conditions for checking the number
            if is_valid(user):
                user = int(user)
                # Variable for hints. Determines the difference between the number that is puzzled and the one entered by the user
                positive_modul = abs(user - pc_number)

                # Internal conditions for hints
                if user != pc_number:

                    if 70 <= positive_modul <= 89:
                        print('-------------------------------')
                        print("Ice Winds")
                        point -= 15
                        attemts += 1
                        record_attemts += 1

                    elif 50 <= positive_modul <= 69:
                        print('-------------------------------')
                        print("You are very far from the answer.")
                        point -= 15
                        attemts += 1
                        record_attemts += 1

                    elif 30 <= positive_modul <= 49:
                        print('-------------------------------')
                        print("Cold")
                        point -= 15
                        attemts += 1
                        record_attemts += 1

                    elif 15 <= positive_modul <= 29:
                        print('-------------------------------')
                        print("Try again.")
                        point -= 15
                        attemts += 1
                        record_attemts += 1

                    elif 5 <= positive_modul <= 14:
                        print('-------------------------------')
                        print("Cool, you're already very close.")
                        point -= 15
                        attemts += 1
                        record_attemts += 1

                    else:
                        print('-------------------------------')
                        print("Warmer!!!")
                        point -= 15
                        attemts += 1
                        record_attemts += 1


                else:
                    print("***********************")
                    print('PERFECT!!! GREAT!!! SALUT!!!')
                    print('Congratulations! Victory!')
                    point += 20
                    attemts += 1
                    record_attemts += 1
                    flag = False

            # If the user entered the wrong number or string it is a prompt to correct the error
            else:
                print('You will be deducted 10 points because you entered a line instead of a number or because you entered a number outside of the range.')
                point -= 10
                print(point)

        else:
            print('You ran out of glasses GAME OVER')
            flag = False


    game += 1
    attemts_lst.append(attemts)
    record_attemts_lst.append(record_attemts)
    record_attemts = 0

    if point <= 0:
        point = 100
    play_again = input('Press ENTER to play again or press any number to exit: ')





print("The game is over.")
print(f'You have played {game} games.')
print(f'For {game} games you {attemts} to guess the number once.')
print(f"Your personal record is {min(record_attemts_lst)}. It took you {min(record_attemts_lst)} tries to guess the number")
