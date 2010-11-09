import os

def getFileTypeStats(rootDirPath, typeList):
    extensionList = list()
    for dirPath, dirNames, fileList in os.walk(rootDirPath):
        for thisFile in fileList:
            thisFileExtension = os.path.splitext(thisFile)[-1]
            if typeList == "all":
                extensionList.append(thisFileExtension)
            else:
                if thisFileExtension in typeList:
                    extensionList.append(thisFileExtension)

        onlyExtensions = list(set(extensionList))
        extensionList.sort()
        results = {}

        for thisExtension in onlyExtensions:
            results[thisExtension] = 0

        for thisExtension in extensionList:
            results[thisExtension] = results[thisExtension] + 1

        totalNumFiles = len(extensionList)

        for thisResult in results:
            tempNum = results[thisResult]
            results[thisResult] = (results[thisResult] / totalNumFiles) * 100
            results[thisResult] = "{number:.{digits}f}".format(number = results[thisResult], digits = 2)
            results[thisResult] = str(tempNum) + " (" + str(results[thisResult]) + "%)"
    return totalNumFiles, results

print("USAGE--------------------")
print("At the first prompt, place the root directory of the files that you wish to analyse, e.g. 'C:\\Users\\Glen Crawford\\Music' (without quotes, obviously).")
print("At the second prompt, enter a comma-separated list of extensions you want to search for, e.g. 'wav,flac,mp3,ogg'. Again, no quotes, and this is case-specific, so 'mp3' and 'MP3' are different. OR you can just type 'all' (no quotes) to grab all file types.")
print("Then hit <enter>. This program will _not_ alter the files or directories in any way, it just grabs the file names and extensions. This program may tank your computer while it's running, though it shouldn't take more than 1 minute (depending on factors such as whether the files are on an internal or external drive).")
print("ABOUT--------------------")
print("Created on request for members of http://www.bt-network.org/board/. Nor me or this program are in any way affiliated with the owners or operators of that site.")
print("Copyright, Glen Crawford, 2010, all rights reserved, etc. Feel free to share this program around, no usage fees or restrictions apply.")
print("If you find an error or bug, let me know at glencrawford@windowslive.com.")
print("Lastly, this was created on-the-fly, and there is very little error checking and handling, so again, there are no guarantees that this will work, this was only tested on Windows 7, using Python 3.1. No guarantees or promises are provided on how it will (or will not) perform on other platforms or OSs.")
print("Right, I have a history essay to write...\n")

path = input("Root directory of files: ")
types = input("File extensions to search for (separate,by,commas): ")

if types == "all":
    typeList = "all"
else:
    typeList = []
    for thisExtension in types.split(","):
        typeList.append("." + thisExtension.strip())

print("Searching...")

try:
    totalNumFiles, results = getFileTypeStats(path, typeList)
except:
    print("Something catastrophic has happened. Let me know at glencrawford@xtra.co.nz")
    print("Most likely, you've entered an invalid directory path, or there are no files at all in that directory or any of its sub-directories")
else:
    print("\n" + str(totalNumFiles), "files found")
    for thisResult in results:
        print(thisResult + ": " + str(results[thisResult]))
    input("Done!")
