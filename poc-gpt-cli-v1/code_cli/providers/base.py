class BaseProvider:
    def __init__(self, config):
        self.config = config

    def chat(self, messages):
        raise NotImplementedError
