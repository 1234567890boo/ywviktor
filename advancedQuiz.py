import tkinter
window=tkinter.Tk()
window.title('Quiz')
question=''
a1=''
a2=''
a3=''
a4=''
realAnswer=''
Questions=open('quizQuestions.txt','r')
lineCount=1
for q in Questions:
    q=q.strip()
    if lineCount==1:
        question=q
        lineCount+=1
    elif lineCount==2:
        a1=q
        lineCount += 1
    elif lineCount==3:
        a2=q
        lineCount += 1
    elif lineCount==4:
        a3=q
        lineCount += 1
    elif lineCount==5:
        a4=q
        lineCount += 1
    elif lineCount==6:
        realAnswer=q
    elif lineCount==7:
        lineCount=1
    print(question)

#homework: use tkinter to make frames based on the questions, when clicked next it will go to the next wuestion and if there are no more questions it tells you how may question you got wrong