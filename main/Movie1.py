import speech_recognition as sr


def detect_movie_language(movie_audio_path):
    recognizer = sr.Recognizer()

    with sr.AudioFile(movie_audio_path) as source:
        audio = recognizer.record(source)  # Record the entire audio from the movie

    try:
        recognized_text = recognizer.recognize_google(audio, show_all=True)

        # Check for the detected language
        if 'language' in recognized_text:
            detected_language = recognized_text['language']
            return f"Detected language: {detected_language}"
        else:
            return "Language detection failed."
    except sr.UnknownValueError:
        return "Could not recognize any speech."


# Replace 'movie_audio_path' with the path to your movie's audio file
movie_language = detect_movie_language('C:/Workarea/File_Analyser/movie/1.mp4')
print(movie_language)