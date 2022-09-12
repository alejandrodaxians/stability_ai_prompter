import os

from config.properties import IMG_PATH, PROMPT_REGEX
from logic.image_download import Download

download = Download()


class Rename:
    def __init__(self) -> None:
        pass

    def rename_file(self):
        files_names = download.filter_regex(PROMPT_REGEX)
        counter = 1
        actual_name = str(counter) + ".jpg"
        for name in files_names:
            counter += 1
            os.rename(f"{IMG_PATH}{actual_name}", f"{IMG_PATH}{name}.jpg")
