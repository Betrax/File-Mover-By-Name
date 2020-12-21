import glob
import shutil
import os

Dir = "D:/OneDrive/Documents/"  # Where are the files? Add "/" at the end of your directory.
TragetDir = "D:/OneDrive/Documents/school/6a9/"  # Where are the target folders? Add "/" at the end of your directory.

FileNames = glob.glob(Dir + "*-*")  # scans the dir with the selected character (*[selected character]*), searches directly for the name now.

StartIndex = len(Dir)  # The chars of the Dir are useless
for x in range(len(FileNames)):  # Each file gets moved one by one
    Index = FileNames[x].find("-")  # I always create my files using: "class + "-" + topic" way
    SFolder = FileNames[x][StartIndex:Index]  # My folders are always named after the subject, so "Math- exam 1.docx" should be placed in a folder named "Math"

    try: #tries to make a target dir
        os.makedirs(TragetDir + SFolder)
    except: #if the directory already exists just skips this process
        pass
    
    shutil.move(FileNames[x], TragetDir + SFolder)  # moves to the target folder
