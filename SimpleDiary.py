# <> PROGRESS <>
# homeScreen()  [WORKING]
# confirmAction() [WORKING]
# newEntry() [WORKING] --> n
# addEntry() [WORKING] --> a
# readEntry() [WORKING] --> r
# deleteEntry() [WORKING] --> d
# to end the program [WORKING] --> e


from datetime import datetime
import os

# <><>Program<><>

now = datetime.now()
dayInFileName = now.strftime("%d_%m_%y")
dayAndTimeInEntry = now.strftime("%d %B, %Y \n\n[%H:%M]\n")
fileName = f"Diary_{dayInFileName}.txt"
dayInFileName = now.strftime("%d_%m_%y")
timeInEntry = now.strftime("\n[%H:%M]\n")
firstTime = True

def saveLocation():
    pass

def homeScreen():
    global passValue
    global firstTime
    if(firstTime == True):
        doWhat = input("\n### WELCOME TO SIMPLE DIARY ###\nWhat would you like to do? \n")
        firstTime = False
    else:
        doWhat = input("\nWhat else would you like to do? \n")
    
    doWhatKey = doWhat.lower()[0]
    validKeys = ['a','d','e','n','r']
    if(doWhatKey not in validKeys):
        print("Invalid Input")
        homeScreen()
    else:
        if(doWhatKey == 'a'):
            addEntry()
            homeScreen()
        if(doWhatKey == 'd'):
            deleteEntry()
            homeScreen()
        if(doWhatKey == 'e'):
            exit()
        if(doWhatKey == 'n'):
            newEntry()
            homeScreen()
        if(doWhatKey == 'r'):
            readEntry()
            homeScreen()

def confirmAction():
    confirmSent = input("\nConfirm Action?:")
    confirmKey = confirmSent.lower()[0]

    if(confirmKey == 'n'):
        homeScreen()
    elif(confirmKey == 'y'):
        pass
    else:
        print("Invalid Input")
        confirmAction()

def newEntry():
    newEntry = input(now.strftime("\n[%H:%M]\n"))
    newEntryEdit = newEntry.replace("<>","\n")
    confirmAction()
    with open(fileName,'w') as Entry:
        Entry.write(f"{dayAndTimeInEntry}"+newEntryEdit)

def addEntry():
    if(os.path.exists(fileName)):
        addEntry = input(now.strftime("\n[%H:%M]\n"))
        addEntryEdit = addEntry.replace('<>','\n')
        with open(fileName) as f:
            oldEntry = fileName
        with open(fileName,'a') as f:
            confirmAction()
            f.write(f"{timeInEntry}" + addEntryEdit)
    else:
        print("Create a New Entry first")

def readEntry():
    day = input("Enter the date(dd/mm/yy) of entry to read:")
    day = day.replace('/','_')
    readWhat = f"Diary_{day}.txt"
    if(os.path.exists(readWhat) == True):
        with open(readWhat) as f:
            readDiary = f.read()
        print("\nThe Diary Reads,\n")
        print(readDiary)
    else:
        day = day.replace('_','-')
        print(f"No Entry for {day}")

def deleteEntry():
    day = input("Enter the date(dd/mm/yy) of entry to delete:")
    day = day.replace('/','_')
    deleteWhat = f"Diary_{day}.txt"
    if(os.path.exists(deleteWhat) == True):
        confirmAction()
        os.remove(deleteWhat)
        print(f"{deleteWhat} is Deleted")
    else:
        day = day.replace('_','-')
        print(f"No Entry for {day}")

# Main function
homeScreen()









