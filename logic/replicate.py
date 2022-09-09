import replicate
import logging

from config.properties import REPLICATE_API_TOKEN


class StabilityAI:
    def __init__(self):
        self.client = replicate.Client(api_token=REPLICATE_API_TOKEN)
        self.model = self.client.models.get("stability-ai/stable-diffusion")

    def get_prediction_url(self):
        print("Write the prompt for your image:")
        prompt = input()
        logging.info(f'Prompt: "{prompt}"')
        return self.model.predict(prompt=prompt)

    def log_output_url(self):
        output = StabilityAI.get_prediction_url(self)
        logging.info(f"Image URL: {output}")
        logging.info("---")
