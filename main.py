import random


def rockPaperScissors():
    options = (1,2,3)
    game = True
    while game:
        round = int(input('Insert the number of rounds '))
        points = [0,0]
        while round > 0:
            computer = random.choice(options)
            user = int(input('Enter 1 for scissors, 2 for rock and 3 for paper '))
            if not user in options:
                print('that option is unvalid')
                continue
            elif computer - user == 0:
                pass
            elif computer > user and (computer - user != 2):
                points[1] += 1
            elif computer < user and computer - user == -2:
                points[1] += 1
            else:
                points[0] += 1
            round -= 1
        else:
            print('Game ended')
            if points[0] > points[1]:
                print('user win')
                game = False
            elif points[0] == points[1]:
                print(' TIE, rematch will start shortly')
                round = 3
                continue
            else:
                print('user loss : (')
                game = False

rockPaperScissors()
