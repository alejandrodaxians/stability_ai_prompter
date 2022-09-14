from typing import List
import requests
import re

from config.properties import URL_REGEX
from logic.replicate import StabilityAI

stability = StabilityAI()


class Download:
    def __init__(self) -> None:
        pass

    def filter_url(self) -> List:
        """
        Reads the log file returned by read_log_file()
        and filters it according to a regex.

        **params**:
        regex: A regular expression used to match the log file's content.

        **returns**: A list with each match from the regex as each indexed value.
        """
        url = str(stability.get_output_url())
        regex_match = re.search(URL_REGEX, url)
        return regex_match.group(0)

    def download_img(self) -> None:
        """
        Downloads every image hosted on the valid urls that it
        finds inside the filtered list returned by filter_regex().

        **params**: None

        **returns**: None.
        """
        url = self.filter_url()
        prompt_name = stability.prompt
        img_name = f"./images/{prompt_name}.jpg"
        img_data = requests.get(url).content
        with open(img_name, 'wb') as handler:
            handler.write(img_data)
