import requests
import re

# from config.properties import PROMPT_REGEX, URL_REGEX

PROMPT_REGEX = "(?<=Prompt: )(.*?)(?=\\v)"

URL_REGEX = "(?<=')(.*?)(?=')"


class Download:
    def read_log_file():
        with open('./predictions.log', 'r') as log_file:
            file_content = log_file.read()
            return file_content

    def filter_regex(regex: str):
        file_content = Download.read_log_file()
        filelines = file_content.splitlines()
        filtered_list = []
        for line in filelines:
            regex_match = re.search(regex, line)
            if regex_match:
                match_str = regex_match.group(0)
                filtered_list.append(match_str)
        return filtered_list

    def get_file_name():
        names_list = Download.filter_regex(PROMPT_REGEX)
        for name in names_list:
            print(name)

    def download_imgs():
        urls_list = Download.filter_regex(URL_REGEX)
        counter = 0
        for url in urls_list:
            img_data = requests.get(url).content
            counter += 1
            with open(f"./images/{counter}.jpg", 'wb') as handler:
                handler.write(img_data)


if __name__ == "__main__":
    Download.read_log_file()
    Download.filter_regex(URL_REGEX)
    Download.download_imgs()

