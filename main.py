
import random
import json
import os

def load_vocab():
    with open("vocab.json","r",encoding="utf-8") as file:
        return json.load(file)
    

def load_high_score():
    if os.path.exists("high_score.json"):
        with open("high_score.json","r",encoding="utf-8") as file:
            data=json.load(file)
            return data["high_score"]
        
    return 0 #If it does not exist, return high score is 0
    

def save_high_score(score):
    # if  score is 4 , "high_score": 4
    data={
        "high_score": score
    }
    with open("high_score.json","w",encoding="utf-8") as file:
        json.dump(data,file,indent=2) # use 4 spaces to make file easy to read


def play_quiz(vocal_list):
    score = 0
    quiz_count = 5

    quiz_questions = random.sample(vocal_list,quiz_count)
    print("Japanese Vocabulary Quiz")
    print("==========================")

    for index,question in enumerate(quiz_questions, start=1):
     
        print(f"\nQuestion {index}: {question['japanese']}")

        user_answer=input("Your answer: ").lower().strip()
        correct_answer= question["english"].lower().strip()

        if user_answer == correct_answer:
            print("Correct!")
            score = score + 1

        else:
            print("Wrong.")
            print("Correct answer is:", question["english"])

        print("\nQuiz finished!")
        print(f"YOur score:{score}/{quiz_count}")
    return score 

vocal_list= load_vocab()

while True:
    high_score = load_high_score()

    print(f"\nCurrent high score: {high_score}")

    current_score = play_quiz(vocal_list)

    if current_score > high_score:
        print("New high score!")
        save_high_score(current_score)
    else:
        print(f"High score remains: {high_score}")


    play_again = input("\nD you want to play again? (yes/no): ").lower().strip()

    if play_again != "yes":
        print("Thank you for playing")
        break

