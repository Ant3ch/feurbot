import speech_recognition as sr
import time
from pydub import AudioSegment
from pydub.playback import play
from pyfiglet import Figlet
import shutil
import os

recognizer = sr.Recognizer()
mic = sr.Microphone()

feur_count = 0

f = Figlet(font='avatar')


def DrawText(text, center=True):
    if center:
        print(*[x.center(shutil.get_terminal_size().columns) for x in f.renderText(text).split("\n")], sep="\n")
    else:
        print(f.renderText(text))


def clean():
    os.system("cls")


def audioRecord():
    global feur_count
    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio, language="fr-FR")

        if "quoi" in str(text):
            print("feur")
            feur_sound = AudioSegment.from_wav("feur.wav")
            play(feur_sound)
            feur_count += 1
            clean()
        elif "allô" in str(text):
            print("à l'huile")
            huile_sound = AudioSegment.from_wav("à-l_huile.wav")
            play(huile_sound)
            feur_count+=1
            clean()

    except sr.UnknownValueError:
        print("say it again")
        time.sleep(1)
        clean()
    except sr.RequestError:
        print("service down")
        time.sleep(1)
        clean()


def animation_train():
    os.system('cls')
    filenames = ["train1.txt", "train2.txt", "train3.txt", "train4.txt", "train5.txt", "train6.txt", "train7.txt",
                 "train8.txt", "train9.txt", "train10.txt", "train11.txt", "train12.txt","train13.txt","train14.txt","train15.txt","train16.txt"]
    frames = []
    for name in filenames:
        with open(name,"r", encoding="utf8") as f :
            frames.append(f.readlines())

    for frame in frames :
        print("".join(frame))
        if "train12.txt" in frames:
            os.system("color b")
            os.system('color d')
        time.sleep(0.3)

        os.system('cls')


animation_train()
while True:

    audioRecord()
    DrawText(str(feur_count), center=True)
    DrawText(str("feur counter"), center=True)
