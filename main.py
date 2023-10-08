import json
import os
from pocketsphinx import LiveSpeech
import speech_recognition as sr
from playsound import playsound
import webbrowser
from pynput.keyboard import Controller

keyboard = Controller()
commands = None


def text_to_speech(text):
    os.system("echo '" + text + "' | piper   --model " + commands["ttsmodel"] + "   --output_file "
                                "Audio/tts.wav")
    playsound('Audio/tts.wav')


def interpret_command(text):
    print("Interpreting the command ...")
    print("Searching in indexed commands ...")
    for j in range(commands["CommandCount"] + 1):
        print(str(j + 1) + ". " + commands[str(j)]["title"])
        if commands[str(j)]["key word"] in text.lower():
            print("Found command! Executing now ...")
            execute_command(j, text)
            print("Executed command. Returning to listening ...")
            break


def execute_command(index, message):
    try:
        additionaldata = message.lower().split(commands[str(index)]["key word"] + " ")[1]
    except IndexError:
        additionaldata = ""
    if "exit" in commands[str(index)]["command"]:
        text_to_speech(commands[str(index)]["comment"])
        exit()
    else:
        if "execute" in commands[str(index)]["command"]:
            os.system(commands[str(index)]["cmd"])
            if commands[str(index)]["key"] != "":
                text_to_speech(commands[str(index)]["comment"].replace(commands[str(index)]["key"], additionaldata))
            else:
                text_to_speech(commands[str(index)]["comment"])
        if "Webbrowser" in commands[str(index)]["command"]:
            tmp = commands[str(index)]["baseURL"] + additionaldata.replace(" ", commands[str(index)]["replace spaces"])
            webbrowser.open(tmp, new=2)

            if commands[str(index)]["key"] != "":
                text_to_speech(commands[str(index)]["comment"].replace(commands[str(index)]["key"], additionaldata))
            else:
                text_to_speech(commands[str(index)]["comment"])


def get_command(rec):
    with sr.Microphone() as source:
        audio_data = rec.record(source, duration=5)
        text = rec.recognize_whisper(audio_data, language="EN")
        print(text)
        interpret_command(text)
    pass


if __name__ == "__main__":
    print("Starting ...")

    print("Searching for commands ...")
    with open("Commands.json", "r") as read_file:
        commands = json.load(read_file)

    print("Found the following commands:")
    for i in range(commands["CommandCount"] + 1):
        print(str(i + 1) + ". " + commands[str(i)]["title"])

    text_to_speech(commands["start message"])

    recognizer = sr.Recognizer()

    speech = LiveSpeech(keyphrase=commands["activation word"], kws_threshold=1e-20)
    for phrase in speech:
        print("Heard keyword!")
        text_to_speech("How may I help you Sir?")
        get_command(recognizer)
