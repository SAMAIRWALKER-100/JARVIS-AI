from audioop import error
import pyttsx3
import speech_recognition as sr

class AI():
    __name = "JARVIS"
    __skill = []
    
    def __init__(self, name=None):
        self.engine = pyttsx3.init()
        self.r = sr.Recognizer()
        self.m = sr.Microphone()
        
        if name is not None:
            self.__name = name
            
        print("Listening")
        with self.m as source:
            self.r.adjust_for_ambient_noise(source)
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        sentence = "Hello, my name is" + self._name
        self._name = value
        self.engine.say(sentence)
        self.engine.runAndWait()
        
    def say(self, sentence):
        self.engine.say(sentence)
        self.engine.runAndWait()
        
    def listen(self):
        print("Say Something")
        with self.m as source:
            audio = self.r.listen(source)
        print("Got it")
        try:
            phrase = self.r.recognize_google(audio, show_all=False, language=("english, US"))
            self.engine.runAndWait()
        except error:
            print("Sorry, I didn't hear.",error)
            self.engine.say("Sorry, I didn't hear that")
            self.engine.runAndWait()
        return phrase