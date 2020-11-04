import time
import eel

right = 0
rightNot = 0

resTime = None
StartTime = None
WinLose = None
nickName = None 
results = False 
block = False 
iteracy = 0
health = 5
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
    global resTime
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

    resTime = None
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
    health = 5

@eel.expose
def setNick(txtn):
    global nickName
    nickName = txtn

@eel.expose
def getIteracy():
    global iteracy
    return iteracy

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
    global resTime
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
            restart/exit""".format(x = nickName,y = WinLose, z = resTime, a = right, b = rightNot)
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
            banan = texts[57]
            if(textik=="TIMA"):
                right +=1
                vozvrat = texts[9]
            else:
                rightNot +=1
                health-=1
                vozvrat = texts[8]    

        elif(iteracy==5):
            dobav = True
            banan = texts[15]
            if(textik=="RUR\'U\'"):
                right+=1
                vozvrat = texts[59]
            else:
                rightNot+=1
                health-=1
                vozvrat  = texts[58]

        elif(iteracy==6):
            dobav = True
            banan = texts[19]
            if(textik=="-7,1"or textik=="1,-7"):
                right+=1
                vozvrat = texts[16]
            elif(textik=='1'or textik=='-7'):
                right+=1
                vozvrat = texts[17]
            else:
                rightNot+=1
                health-=1
                vozvrat = texts[18]
        elif(iteracy==7):
            dobav = True
            banan = texts[22]
            if(textik=='33'):
                right+=1
                vozvrat = texts[20]
            else:
                rightNot+=1
                health-=1
                vozvrat=texts[21]
        elif(iteracy==8):
            dobav = True
            banan = texts[25]
            if(textik=='1'):
                right+=1
                vozvrat = texts[23]
            else:
                rightNot+=1
                health-=1
                vozvrat = texts[24]
        elif(iteracy==9):
            dobav = True
            banan = texts[28]
            if(textik=='хоба'):
                right+=1
                vozvrat = texts[26]
            else:
                rightNot+=1
                health-=1
                vozvrat = texts[27]
        elif(iteracy==10):
            dobav = True
            banan = texts[31]
            if(textik=='3'):
                right+=1
                vozvrat = texts[30]
            elif(textik=='2'or textik =='1'):
                rightNot+=1
                health-=1
                vozvrat = texts[29]
            else:
                rightNot+=1
                health-=1
                vozvrat = texts[over]
        elif(iteracy==11):
            dobav = True
            banan = texts[34]
            if(textik=="OLD TOWN ROAD"):
                right+=1
                vozvrat = texts[32]
            else:
                rightNot+=1
                health-=1
                vozvrat = texts[33]
        elif(iteracy==12):       
            dobav = True
            banan = texts[37]
            if(textik=='Timpuheen'):
                right+=1
                vozvrat = texts[35] 
            else:
                rightNot+=1
                health-=1
                vozvrat = texts[36]
        elif(iteracy==13):
            dobav = True
            banan = texts[39]
            right+=1
            vozvrat = texts[38]            
        elif(iteracy==14):
            dobav = True
            banan = texts[42]
            if(textik=='256'):
                right+=1
                vozvrat = texts[40]
            else:
                rightNot+=1
                health-=1
                vozvrat = texts[41]
        elif(iteracy==15):
            dobav = True
            banan = texts[44]
            if(textik=='avatar'or textik=='gravityFalls'or textik=='naruto'):
                right+=1
                vozvrat = texts[43]
            else:
                rightNot+=1
                health-=1
                vozvrat = texts[over]
        elif(iteracy==16):
            dobav = True
            banan = texts[47]
            if(textik=='elite'):
                right+=1
                vozvrat = texts[46]
            else:
                rightNot+=1
                health-=1
                vozvrat = texts[45]
        elif(iteracy==17):
            dobav = True
            banan = texts[50]
            if(textik=='в правде'):
                right+=1
                vozvrat = texts[49]
            elif(textik=='в единстве' or textik=='в дружбе'):
                rightNot+=1
                health-=1
                vozvrat = texts[48]
            else:
                rightNot+=1
                health-=1
                vozvrat = texts[over] 
        elif(iteracy==18):
            dobav = True
            banan = texts[53]
            if(textik=='ВЗРЫВ'):
                right+=1
                vozvrat = texts[51]
            else:
                rightNot+=1
                health-=1
                vozvrat = texts[52]
        elif(iteracy==19):
            dobav = True
            banan = texts[10]
            if(textik=='ампелография'):
                right+=1
                vozvrat = texts[55]
                health+=1
            elif(textik=='skip'and health>2):
                health-=2            
                vozvrat = texts[54]
            else:
                rightNot+=1
                health=0
                vozvrat=texts[56]  
        elif(iteracy==20):
            dobav = True
            banan = texts[60]
            if(textik=="Audi"):
                right+=1
                vozvrat = texts[13]
            elif(textik == "mers"):
                rightNot +=1
                health-=1
                vozvrat = texts[14]
            elif(textik=="bmw"):
                rightNot +=1
                if(health>=2):
                    health-=2
                    vozvrat = texts[11]
                else:
                    health=0
                    vozvrat = texts[12] 
            else:
                rightNot +=1
                health -=1
                vozvrat = texts[over] 

        elif(iteracy==21):
            dobav = True
            banan = texts[63]
            if(textik=="first 2 layers"):
                right+=1
                vozvrat = texts[61]
            else:
                rightNot+=1
                health-=1
                vozvrat = texts[62]
        elif(iteracy==22):
            block = True
            dobav = True
            banan = texts[win]
            WinLose = 'победил'
            results = True
            resTime = normalTime(int(time.time() - StartTime))
            if(textik=='Тони'):
                right+=1
                vozvrat = texts[66]
            elif(textik=='Стив'):
                rightNot+=1
                health-=1
                vozvrat = texts[64]
            elif(textik=='Бенедикт'):
                rightNot+=1
                health-=1
                vozvrat = texts[65] 
            else:
                rightNot +=1
                health -=1
                vozvrat = texts[over]             

        else:
            return "Ты чего наделал?"
                               
        if(health==0):
            results = True
            resTime = normalTime(int(time.time() - StartTime))
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