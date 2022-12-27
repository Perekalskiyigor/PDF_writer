from PIL import Image
import pathlib
from pathlib import Path

class Insert_Image():
    def __init__(self, blank1, qr1):
        """Инициализирует атрибуты описания автомобиля."""
        self.blank1 = blank1
        self.qr1 = qr1
    
    def insert_qr (self):
        image = Image.open(self.blank1)
        im1 = Image.open(self.blank1)
        im2 = Image.open(self.qr1)
        im1.paste(im2)
        im1.save('result_blank.jpg', quality=95)
        im1.close()
        im2.close()

    def insert_bar (self):
        image = Image.open(self.blank1)
        im1 = Image.open(self.blank1)
        im2 = Image.open(self.qr1)
        im1.paste(im2)
        im1.save('result_blank2.jpg', quality=95)
        im1.close()
        im2.close()