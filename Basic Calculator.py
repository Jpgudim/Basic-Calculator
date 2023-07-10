print ("Welcome to the calculator! What do you want to calculate?")
input = input("")
input_2 = input.replace(" ","")

#defining dictionaries and placeholder variables (n and m)

numbers = {1:""}
n = 1
m = 1


operat = {}
ans2 = 0
answer = {}
final = 0

#loop to turn intput into usable variables in dictionaries

for char in input_2:
    if char in "0123456789":
        numbers[n] += char
    if char in "Xx*/+-":
        n += 1
        numbers[n] = ""
        operat[m] = ""
        operat[m] = char
        m += 1

for key in operat:
    if operat[key] == "X" or operat[key] == "x":
        if key == 1:
            answer[key] = int(numbers[key]) * int(numbers[key + 1])
            numbers[key] = answer[key]
        else:
            answer[key] = int(numbers[key - 1]) * int(numbers[key + 1])
            numbers[key] = answer[key]
    if operat[key] == "/":
        if key == 1:
            answer[key] = int(numbers[key]) / int(numbers[key + 1])
            numbers[key] = answer[key]
        else:
            answer[key] = int(numbers[key - 1]) / int(numbers[key + 1])
            numbers[key] = answer[key]
    if operat[key] == "+":
        if key == 1:
            answer[key] = int(numbers[key]) + int(numbers[key + 1])
            numbers[key] = answer[key]
        else:
            answer[key] = int(numbers[key - 1]) + int(numbers[key + 1])
            numbers[key] = answer[key]
    if operat[key] == "-":
        if key == 1:
            answer[key] = int(numbers[key]) - int(numbers[key + 1])
            numbers[key] = answer[key]
        else:
            answer[key] = int(numbers[key - 1]) - int(numbers[key + 1])
            numbers[key] = answer[key]

final_answer = answer.copy()

for key in answer:
    if  answer[key] == "":
        del final_answer[key]
print (final_answer[list(final_answer.keys())[-1]])


