### Exercise 1:
#Print -20 to and including 50. Use any loop you want.

#for i in range(-20, 50 + 1):
#  print(i)


### Exercise 2:
#Create a loop that prints even numbers from 0 to and including 20.Hint: You can find multiples of 2 with (whatever_number % 2 == 0)

#for i in range(0, 20 + 1 , 2):
 #   print(i)

## Exercise 3:
#Prompt the user for 3 numbers. Then print the 3 numbers along with their average after the 3rd number is entered. Refer to example below replacing ```NUMBER1```, ```NUMBER2```, ```NUMBER3```, and ```THEAVERAGE``` with the actual values.

#Ex.Output

#userInput = input("enter number ")
#userInput2 = input("enter number ")
#userInput3 = input("enter number ")
#sum = int(userInput) + int(userInput2) + int(userInput3)

#print(str(userInput) + " + " + str(userInput2) + " + " + str(userInput3) + " = " + str(sum))


## Challenge:
#Password Checker - Ask the user to enter a password. Ask them to confirm the password. If it's not equal, keep asking until it's correct or they enter 'Q' to quit.



userInput = input("enter a password")
userInput2 = input("confirm password")

while userInput != userInput2:
    userInput2 = input("confirm password")



