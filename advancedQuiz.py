import tkinter
window=tkinter.Tk()
startframe=tkinter.Frame()
endFrame=tkinter.Frame()
window.title('Quiz')

question=' '
a1=' '
a2=' '
a3=' '
a4=' '
realAnswer=''
questions=[]
qinfo=[]
frames=[]
QuizScoreSave=[]
QuizScore=[]
score=0
username=''
Questions=open('quizQuestions.txt','r')
from AdvancedQuizScoreBoard import data
for w in data:
    QuizScore.append(w)
lineCount=1
tkinterCounter=0
v=tkinter.IntVar()
v.set(1)

def Start():
    global tkinterCounter,username
    username=e.get()
    startframe.grid_forget()
    frames[tkinterCounter].grid(row=0,column=0)


def Next():
    global tkinterCounter,score
    a = checkAnswer()
    if a == True:
        score += 1
    if tkinterCounter==len(frames)-1:
        frames[tkinterCounter].grid_forget()
        endFRame()
        endFrame.grid(row=0,column=0)
    else:
        frames[tkinterCounter].grid_forget()
        tkinterCounter += 1
        frames[tkinterCounter].grid(row=0,column=0)

def checkAnswer():
    if questions[tkinterCounter][5][7:].strip()==questions[tkinterCounter][v.get()].strip():
        return True

def mySort(v):
    return v[1]

def Quit():
    global QuizScore
    SaveOficial = open('AdvancedQuizScoreBoard.py', 'w')
    if len(frames)-1==tkinterCounter:
        QuizScoreSave.append([username, score])
        QuizScore+=QuizScoreSave
        sortedQuizScore=sorted(QuizScore, key=mySort)
        QuizScore=sortedQuizScore
        QuizScore.reverse()
        SaveOficial.write('data=[')
        for e in QuizScore:
            SaveOficial.write(str(e)+',')
        SaveOficial.write(']')
        SaveOficial.close()
    exit()

def startFrame():
    l=tkinter.Label(startframe,text="Quiz and Thing")
    e=tkinter.Entry(startframe)
    b=tkinter.Button(startframe,text="Start",command=Start)
    b2=tkinter.Button(startframe, text="Quit",command=Quit)
    l.grid(row=0,column=0,columnspan=3)
    e.grid(row=1,column=0,columnspan=3)
    b.grid(row=2,column=0)
    b2.grid(row=2,column=1)
    startframe.grid(row=0, column=0)
    return e

def endFRame():
    l=tkinter.Label(endFrame,text="You finished the quiz!")
    l2=tkinter.Label(endFrame,text="You got "+str(score)+" questions correct!")
    b=tkinter.Button(endFrame,text="Quit",command=Quit)
    l.grid(row=0,column=0)
    l2.grid(row=1,column=0)
    b.grid(row=2,column=0)





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
        qinfo.append(realAnswer)
        lineCount+=1
    elif lineCount==7:
        lineCount = 1

        frame=tkinter.Frame(window)
        l=tkinter.Label(frame,text=question)
        b=tkinter.Radiobutton(frame,text=a1,value=1,variable=v)
        b2 = tkinter.Radiobutton(frame,text=a2,value=2,variable=v)
        b3 = tkinter.Radiobutton(frame,text=a3,value=3,variable=v)
        b4 = tkinter.Radiobutton(frame,text=a4,value=4,variable=v)
        b5=tkinter.Button(frame,text='Next',command=Next)
        b6 = tkinter.Button(frame, text='Quit', command=Quit)
        l.grid(row=0,column=0,columnspan=2)
        b.grid(row=1,column=0,columnspan=2)
        b2.grid(row=2,column=0,columnspan=2)
        b3.grid(row=3,column=0,columnspan=2)
        b4.grid(row=4,column=0,columnspan=2)
        b5.grid(row=5,column=0)
        b6.grid(row=5, column=1)
        questions.append([question,a1,a2,a3,a4,realAnswer])
        frames.append(frame)

e=startFrame()
window.mainloop()
#homework: Make prime number checker with server and client