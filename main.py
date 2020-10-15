import eel

texts=[]
f = open("texts.txt","r")
pampam = f.read()
texts = pampam.split('/')
del pampam
f.close

@eel.expose
def getText(textik):
    return texts
    
eel.init("web")
eel.start("main.html", size=(800,800))

