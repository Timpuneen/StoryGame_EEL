import eel

@eel.expose
def getText(textik):
    return "blabla"+textik


eel.init("web")
eel.start("main.html", size=(800,800))
