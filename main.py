from config.logging_conf import config_logs
from logic.replicate import StabilityAI
from logic.image_download import Download
from logic.rename_image import Rename


stability = StabilityAI()
download = Download()
rename = Rename()


if __name__ == "__main__":
    config_logs()
    stability.log_output_url()
    download.download_imgs()
    rename.rename_file()
