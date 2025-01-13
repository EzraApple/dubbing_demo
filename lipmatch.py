import os
import subprocess

class LipMatcher:
    """
    A class to handle lip-syncing the original video with a new audio track using Wav2Lip.
    """

    def __init__(self, wav2lip_repo_path="Wav2Lip", checkpoint_path="checkpoints/wav2lip_gan.pth"):
        """
        Parameters:
        -----------
        wav2lip_repo_path : str
            Path to the local Wav2Lip repository (cloned from GitHub).
        checkpoint_path : str
            Path to the Wav2Lip pretrained model (.pth file).
        """
        self.wav2lip_repo_path = wav2lip_repo_path
        self.checkpoint_path = checkpoint_path

        if not os.path.exists(self.wav2lip_repo_path):
            raise FileNotFoundError(
                f"Wav2Lip repo not found: {self.wav2lip_repo_path}.\n"
                "Clone it via: git clone https://github.com/Rudrabha/Wav2Lip.git"
            )
        if not os.path.exists(self.checkpoint_path):
            raise FileNotFoundError(
                f"Wav2Lip checkpoint not found: {self.checkpoint_path}.\n"
                "Download it from: https://github.com/Rudrabha/Wav2Lip#checkpoints"
            )
        self.inference_script = os.path.join(self.wav2lip_repo_path, "inference.py")

    def match_lips(
        self,
        original_video_path: str,
        new_audio_path: str,
        output_video_path: str,
        pads: tuple[int, int, int, int] = None,
        no_smoothing: bool = False,
        # mps: bool = False  # If you want to experiment with MPS, uncomment and handle below
    ) -> str:
        """
        Lip-sync the original video with the new audio using Wav2Lip.

        Parameters
        ----------
        original_video_path : str
            Path to the original video containing the speaker's face.
        new_audio_path : str
            Path to the new audio track (e.g., cloned TTS output).
        output_video_path : str
            Where to save the lip-synced output video.
        pads : (top, bottom, left, right), optional
            Pixel padding around the face.
        no_smoothing : bool, optional
            Whether to disable smoothing in Wav2Lip (i.e., --nosmooth).

        Returns
        -------
        str
            The path to the generated lip-synced video.
        """

        if not os.path.exists(original_video_path):
            raise FileNotFoundError(f"Original video not found: {original_video_path}")
        if not os.path.exists(new_audio_path):
            raise FileNotFoundError(f"New audio file not found: {new_audio_path}")

        command = [
            "python", self.inference_script,
            "--checkpoint_path", self.checkpoint_path,
            "--face", original_video_path,
            "--audio", new_audio_path,
            "--outfile", output_video_path,
        ]

        # If you want to use padding
        if pads is not None and len(pads) == 4:
            command += [
                "--pads",
                str(pads[0]), str(pads[1]),
                str(pads[2]), str(pads[3])
            ]

        # If you want to disable smoothing
        if no_smoothing:
            command.append("--nosmooth")

        print("Running Wav2Lip command:")
        print(" ".join(command))

        subprocess.run(command, check=True)

        if not os.path.exists(output_video_path):
            raise RuntimeError("Lip-synced video was not generated. Check Wav2Lip logs.")

        print(f"Lip-synced video saved to: {output_video_path}")
        return output_video_path
