# flashcards.py

# import the json module from python3
import json

# open the file and parse the JSON
with open('me-capitals.json', 'r') as f:
    data = json.load(f)

# initialize total as the length of the cards array
total = len(data["cards"])
# initialize score as 0
score = 0
wrong_answers = 0
player = False

while player == False: #Created While Loop to be able to ask player if they want to play again (Brainstorm New feature suggestion)
    
    score = 0
    wrong_answers = 0
    count = 0
    

    for i in data["cards"]:
           
        guess = input(i["q"] + " > ")
        
        if guess.lower() == i["a"].lower():
            # increment score up one
            score += 1
            # interpolate score and total into the response
            print(f"Correct! Current score: {score}/{total}")

        elif guess.lower() != i["a"].lower():
            print("Incorrect! The correct answer was", i["a"])
            print(f"Current score: {score}/{total}")
            wrong_answers += 1
        
        count = wrong_answers + score

    #Stretch Challenge - End Game Message
    #The game will print a message "Thank you for playing" at the end of the game
    #Additionally, it will generate a message based on the score:

        if count == total:
            print(f"Thanks for playing! You scored: {score} out of five correct!")
            if (score < (total/2)):
                print(f"Improvement needed. . . you only got {(score*100)/total}% right")
                play_again = input("Do you want to play again? (yes/no)")

            elif(score > (total/2) and score < total):
                print(f"Good job ! you got {(score*100)/total}% right!")
                play_again = input("Do you want to play again? (yes/no)")

            elif(score == total):
                print(f"Amazing ! you got {(score*100)/total}% right!")
                play_again = input("Do you want to play again? (yes/no)")
            #Brainstorm New Features 
            if play_again == "yes": 
                player = False  
            elif play_again == "no":
                print("thank you for playing.")
                player = True

    