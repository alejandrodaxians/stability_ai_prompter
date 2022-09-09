from config.logging_conf import config_logs
from logic.replicate import StabilityAI


stability = StabilityAI()


if __name__ == "__main__":
    config_logs()
    stability.log_output_url()
