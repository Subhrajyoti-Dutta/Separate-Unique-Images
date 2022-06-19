import io
import string

from PIL import Image


class SheetImageLoader:
    _images = {}

    def __init__(self, sheet):
        sheet_images = sheet._images
        for image in sheet_images:
            row = image.anchor._from.row + 1
            col = string.ascii_uppercase[image.anchor._from.col]
            self._images[f'{col}{row}'] = io.BytesIO(image._data())

    def get(self, cell):
        if cell not in self._images:
            raise ValueError(f"Cell {cell} doesn't contain an image")
        else:
            image = self._images[cell]
            return Image.open(image)