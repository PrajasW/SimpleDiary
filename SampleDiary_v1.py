# Features
# Add a new Entry (1 Entry/day) [DONE]
# NOTE: write <> to put in Enter
# View Any Entry [WIP] 
# Add to Today's Entry [WIP]
# Delete Any Entry [DONE]

from datetime import datetime
import os


class DairyEntry:

    def read():
        pass
    
    def add():
        pass
    
    def newEntry():
        # to get today's date and time
        now = datetime.now()
        # to get it formated
        dayInFileName = now.strftime("%d_%m_%Y")
        dayAndTimeInEntry = now.strftime("%d %B, %Y \n\n[%H:%M]\n")

        newEntry = input(now.strftime("[%H:%M]\n"))
        newEntryEdit = newEntry.replace("<>","\n")

        with open(f"Dairy_{dayInFileName}.txt",'w') as Entry:
            Entry.write(f"{dayAndTimeInEntry}"+newEntryEdit)
    
    def deleteEntry():
        day = input("Enter the date(dd_mm_yy) of entry to delete:")
        fileToDelete = f"Dairy_{day}.txt"
        if(os.path.isfile(fileToDelete) ==True):
            os.remove(fileToDelete)
        else:
            print("File Does Not Exist")


# TESTING
Entry1 = DairyEntry()
DairyEntry.deleteEntry()







