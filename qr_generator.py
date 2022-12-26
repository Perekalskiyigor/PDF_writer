import qrcode
import csv_parser
# пример данных
data = "csv_parser.reader_row"
data = csv_parser.reader_row
print(f"QR БО1/БР = {data}")

# имя конечного файла
filename = "qr.png"
# генерируем qr-код
img = qrcode.make(data)
# сохраняем img в файл
img.save(filename)