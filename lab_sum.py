sum = 0
user_input = int(input("Enter a positive integer: "))
for i in range(1,user_input + 1):
    if i % 2 == 0:
        sum = sum + i
print("The sum of even numbers between 1 and ",user_input," is: ",sum)