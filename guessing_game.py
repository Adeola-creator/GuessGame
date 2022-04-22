import random
val = random.randint(1, 100)
for i in range(10):
 guess = input("Guess a number between 1 and 100 :  ")
 if int(guess) < val:
 	   	print("Too low")
 elif int(guess) > val:
 	       print("Too high")
 elif int(guess) == val:
 	   	print("Correct!!")
 	   	break
else:
 print("You ran out of guesses, the correct answer is " + str (val) )