import os
import time

DAYS = 5                #Max liftime of the file, files older than 5 days will be deleted!
FOLDERS = [
            "/home/anatoly/Desktop/cleanup/misc"
            "/home/anatoly/Desktop/cleanup/oldstuff"
            "/home/anatoly/Desktop/cleanup/oldlogs"
]

TOTAL_DELETED_SIZE  = 0
TOTAL_DELETED_FILES = 0
TOTAL_DELETED_DIRS  = 0

#--------------------------MAIN-----------------------------------

starttime = time.asctime()
finishtime = time.asctime()

nowtime = time.time()                         #Get current time in seconds
oldtime = nowtime - 60 * 60 * 24 * DAYS       #Time (DAYS) ago 

def deleteoldfiles(folder):
    global TOTAL_DELETED_FILES
    global TOTAL_DELETED_SIZE
    for path, dirs, files in os.walk(folder):
        for file in files:
            filename = os.path.join(path, file)   # Get full path to file
            filetime = os.path.getmtime(filename)
            if filetime < oldtime:
                sizefile = os.path.getsize(filename)
                TOTAL_DELETED_SIZE  += sizefile
                TOTAL_DELETED_FILES += 1 
                print("Deleting file: " + str(filename))
                os.remove(filename)


def deleteemptydirs(folder):
     global TOTAL_DELETED_DIRS
     for path, dirs, files in os.walk(folder):
         if (not dirs) and (not files):
             TOTAL_DELETED_DIRS +=1
             print("Removing empty directory: " + str(path))
             os.rmdir(path)


for folder in FOLDERS:
    deleteoldfiles(folder)
    deleteemptydirs(folder)


print("-------------------------------------------------------")
print("Start time: "            + str(starttime))
print("Total deleted size: "    + str(TOTAL_DELETED_SIZE/1024/1024) + "MB")
print("Total deleted files: "   + str(TOTAL_DELETED_FILES))
print("Total deleted folders: " + str(TOTAL_DELETED_DIRS))
print("Finish time:"            + str(finishtime))
print("-------------------------------------------------------")

