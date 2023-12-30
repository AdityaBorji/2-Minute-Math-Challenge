import random
import time

def level1(start_time):
    score=0
    OPERATORS=["+", "-", "*", "/"]
    for i in range(1,11):
        current_time = time.time()
        if (current_time-start_time>=120):
            print("Times up!")
            return_score(score, "")
        print(f"\n********LEVEL {i}*********\n")
        a=random.randint(1, 10)
        b=random.randint(1, 10)
        operator=random.choice(OPERATORS)
        problem=str(a)+" "+ operator + " " + str(b)
        ans=input(f"{problem} = ")
        if ans!=str(int(round(eval(problem), 0))):
            return_score(score, "")
        score+=1
    print(f"\nCURRENT SCORE= {score}")
    return level2(score, start_time)


def level2(score, start_time):

    OPERATORS=["+", "-", "*", "/"]
    for i in range(score+1,21):
        current_time = time.time()
        if (current_time-start_time>=120):
            print("Times up!")
            return_score(score, "")
        print(f"\n********LEVEL {i}*********\n")
        a=random.randint(10, 100)
        b=random.randint(10, 100)
        operator=random.choice(OPERATORS)
        problem=str(a)+" "+ operator + " " + str(b)
        ans=input(f"{problem} = ")
        if ans!=str(int(round(eval(problem), 0))):
            return_score(score, "")
        score+=1
    print(f"\nCURRENT SCORE= {score}")
    return level3(score, start_time)


def level3(score, start_time):
    OPERATORS=["+", "-"]
    for i in range(score+1, 31):
        current_time = time.time()
        if (current_time-start_time>=120):
            print("Times up!")
            return_score(score, "")
        print(f"\n********LEVEL {i}*********\n")
        a=random.randint(1, 100)
        b= random.randint(11,100)
        operator=random.choice(OPERATORS)
        x=random.randint(1,2)
        if x==1:
            print((f"{b} {operator} ###  = {a}"))
            # number1=int(input("Pls enter a value that may substitute number 1: "))
            number=int(input("Enter a value to substitute ###: "))
            problem=f"{b} {operator} {number}"
            if eval(problem)!=a:
                return_score(score, "")

        if x==2:
            print((f"### {operator} {b}  = {a}"))
            number=int(input("Enter a value to substitute ###:  "))
            problem=f"{number} {operator} ({b})"
            if eval(problem)!=a:
                return_score(score, "")
        score+=1
    print(f"\nCURRENT SCORE= {score}")
    return level4(score, start_time)



def level4(score, start_time):
    
    OPERATORS=["+", "-", "*"]
    for i in range(score+1, 41):
        current_time = time.time()
        if (current_time-start_time>=120):
            print("Times up!")
            return_score(score, "")
        print(f"\n********LEVEL {i}*********\n")
        problem=""
        for j in range(1,4):
            a=random.randint(1, 10)
            operator=random.choice(OPERATORS)
            if j==3:
                  problem+=str(a)
                  break
            problem+=str(a)+" "+ operator+ " "
        ans=input(f"{problem} = ")
        if ans!=str(eval(problem)):
            return_score(score, "")
        score+=1
    print(f"CURRENT SCORE= {score}")
    return_score(score, "DONE")
    

def Greet(name):
    print(f"\nHello {name}, Welcome to the 2 minute Math Challenge")
    print('''RULES OF THE GAME:-
You cannot skip any question and have to solve them in the same order as they appear on the screen.
You need to type the answer of the question and Press enter. To save the answer and move to the next question.
Answer can be a negative number.
''')
    input(("\nPress Enter when you are ready "))
    time.sleep(1)
    start_time = time.time()
    level1(start_time)


def return_score(score, indication):
    sum=0
    global name
    with open("Hiscore.txt", "r") as f:
        data=f.readlines()
        stringx=""
        stringy=""
        for i in range(len(data)):
            if name in data[i]:
                stringx=data[i]
                stringy=stringx.replace(f"{name}    ", "")
                previous_High_Score=int(stringy)
                if score>(int(stringy)):                        #If a new high score is created we directly replace the previous high score.
                    data[i]=f"{name}    {score}\n"
                    sum=1
                    break
                if score<=(int(stringy)):                           
                    sum=2
                    break
            
        if sum==0:
            data.append(f"{name}    {score}\n")        #If we do not put the \n here while appending all the elements,Then 
            previous_High_Score=score                                    # consecutive elements merge and cause problem
    with open("Hiscore.txt", "w") as f:
        f.writelines(list(data))

    if indication=="DONE":
        print(f"WELL DONE! You have succesfully Completed the Challenge!\nFINAL SCORE= {score}\nThankyou for playing the GAME")
    
    if previous_High_Score>score:
        print(f"Game Over\nFINAL SCORE= {score}\nYour previous High Score was {previous_High_Score}\nThankyou for playing the Game")
    
    elif previous_High_Score==score:
        print(f"Game Over!\nCongratulations, you Matched your Previous High Score {previous_High_Score}\nThankyou for playing the game")
    
    elif score>previous_High_Score:
        print(f"Game Over!\nFINAL SCORE= {score}\nCongratulations, you have created a new high score")
    exit()


if __name__=="__main__":
    name=input("Pls enter your name: ").lower()
    Greet(name)
