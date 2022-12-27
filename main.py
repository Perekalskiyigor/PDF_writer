from PIL import Image
import pathlib
from pathlib import Path
from qr_generator import QR
from insert_image import Insert_Image
# пути https://webtort.ru/%D0%BA%D0%B0%D0%BA-%D0%B7%D0%B0%D0%B4%D0%B0%D1%82%D1%8C-%D0%BF%D1%83%D1%82%D1%8C-%D0%BA-%D1%84%D0%B0%D0%B9%D0%BB%D1%83-%D0%B2-python/

# Создаем Qr
qrimage=QR("1.csv","image_test.png")
qrimage.get_qr1()

# Вставляем QR в нужное изображение
insert_image = Insert_Image('oge.TIFF', "image_test.png")
insert_image.insert_qr()

