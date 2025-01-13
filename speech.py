import os
from TTS.api import TTS

class Speaker:
    """
    A class that uses Coqui TTS to generate speech in a cloned voice.
    """

    def __init__(self,
                 model_name: str = "tts_models/multilingual/multi-dataset/your_tts",
                 language_code: str = "es"):
        """
        Initialize the Speaker.

        Parameters:
        -----------
        model_name : str
            The name of the Coqui TTS model to load.
            "tts_models/multilingual/multi-dataset/your_tts" supports voice cloning
            for multiple languages.
        language_code : str
            The language code in which you plan to generate speech (e.g., "es" for Spanish).
        """
        print(f"Loading TTS model: {model_name}")
        self.model_name = model_name
        self.language_code = language_code
        self.tts = TTS(model_name=self.model_name)
        print("TTS model loaded successfully.")

    def generate_speech(self,
                        text: str,
                        speaker_wav: str,
                        output_path: str = "output.wav") -> str:
        """
        Generate speech (in the chosen language) using the provided speaker's WAV sample.

        Parameters:
        -----------
        text : str
            The text to be converted to speech.
        speaker_wav : str
            Path to the WAV file that contains the original speaker's voice
            for cloning (e.g., extracted from demo_video.mov).
        output_path : str
            Where to save the generated WAV file.

        Returns:
        --------
        str
            The file path of the generated WAV audio.
        """
        print(f"Generating speech with voice cloned from: {speaker_wav}")
        self.tts.tts_to_file(
            text=text,
            speaker_wav=speaker_wav,    # This is crucial for speaker adaptation
            language=self.language_code,
            file_path=output_path
        )
        return output_path
