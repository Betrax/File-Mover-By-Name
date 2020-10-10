import glob
import shutil

Dir = "D:/OneDrive/Documents/"  # Where are the files?
TragetDir = "D:/OneDrive/Documents/school/6a9/"  # Where are the target files?

StartIndex = len(Dir)  # The chars of the Dir are useless

FileNames = glob.glob(Dir + "*.docx")  # Scans the Dir for files with the slected extension


for x in range(len(FileNames)):  # Each file gets moved one by one
    Index = FileNames[x].find("-")  # I always create my files using: class + "-" + topic
    SFolder = FileNames[x][StartIndex:Index]  # My folders are always named after the subject, so "Math- exam 1.docx" should be placed in a folder named "Math"

    shutil.move(FileNames[x], TragetDir + SFolder)  # moves to the target folder