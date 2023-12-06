input = open("input1.1.txt")
#print(input.read())

substrings = {
    "nine":"9e",
    "eight":"8t",
    "seven":"7n",
    "six":"6x",
    "five":"5e",
    "four":"4r", 
    "three":"3e", 
    "two":"2o",
    "one":"1e",
    "zero":"0o", 
    }


lines = []
for line in input:
    for key in sorted(substrings, key=lambda x: line.find(x)):
        if key in line:
            line = line.replace(key, substrings[key])
            #print(line.strip())
    lines.append(line.strip())
print(lines)
#print(len(lines))

# all numbers written in letters are converted

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
#print(type(numbers))

all_line_lists = []

for line in lines:
    #print(line)
    line_list = []
    for c in line:
        #print(c)
        if c in numbers:
            line_list.append(c)
            #print(line_list)
    #print(line_list)
    all_line_lists.append(line_list)
#print(all_line_lists)

all_calibration_values = []
for sublist in all_line_lists:
    calibration_value =sublist[0] + sublist[-1]
    all_calibration_values.append(calibration_value)
#print(all_calibration_values)

numbers_to_sum = []
for element in all_calibration_values:
    element = int(element)
    numbers_to_sum.append(element)
print(numbers_to_sum)
print("Number of all calibration values: ", len(numbers_to_sum))

sum = 0
for number in numbers_to_sum:
    sum = sum + number
    #print(sum)
print("Sum of all calibration values: ", sum)