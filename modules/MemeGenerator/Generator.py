from .._const.Extension import PhotoExtension
import random
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont


class MemeGenerator:
    """A generator that generates memes."""
    allowed_extensions = [enum.value for enum in PhotoExtension]

    def __init__(self, out_dir: str):
        """Create a new meme."""
        self.out_dir = out_dir

    def can_load(self, path: str) -> bool:
        """Check if the image can be loaded."""
        ext = path.split('.')[-1]

        return ext in self.allowed_extensions

    def make_meme(self, img_path, text, author, width=500) -> str:
        """Manipulate given image into meme then generate meme path."""
        if not self.can_load(img_path):
            raise Exception('Invalid image type')

        if type(img_path) != str:
            raise Exception('Invalid image path')

        with Image.open(img_path) as img:
            max_width = width
            hw_ratio = float(img.size[1]) / float(img.size[0])

            # resize image if too wide
            if img.width > max_width:
                img = img.resize(
                    (max_width, max_width * hw_ratio), Image.NEAREST)
                print("Image is resized down to 500x500", img)

            # add quote to image
            if text and author:
                font = ImageFont.truetype('./_data/fonts/Roboto-Bold.ttf', 16)

                randomVerticalPos = random.choice(range(30, img.height - 30))
                quote1 = f"\"{text}\""
                quote1_position = (30, randomVerticalPos)
                quote2 = f"- {author}"
                quote2_position = (45, randomVerticalPos + 20)

                draw = ImageDraw.Draw(img)
                draw.text(quote1_position, quote1, font=font, fill='white')
                draw.text(quote2_position, quote2, font=font, fill='white')

        img_name = img_path.split('/')[-1]
        meme_name = f"{round(datetime.now().timestamp())}_{img_name}"
        meme_path = f"{self.out_dir}/{meme_name}"
        img.save(meme_path)

        return meme_path
