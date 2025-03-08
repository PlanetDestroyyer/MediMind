from gtts import gTTS
import io
import pygame

class TextToSpeech:
    def __init__(self, language='en'):
        self.language = language
        pygame.mixer.init()

    def speak(self, text):
        tts = gTTS(text=text, lang=self.language, slow=False)
        audio_stream = io.BytesIO()
        tts.write_to_fp(audio_stream)
        audio_stream.seek(0)
        
        pygame.mixer.music.load(audio_stream, 'mp3')
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            continue

# Example usage
tts = TextToSpeech()
tts.speak("Welcome, I am AI Doctor. How can I help you?")
