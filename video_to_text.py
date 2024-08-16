import ffmpeg
import speech_recognition as sr
def extract_audio_from_video(video_path, output_audio_path):
    """
    Extracts audio from a video file and saves it as a separate audio file.

    :param video_path: Path to the input video file.
    :param output_audio_path: Path to save the extracted audio file.
    """
    ffmpeg.input(video_path).output(output_audio_path).run()

def transcribe_audio_to_text(audio_path, language="en-US"):
    """
    Transcribes an audio file to text using Google Web Speech API.

    :param audio_path: Path to the input audio file.
    :param language: Language code for the transcription (default is English).
    :return: Transcribed text.
    """
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_path) as source:
        audio = recognizer.record(source)
    try:
        text = recognizer.recognize_google(audio, language=language)
        return text
    except sr.UnknownValueError:
        return "Google Web Speech API could not understand the audio."
    except sr.RequestError as e:
        return f"Could not request results from Google Web Speech API; {e}"

def save_text_to_file(text, file_path):
    """
    Saves the transcribed text to a file.

    :param text: The transcribed text.
    :param file_path: Path to the output text file.
    """
    with open(file_path, "w") as file:
        file.write(text)

def video_to_text_pipeline(video_path, audio_output_path, text_output_path, language="en-US"):
    """
    Complete pipeline to convert video to text by extracting audio, transcribing it, and saving the result.

    :param video_path: Path to the input video file.
    :param audio_output_path: Path to save the extracted audio file.
    :param text_output_path: Path to save the transcribed text.
    :param language: Language code for the transcription (default is English).
    """
    # Step 1: Extract audio from the video
    extract_audio_from_video(video_path, audio_output_path)

    # Step 2: Convert the audio to text
    transcription = transcribe_audio_to_text(audio_output_path, language)

    # Step 3: Save the transcription to a text file
    save_text_to_file(transcription, text_output_path)

# Step 4: Define Input and Output Paths
if __name__ == "__main__":
    video_file = 'input_video.mp4'       # Input video file
    audio_file = 'output_audio.wav'      # Extracted audio file
    text_file = 'transcription.txt'      # Output text file

    # Specify the language code for the video language
    # Example: 'es-ES' for Spanish, 'fr-FR' for French, etc.
    language_code = "en-US"  # Change this based on the language of the video

    # Run the complete pipeline
    video_to_text_pipeline(video_file, audio_file, text_file, language_code)