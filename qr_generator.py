import qrcode
# пример данных
data = "https://pythonist.ru/"
# имя конечного файла
filename = "qr.png"
# генерируем qr-код
img = qrcode.make(data)
# сохраняем img в файл
img.save(filename)