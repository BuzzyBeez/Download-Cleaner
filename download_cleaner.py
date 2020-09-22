#! python3
# this script will organize your downloads folder. It will make folders for file types like pic, docs, movies
# then it will move those files into those folders

import os          # we need os so we can move through the file system
import shutil       # we need shell utilites so we can move files between folders
import re            # we need Regular expressions to find files and match all files types



getUserDownloadFolder = os.path.expanduser('~/Downloads')             # first we need to get the users home folder and get to downloads
workingDir = os.chdir(getUserDownloadFolder)                          # next we need to move to the working dir (the downloads folder)
getPath  = os.getcwd()

def makeDir(folderName):
    if os.path.exists(f'{getUserDownloadFolder}/{folderName}'):   # this function is for seeing if the folder exsists if does pass
        pass                                                          # if it doesn't then create it
    else:
        os.mkdir(f'{getUserDownloadFolder}/{folderName}')



regexPics = re.compile(r".*?\.jpg|.*?\.png|.*?\.HEIC|.*?\.gif|.*?\.jpeg", re.IGNORECASE)        # now we compile the matches for all the file types
regexPDF = re.compile(r".*?\.pdf", re.IGNORECASE)
regexMovies = re.compile(r".*?\.mp4|.*?\.mov|.*?\.mpg|.*?\.wmv", re.IGNORECASE)
regexWordDocs = re.compile(r".*?\.pages|.*?\.doc|.*?\.docx|.*?\.dotx|.*?\.xls|.*?\.numbers", re.IGNORECASE)
regexOther = re.compile(r".*?\.exe|.*?\.dmg|.*?\.jar", re.IGNORECASE)
regex_pkgs = re.compile(r".*?\.pkg", re.IGNORECASE)


regexList = [regexPics, regexPDF, regexMovies, regexWordDocs, regexOther, regex_pkgs]

fileStringTypes = 'pictures', 'PDF', 'Movies', 'WordDocs', 'Other', 'Packages'         # we need to use multiple assigment so we can add the files to the correct folder


def filesToMatch(regex, stringFileType):                    # this function needs one of the complied matches and one of the assigned stings
    for files in os.listdir(getPath):                        # then list the files in downloads
        matchFiles = regex.findall(files)                    # use the regex to match the file types we want
        if matchFiles == []:                                # if we don't get a match we always get an empty list so we just keep looping if that happens
            continue
        for fileType in matchFiles:
            shutil.move(fileType, f"{getUserDownloadFolder}/{stringFileType}")  # now that we have a list of matched files we take all those files
            print("{} was moved to Pictures".format(fileType))                        # we move them to the same folder and let the user know where they went


for _ in range(0,len(fileStringTypes)):
    makeDir(fileStringTypes[_])                             # make all regexs into a list so we can cycle throught it
    filesToMatch(regexList[_], fileStringTypes[_])
