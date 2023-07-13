print ("Welcome to the calculator! What do you want to calculate?")

#function to receive and check user input
def get_input():
    userinput = "invalid"
    while userinput == "invalid":
        userinput = input("")
        if userinput.isupper() == True or userinput.islower() == True:
            print ("That is an invalid input. Try again:")
            userinput = "invalid"
        for n in range(0,len(userinput)):
            if userinput[n] in "Xx*/+-" and userinput[n+1] in "Xx*/+-":
                print ("That is an invalid input. Try again:")
                userinput = "invalid"
    return userinput

userinput = get_input()

#defining dictionaries and placeholder variables (n and m)
numbers = {1:""}
n = 1
m = 1

#loop to turn intput into usable variables in dictionaries
for char in userinput:
    if char in "0123456789":
        numbers[n] += char
    if char in "Xx*/+-":
        n += 1
        numbers[n] = ""
        numbers[n] = char
        n += 1
        numbers [n] = ""

#first for loop to calculate multiplication and division first
for key in numbers:
    z = 1
    o = 1
    if numbers[key] == "X" or numbers[key] == "x" or numbers[key] == "*":
        while str(numbers[key - o]) in "Xx*/+- ":
            o += 1
        while str(numbers[key + z]) in "Xx*/+- ":
            z += 1
        numbers[key] = int(numbers[key - o]) * int(numbers[key + z])
        numbers[key - o] = ""
        numbers[key + z] = ""
    if numbers[key] == "/":
        while str(numbers[key - o]) in "Xx*/+- ":
            o += 1
        while str(numbers[key + z]) in "Xx*/+- ":
            z += 1
        numbers[key] = int(numbers[key - o]) / int(numbers[key + z])
        numbers[key - o] = ""
        numbers[key + z] = ""
#second for loop to calculate addition and subtraction
for key in numbers:
    z = 1
    o = 1
    if numbers[key] == "+":
        while str(numbers[key - o]) in "Xx*/+- ":
            o += 1
        while str(numbers[key + z]) in "Xx*/+- ":
            z += 1
        numbers[key] = int(numbers[key - o]) + int(numbers[key + z])
        numbers[key - o] = ""
        numbers[key + z] = ""
    if numbers[key] == "-":
        while str(numbers[key - o]) in "Xx*/+- ":
            o += 1
        while str(numbers[key + z]) in "Xx*/+- ":
            z += 1
        numbers[key] = int(numbers[key - o]) - int(numbers[key + z])
        numbers[key - o] = ""
        numbers[key + z] = ""

#for loop that iterates through the dictionary and prints out the only remaining number, which is the final answer
for key in numbers:
    if numbers[key] != "":
        print (str(userinput) + " = " + str(numbers[key]))


