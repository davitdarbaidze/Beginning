import random
import time as t



question = {'results':[{'question': "which mountain is hight in the world",'correct_answer':"Everest",'incorrect_answers':["Fiji","Shkhara"]},{'question':"how much is 3*3?",'correct_answer':"9",'incorrect_answers':["6","7"]},{'question':"which is biggest country in the world?",'correct_answer':"Russia",'incorrect_answers':["USA","Hungary"]}]}




play = False
i=0
wrongAnswer = 0
allQuestion = 0
score= 0
updateDict = {}
incorrectAnswer = []
answers = []
countQuest = 0
print("This is a game where you will get questions and you should try to answer them correctly")
input("press Enter to reveal first question")

f = open("Maru.txt","w+")

while play== False:
    
    
    lengthOfDict = len(question['results'])
    i = random.randrange(0,lengthOfDict)    
    print(question['results'][i]['question'])
    countQuest+=1
    allQuestion+=1
    f.write(question['results'][i]['question']+"\n")
    
    for y in question['results'][i]['incorrect_answers']:
        answer_number = 1        
        answers.append(y)
        
        
    answers.append(question['results'][i]['correct_answer'])    
    random.shuffle(answers)
    for answer in answers:
        print(str(chr(64+answer_number))+" - " + answer)
        answer_number+=1
        
    answers.clear()    
    
    
    
    answer = str(input("what is your answer? "))
    if(answer!=str(question['results'][i]['correct_answer'])):
        print("wrong answer")
        wrongAnswer+=1
    else:
        score+=1
        print("you are correct and your score is")
    
    
    game=input("Press any key to continue or type quit to exit and print results? \n")
    if game == "quit":
        print(" correct answer % "+str((score*100)/allQuestion))
        play=True
        continue


    
    if lengthOfDict >= lengthOfDict and countQuest>3:
        morequest=input("would you like to add more questions y/n?")
        if morequest == "y":
            
            anotherQuest = input("type the question \n")
            correctAnswer = input("type correct answer for question \n")
            firstIncorrectAnswer = input("type first incorrect answer \n")
            secondIncorrectAnswer = input("type second incorrect answer \n")
            incorrectAnswer.append(firstIncorrectAnswer)
            incorrectAnswer.append(secondIncorrectAnswer)
            updateDict = [{'question':anotherQuest,'correct_answer':correctAnswer,'incorrect_answers':incorrectAnswer}]
            question['results'].extend((updateDict))
            
            
            
            
            
            
        else:      
            continue
        #update(updateDict)
        #print(question)
    updateDict.clear()
        


    if(game!='quit'):
        
        continue
    else:
        print(" correct answer % "+str((score*100)/allQuestion))
        play=True
f.close()