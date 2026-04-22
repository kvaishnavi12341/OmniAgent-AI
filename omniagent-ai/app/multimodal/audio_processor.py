import whisper

class AudioProcessor:
    def __init__(self):
        self.model = whisper.load_model("base")

    def process(self, path):
        result = self.model.transcribe(path)
        return result["text"]