print ("Welcome to the calculator! What do you want to calculate?")
input = input("")
input_2 = input.replace(" ","")

num1 = ""
num2 = ""
  
for char in input_2:
    if char in "0123456789":
        num1 += char
    else:
        break

length = len(num1) + 1
num2 = input_2[int(length):]

num1 = int(num1)
num2 = int(num2)

print()
if "X" in input_2 or "x" in input_2 or "*" in input_2:
    answer = num1 * num2
    print (input + " = " + str(answer))
elif "/" in input_2:
    answer = num1 / num2
    print (input + " = " + str(answer))
elif "+" in input_2: 
    answer = num1 + num2
    print (input + " = " + str(answer))
elif "-" in input_2:
    answer = num1 - num2
    print (input + " = " + str(answer))
print ()



