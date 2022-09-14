from typing import Any, Iterator
import replicate
import logging

from config.properties_token import REPLICATE_API_TOKEN


class StabilityAI:
    def __init__(self):
        self.client = replicate.Client(api_token=REPLICATE_API_TOKEN)
        self.model = self.client.models.get("stability-ai/stable-diffusion")
        self.prompt = ''

    def get_prompt(self) -> str:
        """
        Takes the user input and returns it.

        **params**: None

        **returns**: String with the user's prompt.
        """
        print("Write the prompt for your image:")
        self.prompt = input()
        return self.prompt

    def get_prediction(self) -> Any | Iterator:
        """
        Takes the user's input to give a prompt to the prediction model.

        **params**: None

        **returns**: The raw object returned by the prediction model after passing
        it the prompt.
        """
        prompt = self.get_prompt()
        logging.info(f'Prompt: "{prompt}"')
        return self.model.predict(prompt=prompt)

    def get_output_url(self) -> None:
        """
        Logs the the raw url object returned by get_prediction_url().

        **params**: None

        **returns**: None
        """
        output = self.get_prediction()
        logging.info(f"Image URL: {output}")
        logging.info("---")
        return output
