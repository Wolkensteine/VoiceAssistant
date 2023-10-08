# VoiceAssistant
This is a simple **VoiceAssistant** that is easy to use and processes your voice locally, though you sadly still need an internet connection for text to speech (I am working on making it available offline). <br>
This project is written in Python and you can easyly create commands in JSON, that are automatically used by the assistant when you restart it with the new file.
# Compatibility
### Linux
I have developed this on Linux Mint on x86 architecture, so it should be able to run on all Ubuntu (based) linux machines and as it is based on Python you should be able to get it working on all Linux machines.<br>
I am planning to run this on a Raspberry Pi, when I get that working, I will create a setup tutorial for it. 
### Windows
I do not have tested this on Windows, though it should run on Windows. I am planning to test it on a Windows 11 Virtual machine, updates will follow someday™
### Mac OS | OSX
I do not have tested this on Mac OS, though it should run on it. As I do not have access to a Mac of any sorts, I am not gonna test it.
# Requirements
1. Python 3.x
2. PyAudio ```pip install PyAudio```or ```apt-get install python-pyaudio```
3. [SpeechRecognition](https://pypi.org/project/SpeechRecognition/) ```pip install SpeechRecognition```
4. [PocketSphinx](https://pypi.org/project/pocketsphinx/) ```pip install pocketsphinx```
5. [Piper TTS](https://pypi.org/project/piper-tts/) ```pip install piper-tts```
