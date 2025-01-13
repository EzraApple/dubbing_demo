## Pipeline Overview


### 1. Audio Extraction
We use MoviePy to extract the audio track from the input video.
Key benefit: easily isolate the speaker’s voice as a .wav file for further processing.
### 2. Transcription
We use OpenAI Whisper to transcribe the extracted audio into text.
Whisper is known for high accuracy and multi-language support.
### 3. Translation
We rely on Argos Translate  to translate the transcribed text into a target language (e.g., English → Spanish).
Key feature: offline usage and straightforward integration via Python APIs.
### 4. Voice Cloning / TTS
We use Coqui TTS to clone the speaker’s voice and generate TTS in the new language.
This step involves computing a speaker embedding and then synthesizing speech with that cloned voice.
### 5. Lip Sync
The final step uses Wav2Lip to match the original speaker’s lip movements to the newly generated audio.
Result: a new video where the speaker appears to speak the translated dialogue with aligned lip movements.