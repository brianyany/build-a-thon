# coding: utf-8

# NOTE: this example requires PyAudio because it uses the Microphone class

import speech_recognition as sr
import time

# obtain audio from the microphone
r = sr.Recognizer()
mic = sr.Microphone()

# Setup Block
# Let's calibrate the microphone for ambient noise first.
with mic as source:
    print("Calibrating the microphone...")
    r.adjust_for_ambient_noise(source)
    print("Calibration complete!")

# Let's try a very aggressive pause threshold.
# r.pause_threshold = 0.3

# recognize speech using Sphinx
def callback(recognizer, audio):
    try:
        recognized_speech = r.recognize_sphinx(audio, language='en-US')
        print("Sphinx thinks you said " + recognized_speech)
        
        # Do something with the recognized speech segment
        
    except sr.UnknownValueError:
        print("Sphinx could not understand audio")
    except sr.RequestError as e:
        print("Sphinx error; {0}".format(e))

# start listening in the background (note that we don't have to do this inside a `with` statement)
stop_listening = r.listen_in_background(mic, callback)
# `stop_listening` is now a function that, when called, stops background listening

# do some unrelated computations for 60 seconds
for _ in range(60): time.sleep(0.1)  # we're still listening even though the main thread is doing other things

print("We stopped listening.")
# calling this function requests that the background listener stop listening
stop_listening(wait_for_stop=False)

