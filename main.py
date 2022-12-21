from PIL import Image
import pathlib
from pathlib import Path
# пути https://webtort.ru/%D0%BA%D0%B0%D0%BA-%D0%B7%D0%B0%D0%B4%D0%B0%D1%82%D1%8C-%D0%BF%D1%83%D1%82%D1%8C-%D0%BA-%D1%84%D0%B0%D0%B9%D0%BB%D1%83-%D0%B2-python/



image = Image.open('oge.TIFF')
# image.show()
im1 = Image.open('oge.TIFF')
im2 = Image.open('qr.png')
 
im1.paste(im2)
im1.save('result_blank.jpg', quality=95)
 
im1.close()
im2.close()