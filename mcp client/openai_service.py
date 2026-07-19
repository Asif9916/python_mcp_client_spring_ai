from openai import OpenAI


class OpenAIService:

    def __init__(self, api_key, model):
        self.client = OpenAI(api_key=api_key)
        self.model = model

    def chat(self, messages, tools):

        return self.client.responses.create(
            model=self.model,
            input=messages,
            tools=tools
        )