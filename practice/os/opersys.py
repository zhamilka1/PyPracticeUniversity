import os
from pdf2docx import Converter
from docx2pdf import convert
from PIL import Image

def showMenu():
    print(os.getcwd())
    print("0:Замена пути к рабочему каталогу")
    print("1:Изменить файл в формате PDF в DOCX")
    print("2:Изменить файл в формате в PDF")
    print("3:Ужать качество изображения")
    print("4:Удалить группу файлов по подстроке")
    print("5:Выход из программы")

def showFilesAndMakeChoise():
    files = os.listdir(os.getcwd())
    for i in range(0,len(files)):
        print(f"{i} : {files[i]}")
    choise = int(input("выберите файл"))
    return files[choise]
def main():
    while choise != 5:
        showMenu()
        choise = int(input("Введите номер"))
        if choise == 0:
            newdirname = input("Введите название директории")
            if (os.path.exists(newdirname)):
                if (os.path.isdir(newdirname)):
                    os.chdir(newdirname)
            print("вы перешли в директорию:" + newdirname)
        elif choise == 1:
            pdfFile = showFilesAndMakeChoise()
            wordFile = pdfFile.replace('.pdf', '.docx')
            cv = Converter(pdfFile)
            cv.convert(wordFile)
            cv.close()
        elif choise == 2:
            docxFile = showFilesAndMakeChoise()
            convert(docxFile)
        elif choise == 3:
            imagePath = showFilesAndMakeChoise()
            quality = int(input("Введите качество от 0 до 100%"))
            with Image.open(imagePath) as img:
                print(img.format, img.size)
                if img.mode != "RGB":
                    img = img.convert("RGB")
                img.save(imagePath, "JPEG", optimize=True, quality=quality)
        elif choise == 4:
            files = os.listdir(os.getcwd())
            searchType = int(input("Введите тип паттерна: 0-префикс 1-постфикс 2-подстрока 3-расширение"))
            if searchType == 0:
                substr = input('Введите префикс')
                for file in files:
                    if file.lower().startswith(substr.lower()):
                        path = f"{os.getcwd()}\{file}"
                        os.remove(path)
            elif searchType == 1:
                substr = input('Введите постфикс')
                for file in files:
                    if file.lower().endswith(substr.lower()):
                        path = f"{os.getcwd()}\{file}"
                        os.remove(path)
            elif searchType == 2:
                substr = input('Введите подстроку')
                for file in files:
                    if substr.lower() in file.lower():
                        path = f"{os.getcwd()}\{file}"
                        os.remove(path)
            elif searchType == 3:
                substr = input('Введите расширение')
                for file in files:
                    if ('.' + substr.lower()) in file.lower():
                        path = f"{os.getcwd()}\{file}"
                        os.remove(path)
        else:
            break
