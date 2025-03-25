"""
Name: DMS (Dokumenten Management System)
Sprache: Python

1. input erstellen
2. klassen erstellen
3. if's erstellen für navigation und bearbeitung aller dateien
"""

help = "H"
close = "C"
cont = "Y"
newTextFile = "N"

version = 1.0
willkommenstext = f"""
###### DMS gestartet ######
Version: {version}
Hilfe: {help}
Schließen: {close}
Fortfahren: {cont}

"""

hilfetext = f"""
###### Anleitung ######
Schließen: {close}
Fortfahren: {cont}

"""

continuetext = f"""
###### Was möchten sie machen? ######
Neue Datei erstellen: {newTextFile}

"""

addAttributeName = f"""
Bitte Datei namen eingeben (A-Z, 0-9 oder _ möglich)

"""

addAttributeFormat = f"""
Bitte Format eingeben (txt möglich)

"""

print(willkommenstext)

def continueProgram():
    print(continuetext)

def createFile():
    file = txtFileName + "." + txtFileFormat

    with open(file, 'w'):
        print("datei " + file + " erstellt.")
#TODO: Klassen erstellen

class File:
    def __init__(self, name, fileFormat):
        self.name = name
        self.fileFormat = fileFormat

    def __str__(self):
        return(self.name + "." + self.fileFormat + " objekt erstellt")

while True:
    prompt1 = input(": ")
    if prompt1 == help:
    
        print(hilfetext)
    
    elif prompt1 == close:
    
        break
    
    elif prompt1 == cont:
        
        continueProgram()
    
    elif prompt1 == newTextFile:
        
        txtFileName = input(addAttributeName + ":")
        txtFileFormat = input(addAttributeFormat + ":")
        currentFile = File(txtFileName, txtFileFormat)
        print(currentFile)
        createFile()
    else:
    
        print("Ungültiger Keyword. Bitte einen vorhandenen Keyword eingeben")

print("Programm wird beendet")