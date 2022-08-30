import moviepy.editor as mp
import speech_recognition as sr
from textblob import TextBlob

def score(x):
    if x<0:
        return "NEGATIVE"
    elif x==0:
        return "NEUTRAL"
    else:
        return "POSITIVE"

def speechrecog(file):
    r = sr.Recognizer()
    audio = sr.AudioFile(file)
    with audio as source:
        r.adjust_for_ambient_noise(source)
        audio_file = r.record(source)
    result = r.recognize_google(audio_file)
    print(result)
    polarity = TextBlob(result).sentiment.polarity
    out_score = score(polarity)
    return result,out_score

def upload(file):
    if file.endswith("mp4"):
        clip = mp.VideoFileClip(file)
        filemp4convert = clip.audio.write_audiofile("D:\Mchine learning_integration\Arwin\Speech_recognition\media_out" + "\\" + "converted.wav")
        data_out = "D:\Mchine learning_integration\Arwin\Speech_recognition\media_out\converted.wav"
        return data_out
    elif file.endswith("wav"):
        # data_out = speechrecog(file)
        pass
        return file

