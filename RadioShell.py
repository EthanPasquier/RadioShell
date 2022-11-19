#!/usr/bin/env python3
import webbrowser
import os
import random

def ft_musique_random():
    f = open("data", "r")
    lines = f.readlines()
    nblink = random.randint(0,len(lines)-1)
    if ('"' in lines[nblink]):
        print("\nNom et artiste : \033[96m"+lines[nblink].split('"')[1])
    get_url= webbrowser.open(lines[nblink])
    f.close()

def ft_add_song():
    f = open("data", "a")
    titre = input("le nom de la musique : ")
    artiste = input("le nom de l'artiste : ")
    url = input("L'url de la musique sur youtube : ")
    f.write(url+' "'+titre+" - "+artiste+"\n")
    os.system("clear")
    f.close()

def ft_list_song():
    f = open("data", "r")
    lines = f.readlines()
    i = 0
    while(i < len(lines)):
        print(lines[i].split('"')[1])
        i += 1

def ft_sync():
    os.system("git stash > /dev/null")
    os.system("git pull > /dev/null")
    os.system("git stash apply > /dev/null")
    os.system("git add data > /dev/null")
    os.system("git commit -m \"user commit music\" > /dev/null")
    os.system("git push > /dev/null")
    print("\033[92mprogramme synchronisé ✅")

def programm():
    random_color = random.randint(91,96)
    os.system("clear")
    f = open("title", "r")
    titre = f.read()
    print("\033["+str(random_color)+"m"+titre)
    f.close()
    print("\033[0mRandom music\033[93m [1] \033[0m- Add music\033[93m [2] \033[0m- List music\033[93m [3] \033[0m- Sync\033[93m [4]")
    reponse = input("\n\033[0moption : \033[93m")
    print("\033[0m")
    if (reponse == '1'):
        ft_musique_random()
    elif (reponse == '2'):
        ft_add_song()
    elif (reponse == '3'):
        ft_list_song()
    elif (reponse == '4'):
        ft_sync()
    else:
        print("\033[91mBad Input")

i = '1'
while(i == '1'):
    programm()
    i = input("\033[0mPour revenir au programme\033[93m [1] : ")
