import csv
# https://pythonworld.ru/moduli/modul-csv.html

def reader_row(results):
    QR_BO1_BR = results[0]
    QR_BO2_list1 = results[1]
    QR_BO2_list2 = results[2]
    QR_DBO = results[3]
    code_region = results[4]
    code_subject = results[5]
    name_of_subject = results[6]
    data_of_exam = results[7]
    receiver = results[8]
    name_of_unit = results[9]
    Number_of_BO1 = results[10]
    Number_of_BO2_list1 = results[11]
    Number_of_BO2_list2 = results[12]
    Number_KIM = results[13]
    Number_DBO = results[14]
    Number_variant = results[15]
    Name_file_KIM = results[16]

    # print(f"QR БО1/БР = {QR_BO1_BR}")
    # print(f"QR БО2 лист1 = {QR_BO2_list1}")
    # print(f"QR ДБО/QR ДБО = пустой {QR_DBO}")
    # print(f"Код региона = {code_region}")
    # print(f"Код предмета = {code_subject}")
    # print(f"Название предмета = {name_of_subject}")
    # print(f"Дата экзамена = {data_of_exam}")
    # print(f"Получатель = {receiver}")
    # print(f"Имя комплекта = {name_of_unit}")
    # print(f"Номер БО1/БР = {Number_of_BO1}")
    # print(f"Номер БО2 лист1 = {Number_of_BO2_list1}")
    # print(f"Номер БО2 лист2 = {Number_of_BO2_list2}")
    # print(f"Номер КИМ = {Number_KIM}")
    # print(f"Номер ДБО/Номер ДБО пустой = {Number_DBO}")
    # print(f"Номер варианта = {Number_variant}")
    # print(f"Имя файла КИМ = {Name_file_KIM}")
    return(QR_BO1_BR)

# import csv
# with open('1.csv', 'r', newline='') as csvfile:
#      spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
#      for row in spamreader:
#          print(', '.join(row))

csv_file = open("1.csv")
csv_reader = csv.reader(csv_file, delimiter = ";")
csv_data = list(csv_reader)
# print (csv_data)

# Считывание данных из CSV файла
#print (f"{csv_data[0]}")
list_data = csv_data[1] # получаем доступ к первой строке
print (reader_row(list_data))

