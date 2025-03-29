"""
Name: DMS (Dokumenten Management System)
Sprache: Python

1. input erstellen
2. klassen erstellen
3. if's erstellen für navigation und bearbeitung aller dateien
"""

# bibliotheken

from pathlib import Path

# commands zu navigation

help = "H"
close = "C"
cont = "Y"
newTextFile = "N"
listAllFiles = "L"

# nochn paar weitere nachrichten/informationen

version = 1.0
willkommenstext = f"""
###### DMS gestartet ######
Version: {version}
Hilfe: {help}
Schließen: {close}
Fortfahren: {cont}\n"""

hilfetext = f"""
###### Anleitung ######
Schließen: {close}
Fortfahren: {cont}\n"""

continuetext = f"""
###### Was möchten sie machen? ######
Neue Datei erstellen: {newTextFile}\n"""

addAttributeName = f"""
Bitte Datei namen eingeben (A-Z, 0-9 oder _ möglich)\n"""

addAttributeFormat = f"""
Bitte Format eingeben, Beispiele:
txt - standart text datei
odt - OpenDocument datei
pdf - Portable Document Format\n"""

print(willkommenstext)

def continueProgram():
    print(continuetext)

def createFile():
    file = txtFileName + "." + txtFileFormat

    with open(file, 'w'):
        print("datei " + file + " erstellt.")

#TODO funktion zur auflistung aller dateien im ordner erstellen

def listFiles():
    filePath = Path().resolve
    allfiles = list(filePath)
    print(allfiles)

# Klasse "File", erstellt die baupläne für die zukünftig erstellten dateien

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
        
        txtFileName = input(addAttributeName + ": ")
        txtFileFormat = input(addAttributeFormat + ": ")
        currentFile = File(txtFileName, txtFileFormat)
        print(currentFile)
        createFile()
    
    elif prompt1 == listAllFiles:
        listFiles()
    
    else:
    
        print("Ungültiger command. Bitte einen vorhandenen command eingeben")

print("Programm wird beendet")