#1) Using range()
for num in range(45,210):
    if num == 100:
        continue
    elif num == 205:
        break
    else:
        print(num)

#Using a while loop
user_answer = int(input("what is the product of 7 * 24? "))
while True:
 if user_answer == 168:
    break
 elif user_answer != 168:
    print("Your Answer is wrong try again..")
 user_answer = int(input("what is the product of 7 * 24? "))
 
print("You answered this Question correctly")
 

