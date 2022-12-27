import qrcode
import csv_parser

class QR():
    def __init__(self, file_csv, qr_name):
        """Инициализирует атрибуты описания автомобиля."""
        self.file_csv = file_csv # Имя файла csv
        self.qr_name = qr_name # Имя сохраняемого файла с qr кодом

    def get_qr1(self):
        """Получает строку с кодом из файла csv"""
        Parser = csv_parser.Csv_parser(self.file_csv) # Получаем данные из csv
        data = Parser.reader_row() # Вызываем парсер метод
        img = qrcode.make(data) # Солздаем штрих код
        img.save(self.qr_name) # Сохраняем штрих код
    
 