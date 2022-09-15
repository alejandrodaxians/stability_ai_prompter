from config.logging_conf import config_logs
from logic.replicate import StabilityAI
from logic.image_download import Download


stability = StabilityAI()
download = Download()


if __name__ == "__main__":
    config_logs()
    download.download_img()
