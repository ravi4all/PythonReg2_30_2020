import os, glob, random

path = r"C:\Users\asus\Documents\Data\songs"
songs = []
for root,folder,files in os.walk(path):
    #print(root,folder,file)
    for file in files:
        songPath = root + "\\" + file
        songs.append(songPath)


song = random.choice(songs)
os.startfile(song)
