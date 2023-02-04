# this steaming pile of shit was created by vito in the span of an hour

# here are all the most important variables vvvvvv

# set this path to your own download folder and make sure to add the extra backslashes
downloadspath = "C:\\Users\\Viktor\\Downloads"

# set this path to where the mods will go, typically youll just have to change D:\\SteamLibrary\\ to C:\\Program Files (x86)\\Steam\\
target = "D:\\SteamLibrary\\steamapps\\common\\Blade & Sorcery\\BladeAndSorcery_Data\\StreamingAssets\\Mods"



# OOOO THIS IS IN ALL CAPS SO YOU HAVE TO READ IT <<<<<<<
# IF SOMETHING FUCKS UP (WHICH IT SHOULDNT) THEN  <<<<<<<
# REREAD THE README.MD ON THE GITHUB PAGE         <<<<<<<
# IF YOU STILL HAVE AN ISSUE THEN GO BOTHER VITO  <<<<<<<
# UNLESS HES ALREADY DEAD IN WHICH CASE GO BOTHER <<<<<<<
# DANIEL INSTEAD BECAUSE HE KNOWS THIS NERD SHIT  <<<<<<<










# keep scrolling down if you wanna see all the nerd shit that this garbage runs on











# if ur a nerd then go ahead and steal my code i couldnt give less fucks
# hell you could even copy the entirety of this code and resell it on v3rm or some shit
# i do not care


# imports (as always)

# zipfile to unzip the zipped folders (i have never seen a folder irl with a zipper)
import zipfile
# import os to read ur files (and send ur google password to a webhook)
import os
# this one is to forcefully remove files from 7zip archives
from pyunpack import Archive
import shutil

# for every file in \downloads
for i in os.listdir(downloadspath):
    print(i)
    fil = os.path.join(downloadspath, i)
    # checking for proof of aliens (files)
    if os.path.isfile(fil):
        if fil.lower().endswith('.zip'):
            with zipfile.ZipFile(fil, 'r') as zip_ref:
                zip_ref.extractall(target)
            os.remove(fil)
        elif fil.lower().endswith('.7z'):
            Archive(fil).extractall(target)
            os.remove(fil)
        elif fil.lower().endswith('rar'):
            Archive(fil).extractall(target)
            os.remove(fil)
        else:
            shutil.move(fil, target)
            os.remove(fil)

print("ok im done bein ur slave can i go home now i need to feed my wife")