print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")
correct = 0
incorrect = 0

if playing.lower() != "yes":
    quit()
else:
    print("Okay! Let's play! :)")

answer = input("What does CPU stand for? ")
if answer.lower() == "centeral processing unit":
    print("Correct!")
    correct = correct + 1
else:
    print("Incorrect")
    incorrect = incorrect + 1

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    correct = correct + 1
else:
    print("Incorrect")
    incorrect = incorrect + 1

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    correct = correct + 1
else:
    print("Incorrect")
    incorrect = incorrect + 1

answer = input("What does PSU stand for? ")
if answer.lower() == "power supply":
    print("Correct!")
    correct = correct + 1
else:
    print("Incorrect")
    incorrect = incorrect + 1

print("You got " + str(correct) + " questions correct and " +
      str(incorrect) + " questions incorrect")
print("Your final score is " + str((correct/4)*100) + "%")
