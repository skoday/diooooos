import speech_recognition as sr

# Create a recognizer
recognizer = sr.Recognizer()

# Use the microphone as the audio source
with sr.Microphone() as source:
    print("Speak up...")
    audio = recognizer.listen(source)

try:
    # Use Google Speech Recognition to transcribe the audio
    text = recognizer.recognize_google(audio, language='en-US')  # Change to your desired language if different
    print("You said:", text)
except sr.UnknownValueError:
    print("Couldn't understand the audio")
except sr.RequestError as e:
    print("Error fetching results; {0}".format(e))
