import eel

texts=[]
f = open("texts.txt","r")
pampam = f.read
f.close
for i in pampam:
    if pampam[i]==';':
        print(i)
        break

@eel.expose
def getText(textik):
    return "lalala"
    
eel.init("web")
eel.start("main.html", size=(800,800))
