# transcribe.py

import whisper


class Transcriber:
    """
    A class that wraps the Whisper model to handle transcription of audio files.
    """

    def __init__(self, model_name: str = "base", device: str = "cpu"):
        """
        Initialize the Transcriber.

        Parameters:
        -----------
        model_name : str
            Name of the Whisper model to load.
            Options typically include: "tiny", "base", "small", "medium", "large".
        device : str
            PyTorch device to run the model on.
            Set to "cuda" if you have a GPU and want faster inference.
        """
        self.model_name = model_name
        self.device = device
        # Load the whisper model
        self.model = whisper.load_model(model_name, device=device)

    def transcribe_audio(self, audio_path: str) -> dict:
        """
        Transcribe an audio file and return the results.

        Parameters:
        -----------
        audio_path : str
            Path to the audio file (e.g., WAV, MP3, etc.) to transcribe.

        Returns:
        --------
        result : dict
            A dictionary containing transcription data:
              - 'text' for the transcribed text.
              - 'segments' for the list of segments with timestamps and text.
              - 'language' for the detected language (if the model supports detection).
        """
        result = self.model.transcribe(audio_path, verbose=False)
        return result

    def display_full_text(self, result: dict):
        """
        Print the full transcribed text from the result.

        Parameters:
        -----------
        result : dict
            The dictionary containing transcription data.
        """
        print("\n--- Transcribed Text ---")
        print(result.get("text", ""))

    def display_segmented_text(self, result: dict):
        """
        Print transcription segments with their start and end times.

        Parameters:
        -----------
        result : dict
            The dictionary containing transcription data.
        """
        print("\n--- Segmented Transcription ---")
        segments = result.get("segments", [])
        for seg in segments:
            start = seg["start"]
            end = seg["end"]
            text = seg["text"].strip()
            print(f"[{start:.2f} --> {end:.2f}]: {text}")
