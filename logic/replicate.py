import replicate
import logging

from config.properties import REPLICATE_API_TOKEN

class StabilityAI:
    def set_client_with_token(self):
        return replicate.Client(api_token=REPLICATE_API_TOKEN)

    def set_stable_model(self):
        client = StabilityAI.set_client_with_token(self)
        return client.models.get("stability-ai/stable-diffusion")

    def get_prediction_url(self):
        model = StabilityAI.set_stable_model(self)
        print("Write the prompt for your image:")
        prompt = input()
        logging.info(f"Prompt: {prompt}")
        return model.predict(prompt=prompt)

    def log_output_url(self):
        output = StabilityAI.get_prediction_url(self)
        logging.info(f"Image URL: {output}")
        logging.info("---")
