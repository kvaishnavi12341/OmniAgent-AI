from transformers import pipeline

class ImageProcessor:
    def __init__(self):
        self.captioner = pipeline("image-to-text")

    def process(self, image_path):
        result = self.captioner(image_path)
        return result[0]["generated_text"]