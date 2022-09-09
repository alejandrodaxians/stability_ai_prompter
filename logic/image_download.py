import requests
import re

# from config.properties import PROMPT_REGEX, URL_REGEX

PROMPT_REGEX = "(?<=\")(.*?)(?=\")"

URL_REGEX = "(?<=')(.*?)(?=')"


class Download:
    def __init__(self) -> None:
        pass

    def read_log_file(self):
        with open('./predictions.log', 'r') as log_file:
            file_content = log_file.read()
            return file_content

    def filter_regex(self, regex: str):
        file_content = self.read_log_file()
        filelines = file_content.splitlines()
        filtered_list = []
        for line in filelines:
            regex_match = re.search(regex, line)
            if regex_match:
                match_str = regex_match.group(0)
                filtered_list.append(match_str)
        return filtered_list

    def download_imgs(self):
        urls_list = self.filter_regex(URL_REGEX)
        # names_list = self.filter_regex(PROMPT_REGEX)
        for url in urls_list:
            img_data = requests.get(url).content
            with open("./images/image.jpg", 'wb') as handler:
                handler.write(img_data)


if __name__ == "__main__":
    Download.download_imgs()
