import speech_recognition as sr

recognizer = sr.Recognizer()

# Use the cleaned and converted audio file
audio_file = "test_mono.wav"

with sr.AudioFile(audio_file) as source:
    recognizer.adjust_for_ambient_noise(source)  # Reduce background noise
    audio = recognizer.record(source, duration=3)  # Process first 3 seconds

try:
    text = recognizer.recognize_google(audio, show_all=True)  # Show all possible results
    if text:
        print("Recognized Text:", text)
    else:
        print("No speech detected, try increasing volume or reducing noise.")
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand the audio")
except sr.RequestError:
    print("Could not request results from Google Speech Recognition service")
