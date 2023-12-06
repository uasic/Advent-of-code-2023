input = open("input2.1.txt")
#print(input.read())

# PART 1:

blue_limit = 14
red_limit = 12
green_limit = 13

import re
possible_games = []

for line in input.readlines():

    possibility_blue = True
    possibility_green = True
    possibility_red = True

    game_id = re.compile(r'(\d+):')
    game_id = game_id.findall(line)
    
    for id in game_id:
        game_id = int(id)
        #print(game_id)

    #BLUE
    blue = re.compile(r'(\d+) blue')
    number_blue = blue.findall(line)
    #print("Number of blue: ", number_blue)
    for number in number_blue:
        number = int(number)
        #print(number)
        if number > blue_limit:
            possibility_blue = False
            #print("Too much blue cubes.")

    #GREEN
    green = re.compile(r'(\d+) green')
    number_green = green.findall(line)
    #print("Number of green: ", number_green)
    for number in number_green:
        number = int(number)
        #print(number)
        if number > green_limit:
            possibility_green = False
            #print("Too much green cubes.")

    #RED
    red = re.compile(r'(\d+) red')
    number_red = red.findall(line)
    #print("Number of red: ", number_red)
    for number in number_red:
        number = int(number)
        #print(number)
        if number > red_limit:
            possibility_red = False
            #print("Too much red cubes.")

    if possibility_red == True and possibility_blue == True and possibility_green == True: 
        possible_games.append(game_id)

#print("Possible games are: ", possible_games)

sum_games_ID = 0

for value in possible_games:
    sum_games_ID = sum_games_ID + value

#print("Part 1:\nSum: ", sum_games_ID)


# PART 2:

input = open("input2.1.txt")
all_powers_sum = 0

for line in input.readlines():
    
    #print(line)

    game_id = re.compile(r'(\d+):')
    game_id = game_id.findall(line)
    for id in game_id:
        game_id = int(id)
        #print("Game ID: ", game_id)

    #BLUE
    blue = re.compile(r'(\d+) blue')
    number_blue = blue.findall(line)
    #print("Number of blue: ", number_blue)
    number_blue_int = []
    for number in number_blue:
        number = int(number)
        number_blue_int.append(number)
        #print(number)
    #print("Number of blue: ", number_blue_int)
    min_blue = max(number_blue_int)
    #print(min_blue)

    #GREEN
    green = re.compile(r'(\d+) green')
    number_green = green.findall(line)
    #print("Number of green: ", number_green)
    number_green_int = []
    for number in number_green:
        number = int(number)
        number_green_int.append(number)
        #print(number)
    #print("Number of green: ", number_green_int)
    min_green = max(number_green_int)
    #print(min_green)

    #RED
    red = re.compile(r'(\d+) red')
    number_red = red.findall(line)
    #print("Number of red: ", number_red)
    number_red_int = []
    for number in number_red:
        number = int(number)
        number_red_int.append(number)
        #print(number)
    #print("Number of red: ", number_red_int)
    min_red = max(number_red_int)
    #print(min_red)

    power = min_red * min_blue * min_green
    #print("Power of a line = ", power)
    all_powers_sum = all_powers_sum + power

print("Sum of all powers = ", all_powers_sum)