import speech_recognition as sr

recognizer = sr.Recognizer()
mic = sr.Microphone(device_index=1)  # Change index if needed

with mic as source:
    print("Listening...")
    recognizer.adjust_for_ambient_noise(source)  # Reduce background noise
    audio = recognizer.listen(source)  # Listen to the microphone input

try:
    text = recognizer.recognize_google(audio)
    print("Recognized text:", text)
except sr.UnknownValueError:
    print("Could not understand the audio.")
except sr.RequestError:
    print("Could not connect to Google Speech Recognition service.")
