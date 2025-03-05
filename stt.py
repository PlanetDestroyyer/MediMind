import speech_recognition as sr

def speech_to_text():
    # Create a recognizer object
    recognizer = sr.Recognizer()
    
    # Use the default microphone as the audio source
    with sr.Microphone() as source:
        print("Please speak now...")
        
        # Adjust for ambient noise and listen
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)
        
        try:
            # Use Google Speech Recognition
            text = recognizer.recognize_google(audio)
            print("You said:", text)
            return text
        
        except sr.UnknownValueError:
            print("Sorry, could not understand what you said.")
        
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
    
    return None

# Run the speech-to-text function
if __name__ == "__main__":
    speech_to_text()