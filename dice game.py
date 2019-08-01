import random

def roll():
    global dice1
    global dice2

    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)

def balance():
    global current_points
    print(current_points)

def win():
    global current_points
    current_points = current_points + 40
    print(current_points )


def loses():
    global current_points
    current_points  = current_points  - 10
    print(current_points)


name_of_player = input('Hello good sir, Please give me your name')
print('Ready to lose some points ' + name_of_player + '?')
starting_points = int(input('How many points do you want to bet today? '))
current_points = starting_points

print(current_points)
print('rules of the game: Betting on the number of dice 1, 2 or sum of the 2 dice')
print('bet cost 10')
print('If you get the answer correct you get 5 times our bet')

while current_points > 9:
    roll()
    print(dice1,dice2)
    betting_option = input('betting on dice one, two or sum. Please only type one two of sum in')
    betting_guss = int(input('what is do you think the number is'))
    if betting_option == 'one' :
        print('lets hope this work')
        if betting_guss == dice1:
            win()
        else :
            loses()
    elif betting_option == 'two' :
        if betting_guss == dice2 :
            win()
        else :
            loses()
    else:
        if betting_guss == dice1 + dice2 :
            win()
        else :
            loses()

    next = input('Do you want to contue playing? (yes or no)')
    if next == 'no' or next == 'No':
        break
    else:
        print('have fun')

if current_points > starting_points:
    print('Well done you have made money')
else:
    print('better luck next time')