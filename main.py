import time
import eel

right = 0
rightNot = 0

StartTime = None
WinLose = None
nickName = None 
results = False 
block = False 
iteracy = 0
health = 3
images=[]
texts=[]
vozvrat = None
banan = None
dobav = False

by = len(texts)-5
win = len(texts)-4
lose = len(texts)-3
over = len(texts)-2

f = open("texts.txt","r")
pampam = f.read()
texts = pampam.split('|')
del pampam
f.close
del f

f = open("images.txt","r")
pampam = f.read()
images = pampam.split('|')
del pampam
f.close
del f

@eel.expose
def restart():
    global StartTime
    global right
    global rightNot
    global WinLose
    global nickName
    global results
    global dobav
    global banan
    global vozvrat
    global block
    global health
    global iteracy

    StartTime = None
    right = 0
    rightNot = 0
    WinLose = None
    nickName = None
    results = False
    dobav = False
    banan = None
    vozvrat = None
    block = False
    iteracy = 0
    health = 3

@eel.expose
def setNick(txtn):
    global nickName
    nickName = txtn

def normalTime(seconds):
    sekunds = 0
    minutes = 0
    hours = 0
    for i in range(seconds):
        sekunds+=1
        if(sekunds==60):
            sekunds = 0
            minutes +=1
            if(minutes==60):
                minutes = 0
                hours += 1

    return str(hours) +':'+ str(minutes) +':'+ str(sekunds)  

@eel.expose
def getText(textik):
    global StartTime
    global rightNot
    global right

    global WinLose
    global nickName
    global results
    global dobav
    global block
    global health
    global iteracy
    
    global by
    global over
    global win
    global lose
    global vozvrat
    global banan

    if(results==True):
        results = False
        if(textik=="results"):
            vozvrat = """Вот твои результаты {x}:<br/>
            Ты {y}<br/>
            Твое время - {z}<br/>
            Правильных - {a}, не правильных - {b}<br/>
            restart/exit""".format(x = nickName,y = WinLose, z = normalTime(int(time.time() - StartTime)), a = right, b = rightNot)
        else:
            vozvrat = texts[by]  
            
    if block == False:
        if(iteracy==0):
            vozvrat = texts[0]
        elif(iteracy==1):
            if(textik=='y'):
                vozvrat = texts[2]  
            elif(textik=='n'):
                block = True
                vozvrat = texts[1]
            else:
                block = True
                vozvrat = texts[by]
        elif(iteracy==2):
            if(textik=='start'):
                StartTime = time.time()
                vozvrat = texts[4]  
            elif(textik=='leave'):
                block = True
                vozvrat = texts[3]
            else:
                block = True
                vozvrat = texts[by]
        elif(iteracy==3):
            dobav = True
            banan = texts[7]
            if(textik=="def"):
                right +=1
                vozvrat = texts[6]
            elif(textik=="sepra" or textik =="func"):
                rightNot +=1
                vozvrat = texts[5]
                health -=1
            else: 
                rightNot +=1
                vozvrat = texts[over]
                health -=1       
        elif(iteracy==4):
            dobav = True
            banan = texts[10]
            if(textik=="TIMA"):
                right +=1
                vozvrat = texts[9]
            else:
                rightNot +=1
                health-=1
                vozvrat = texts[8]    

        elif(iteracy==5):
            block = True
            dobav = True
            banan = texts[win]
            WinLose = 'победил'
            results = True
            if(textik=="Audi"):
                right+=1
                vozvrat = texts[12]
            elif(textik =="bmw" or textik == "mers"):
                rightNot +=1
                health-=1
                vozvrat = texts[11]
            else:
                rightNot +=1
                health -=1
                vozvrat = texts[over]  

        else:
            return "Ты чего наделал?"
                               
        if(health==0):
            results = True
            block = True
            vozvrat += texts[lose]
            WinLose = 'проиграл'
        elif(health>0 and dobav==True):
            dobav = False
            vozvrat += banan

        iteracy +=1      
  
    return vozvrat      


@eel.expose
def getImage():
    return images[0]

@eel.expose
def getHp():
    global health
    return str(health)+'❦'   
    
eel.init("web")
eel.start("main.html", size=(800,850))