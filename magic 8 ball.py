# ph_levels = 14
# ph = int(input("Enter the pH level (0-14): "))

# if ph > 7 :
#     print("The solution is basic")
# elif ph < 7 :
#     print(" The solution is acidic") 
# else:
#     print("The solution is neutral")      
  
#   magic 8 balls
import random
print("**********Welcome to the magic 8 ball game**********")
print("Ask philosical type question and I will give you the answer!")
questions = input("QUESTION: ")

answers = random.randint(1,9)
 
if answers == 1:
    answer = "yes - definitely"
elif answers == 2:
    answer = "It is decidedly so."    
elif answers == 3:
    answer = "without a doubt"
elif answers == 4:
    answer = "Reply hazy, try again"
elif answers == 5:
    answer = "Ask again later."
elif answers == 6:
    answer = "Better not tell you now."
elif answers == 7:
    answer = "My sources say no."
elif answers == 8:
    answer = "Outlook not so good."
elif answers == 9:
    answer = "Very doubtful."
else:
    answer = "answer is not defined."

print("magic 8 ball:", answer)

       