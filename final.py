import speech_recognition as sr

# Initialize recognizer class (for recognizing the speech)
r = sr.Recognizer()

# Set the silence threshold dynamically based on the ambient noise level
r.dynamic_energy_adjustment_ratio = 1.5

# Reading Microphone as source
# Listening to the speech and store it in the audio_text variable
with sr.Microphone() as source:
    print("Talk")
    # Adjust the energy threshold dynamically during listening
    r.adjust_for_ambient_noise(source)
    audio_text = r.listen(source, timeout=5)
    print("Time over, thanks")

# Recognize the speech
try:
    # Using Google Speech Recognition
    print("Text: " + r.recognize_google(audio_text, language='kn-IN'))
except sr.UnknownValueError:
    print("Sorry, I did not understand")
except sr.RequestError:
    print("Sorry, I could not connect to the service")
