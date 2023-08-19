# I made KBC game using only if-else,loop,list. In this game you have to answer 5 questions ,also there are two lifelines 50-50 and ask the expert,you can use that lifelines if you dont know the answer.If you will choose the wrong answer game will over there, one the other hand after every correct answer you will get +100 marks. At last your score will be displyed on the screen.

name=input("Enter your name: ")
print("Hello ",name,"!")
print("Welcome to KON BANEGA CAROREPATI")
start=input("Enter y/Y to start the game")
questions=["Which programming language is often called the snake language?",
        "Which of the following is not a valid Python data type?",
        "In Python, what is the result of 2 + 3 * 4?",
        "What is the keyword used to define a function in Python?",
        "What is the result of 5 // 2 in Python?"]
options=["a)Java   b)Python   c)Ruby   d)C++",
         "a)int    b)str   c)char    d)float",
         "a)14    b)20   c)18    d)10",
         "a)func   b)define    c)function    d)def",
         "a)2.5    b)2     c)2.0   d)3"]
solutions=["b","c","a","d","b"]
life_line=["a)50-50",
          "b)ask the expert"]
life_line_options=["b)Python      c)Ruby",
                 "a)int          c)char",
                 "c)function      d)def",
                 "a)2.5        b)2"]
l=2
total_points=500
points=0
if start=="y" or start=="Y":
    for i in range(5):
        print(questions[i])
        print(options[i])
        if l>0:
            life=input("Do you want to use lifeline: y/n")
            if life=='Y' or life=='y':
                print("you have",l,"lifeline")
                l-=1
                for j in life_line:
                    print(j)
                inp=input("select a lifeline")
                if inp=="a":
                    life_line.remove("a)50-50")
                    print("now you have 2 options only")
                    print(life_line_options[i])
                elif inp=="b":
                    print("Expert: ",solutions[i],"is the answer.")
                    life_line.remove("b)ask the expert")
                ans=input("Select options: a , b , c , d ")
                if ans==solutions[i]:
                    print("CORRECT")
                    print("You got +100 points")
                    points+=100
                else:
                    print("WRONG , you loose the game!")
                    print("Correct option is",solutions[i])
                    break
            elif life=="N" or life=="n":
                print("you have",l,"lifeline")
                ans=input("Select options: a , b , c , d ")
                if ans==solutions[i]:
                    print("CORRECT")
                    print("You got +100 points")
                    points+=100
                else:
                    print("WRONG , you loose the game!")
                    print("Correct option is",solutions[i])
                    break
                
        else:
            print("you have",l,"lifeline")
            ans=input("Select options: a , b , c , d ")
            if ans==solutions[i]:
                print("CORRECT")
                print("You got +100 points")
                points+=100
            else:
                print("WRONG , you loose the game!")
                print("Correct option is",solutions[i])
                break

print("YOUR SCORE: ",points,"/",total_points)            
print("THANKS FOR PLAYING")
            
        
    
