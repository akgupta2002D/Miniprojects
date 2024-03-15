from pydub import AudioSegment
import speech_recognition as sr

# Convert MP3 to WAV


def convert_mp3_to_wav(mp3_file_path, wav_file_path):
    audio = AudioSegment.from_mp3(mp3_file_path)
    audio.export(wav_file_path, format="wav")

# Transcribe WAV file


def transcribe_wav(wav_file_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(wav_file_path) as source:
        audio_data = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio_data)
            print("Transcription: ", text)
        except sr.UnknownValueError:
            print("Audio unintelligible")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")


# File paths
mp3_file_path = 'C:\\Users\\ankit\\Desktop\\Current Projects\\Mini_Projects\\speech\\testfile.mp3'

wav_file_path = 'testfile.wav'

# Convert and transcribe
convert_mp3_to_wav(mp3_file_path, wav_file_path)
transcribe_wav(wav_file_path)
