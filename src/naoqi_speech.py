import naoqi
import sys

from naoqi import ALProxy
IP   = "10.0.1.3"
PORT = 9559
loggerProxy = ALProxy("ALTextToSpeech", IP, PORT)

def say(speech):
    loggerProxy.say(speech)
