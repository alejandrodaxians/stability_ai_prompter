from typing import Any, Iterator
import replicate
import logging

from config.properties_token import REPLICATE_API_TOKEN


class StabilityAI:
    def __init__(self):
        self.client = replicate.Client(api_token=REPLICATE_API_TOKEN)
        self.model = self.client.models.get("stability-ai/stable-diffusion")

    def get_prediction_url(self) -> Any | Iterator:
        """
        Takes the user's input to give a prompt to the prediction model.

        **params**: None

        **returns**: The raw image url returned by the prediction model after passing
        it the prompt.
        """
        print("Write the prompt for your image:")
        prompt = input()
        logging.info(f'Prompt: "{prompt}"')
        return self.model.predict(prompt=prompt)

    def log_output_url(self) -> None:
        """
        Logs the the raw url object returned by get_prediction_url().

        **params**: None

        **returns**: None
        """
        output = self.get_prediction_url(self)
        logging.info(f"Image URL: {output}")
        logging.info("---")
