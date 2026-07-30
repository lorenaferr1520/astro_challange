import json
import random
def line():
    print('=' * 45)

def load_questions():
    with open("questions.json", "r") as f:
        return json.load(f)

points = 0
life = 10

# -------- DEF SHOW QUESTIONS --------
def show_questions(level):
    dados = load_questions()
    line() #load question
    
    pergunta = random.choice(dados[level])
    
         
    print(pergunta["question"])
    line()
        
    for alternative in pergunta["options"]:
        print(alternative, '-', pergunta["options"][alternative] )

    while True:
        user_answer = input('Answer => ').upper()

        if user_answer not in "ABC":
            print('invalid response')
            continue
        else:
            break
            
    if user_answer == pergunta["answer"]:
        print('correct answer')
        return True
    else:
        print('incorrect answer')
        return False

# -------- MAIN GAME ---------
while True:
# -------- Easy Level --------
    for i in range(10):
        game = show_questions("easy")
        if game == True:
            points += 1
        else:
            life -= 1
            
        if life == 0:
            print('Game Over')
            break
#------------------------------- BREAKPOINT
    if life <= 0:
        break
#------------------------------- BREAKPOINT

# -------- Medium Level --------    
    for i in range(10):
        game = show_questions("medium")
        if game == True:
            points += 1
        else:
            life -= 1
            
        if life == 0:
            print('Game Over')
            break
#------------------------------- BREAKPOINT
    if life <= 0:
        break
#------------------------------- BREAKPOINT

# -------- Hard Level --------
    for i in range(10):
        game = show_questions("hard")
        if game == True:
            points += 1
        else:
            life -= 1
            
        if life == 0:
            print('Game Over')
            break
#------------------------------- BREAKPOINT
    if life <= 0:
        break
#------------------------------- BREAKPOINT

# -------- Legendary Level --------
    for i in range(5):
        game = show_questions("legendary")
        if game == True:
            points += 1
        else:
            life -= 1
            
        if life == 0:
            print('Game Over')
            break
#------------------------------- BREAKPOINT
    if life <= 0:
        break
#------------------------------- BREAKPOINT