print ("Welcome to the calculator! What do you want to calculate?")
input = input("")
input_2 = input.replace(" ","")

#defining dictionaries and placeholder variables (n and m)

numbers = {1:"", 2:"", 3:""}
n = 1
m = 1
operat = {1:"", 2:"", 3:""}
ans2 = 0
answer = {1:"", 2:"", 3:""}
final = 0

#loop to turn intput into usable variables in dictionaries

for char in input_2:
    if char in "0123456789":
        numbers[n] += char
    if char in "Xx*/+-":
        n += 1
        operat[m] = char
        m += 1

# this code below is the plan for coding order of operations.
# making progress, still need to figure out how to not add previous numbers together. IE 10+10+10 is outputting 40 because it is doing 10+10 twice, rather than doing 20+10
# not sure how to solve this, perhaps deleting numbers from dictionary once they are used in calculation?


for key in operat:
    if operat[key] == "X" or operat[key] == "x":
        if key == 1:
            answer[key] = int(numbers[key]) * int(numbers[key + 1])
        else:
            answer[key] = int(numbers[key - 1]) * int(numbers[key + 1])
    if operat[key] == "/":
        if key == 1:
            answer[key] = int(numbers[key]) / int(numbers[key + 1])
        else:
            answer[key] = int(numbers[key - 1]) / int(numbers[key + 1])
    if operat[key] == "+":
        if key == 1:
            answer[key] = int(numbers[key]) + int(numbers[key + 1])
        else:
            answer[key] = int(numbers[key - 1]) + int(numbers[key + 1])
    if operat[key] == "-":
        if key == 1:
            answer[key] = int(numbers[key]) - int(numbers[key + 1])
        else:
            answer[key] = int(numbers[key - 1]) - int(numbers[key + 1])



for key in answer:
    if  answer[key] != "":
        final += int(answer[key])

print (int(final))

#this below code works, but order of operations does not exist
#for example, 10+10x20 will output 400 when it should output 210

#if operat[1] == "X" or operat[1] == "x" or operat[1] == "*":
    #ans1 = int(numbers[1]) * int(numbers[2])
#if operat[1] == "/":
    #ans1 = int(numbers[1]) / int(numbers[2])
#if operat[1] == "+":
    #ans1 = int(numbers[1]) + int(numbers[2])
#if operat[1] == "-":
    #ans1 = int(numbers[1]) - int(numbers[2])
#if operat[2] == "X" or operat[2] == "x" or operat[2] == "*":
    #ans2 = ans1 * int(numbers[3])
#if operat[2] == "/":
    #ans2 = ans1 / int(numbers[3])
#if operat[2] == "+":
    #ans2 = ans1 + int(numbers[3])
#if operat[2] == "-":
    #ans2 = ans1 = int(numbers[3])

#if ans2 != 0:
    #print (input + " = " + str(ans2))
    #print()
#else:
    #print (input + " = " + str(ans1))
    #print()


