import argostranslate.package
import argostranslate.translate
import os


class Translator:
    """
    A class that wraps Argos Translate for language translation.
    """

    def __init__(self, source_lang: str = "en", target_lang: str = "es"):
        """
        Initialize the Translator.

        Parameters:
        -----------
        source_lang : str
            The source language code (e.g., "en").
        target_lang : str
            The target language code (e.g., "es").
        """
        self.source_lang = source_lang
        self.target_lang = target_lang

        # (Optional) This step ensures that the relevant Argos packages are installed.
        # You could skip this if you've already installed the package manually.
        # For a proof-of-concept, it's convenient to do it here.
        self._install_language_package()

    def _install_language_package(self):
        """
        Install the Argos Translate package for the specified language pair,
        if it's not already installed.
        """
        # Update package index
        argostranslate.package.update_package_index()

        available_packages = argostranslate.package.get_available_packages()
        installed_languages = argostranslate.translate.get_installed_languages()

        # Check if the package for the specified language pair is already installed
        installed_codes = [(lang.code, lang) for lang in installed_languages]

        # If the language is already installed, skip reinstallation
        source_lang_installed = any(code == self.source_lang for code, _ in installed_codes)
        target_lang_installed = any(code == self.target_lang for code, _ in installed_codes)

        if source_lang_installed and target_lang_installed:
            return  # Both languages are available—no need to install.

        # Otherwise, find and install the package for our language pair
        for package in available_packages:
            if (package.from_code == self.source_lang and
                    package.to_code == self.target_lang):
                download_path = package.download()
                argostranslate.package.install_from_path(download_path)
                break

    def translate_text(self, text: str) -> str:
        """
        Translate text from source_lang to target_lang using Argos Translate.

        Parameters:
        -----------
        text : str
            The text to translate.

        Returns:
        --------
        str
            The translated text.
        """
        return argostranslate.translate.translate(
            text, self.source_lang, self.target_lang
        )
