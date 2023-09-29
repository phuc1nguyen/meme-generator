"""A class that generates meme to a directory from given image."""

from .._const.Extension import PhotoExtension
import random
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont


class MemeGenerator:
    """A generator that generates memes."""

    _QUOTE_MAX_LENGTH = 50
    _AUTHOR_MAX_LENGTH = 20
    allowed_extensions = [enum.value for enum in PhotoExtension]

    def __init__(self, out_dir: str):
        """Create a new meme."""
        self.out_dir = out_dir

    def validator(self, text, author):
        """Check if quote body and author exceeds maximum number of characters."""
        if len(text) >= self._QUOTE_MAX_LENGTH:
            raise Exception(
                f"Quote body exceeds maximum {self._QUOTE_MAX_LENGTH} characters.")
        if len(author) >= self._AUTHOR_MAX_LENGTH:
            raise Exception(
                f"Author exceeds maxium {self._AUTHOR_MAX_LENGTH} characters.")

    def can_load(self, path: str) -> bool:
        """Check if the image can be loaded."""
        ext = path.split('.')[-1]
        return ext in self.allowed_extensions

    def make_meme(self, img_path, text, author, width=500) -> str:
        """Manipulate given image into meme then generate meme path."""
        if not self.can_load(img_path):
            raise Exception('Invalid image type')

        self.validator(text, author)

        with Image.open(img_path).convert('RGB') as img:
            max_width = width
            hw_ratio = img.size[1] / img.size[0]

            # resize image if too wide
            if img.width > max_width:
                img = img.resize(
                    (max_width, round(max_width * hw_ratio)), Image.NEAREST)
                print("Image is resized down to 500x500", img)

            # add quote to image
            if text and author:
                font = ImageFont.truetype(
                    './_data/fonts/Roboto-Bold.ttf', 16)

                randomVerticalPos = random.choice(
                    range(30, img.height - 30))
                quote1 = f"\"{text}\""
                quote1_position = (30, randomVerticalPos)
                quote2 = f"- {author}"
                quote2_position = (45, randomVerticalPos + 20)

                draw = ImageDraw.Draw(img)
                draw.text(quote1_position, quote1, font=font, fill='white')
                draw.text(quote2_position, quote2, font=font, fill='white')

        img_file_name = img_path.split('/')[-1]
        meme_name = f"{round(datetime.now().timestamp())}_{img_file_name}"
        meme_path = f"{self.out_dir}/{meme_name}"
        img.save(meme_path)

        return meme_path
