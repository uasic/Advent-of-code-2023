'''input = open("input4.txt")

# PART 1

import re

total_points = 0

for line in input.readlines():

    print("Line: ", line)
    line.split(":")
    card_id = re.compile(r'(\d+):')
    card_id = card_id.findall(line)
    for card_id in card_id:
        card_id = int(card_id)
        print("Card ID: ", card_id)
    # card_id označuje številko kartice

    line_modif = line.split(":")
    #print(line_modif)
    del line_modif[0]
    #print(line_modif)
    line_modif = line_modif[0]
    line_modif = line_modif.split("|")
    winning_numbers = line_modif[0].strip()
    my_numbers = line_modif[1].strip()

    #print("winning numbers: ", winning_numbers , " and " , "my numbers: ", my_numbers)
    #print(type(winning_numbers))

    #print(winning_numbers)

    winning_numbers_list = [int(num) for num in winning_numbers.split()]
    print("List of winning numbers: ", winning_numbers_list)
    my_numbers_list = [int(num) for num in my_numbers.split()]
    print("List of my numbers: ", my_numbers_list)


    winning = set(winning_numbers_list)
    my = set(my_numbers_list)
    common_numbers = winning.intersection(my)
    print("My winning numbers: ", common_numbers)
    #print(type(common_numbers))

    number_of_winning_numbers = len(common_numbers)
    print("Number of winning numbers: ", number_of_winning_numbers)

    if number_of_winning_numbers == 0:
        card_worth = 0

    else: card_worth = (2**number_of_winning_numbers)/2

    print("Card worth: ", card_worth)
    total_points = total_points + card_worth

print("My total points: ", total_points)'''



# PART 2

input = open("test.txt")
import re

all_results = []
for line in input.readlines():
    line.split(":")
    card_id = re.compile(r'(\d+):')
    card_id = card_id.findall(line)
    for card_id in card_id:
        card_id = int(card_id)
    line_modif = line.split(":")
    del line_modif[0]
    line_modif = line_modif[0]
    line_modif = line_modif.split("|")
    winning_numbers = line_modif[0].strip()
    my_numbers = line_modif[1].strip()
    winning_numbers_list = [int(num) for num in winning_numbers.split()]
    my_numbers_list = [int(num) for num in my_numbers.split()]
    winning = set(winning_numbers_list)
    my = set(my_numbers_list)
    common_numbers = winning.intersection(my)
    number_of_winning_numbers = len(common_numbers)
    if number_of_winning_numbers == 0:
        card_worth = 0
    else: card_worth = (2**number_of_winning_numbers)/2
    result = []
    #result.append(card_id)
    result.append(number_of_winning_numbers)
    result.append(int(card_worth))

    all_results.append(result)

print("All results: ", all_results)
#print(len(all_results))

outcome_id = 0

while outcome_id <= len(all_results):
    stevec = all_results[outcome_id][0] # stevilo ujemajocih se vrednosti
    # [[4, 8], [2, 2], [2, 2], [1, 1], [0, 0], [0, 0]]
    print("Stevec: ", stevec)
    outcome_id +=1

    while stevec > 0:
        element_to_add = stevec
        all_results.append(all_results[element_to_add].copy())
        stevec = stevec - 1
        #print(stevec)
    

print("Final list: ", all_results)