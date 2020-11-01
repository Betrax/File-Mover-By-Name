import glob
import shutil
import os

Dir = "D:/dir/"  # Where are the files? Don't forget to ad a "/" at the end.
TragetDir = "D:/target/dir/"  # Where are the target folders? Don't forget to ad a "/" at the end.

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
