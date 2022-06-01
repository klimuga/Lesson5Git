import shutil
import use_functions
import victory
import sys
import os



def Invitation():
    print("\nМеню:\n\n"
      "1  создать папку\n"
      "2  удалить (файл/папку)\n"
    "3  копировать (файл/папку)\n"
    "4  просмотр содержимого рабочей директории\n"
    "5  посмотреть только папки\n"
    "6  посмотреть только файлы\n"
    "7  просмотр информации об операционной системе\n"
    "8  создатель программы\n"
    "9  играть в викторину\n"
    "10 мой банковский счет\n"
    "11 смена рабочей директории (*необязательный пункт)\n"
    "12 выход.")
    SelectedAction = input("Введите ваш выбор: ")
    if SelectedAction.isdigit():
        SelectedAction = int(SelectedAction)
    else:
        print("ОШИБКА. Введите число, другие вводы недопустимы.")
        SelectedAction = 0
    return SelectedAction

SelectedAction = Invitation()

def ActionMkDir(): # 1 создать папку
    CreateDirName = input("Как назвать создаваемую папку? ")
    if not os.path.exists(CreateDirName):
        os.mkdir(CreateDirName)
        print("УРА. папка {} успешно создана.".format(CreateDirName))
    else:
        print("ОШИБКА. папка {} уже существует. Оставляю как есть.".format(CreateDirName))

def ActionRmFileDir(): # 2 удалить (файл/папку)
    RemoveDirName = input("Какую папку удалить? ")
    if os.path.exists(RemoveDirName):
        os.rmdir(RemoveDirName)
        print("УРА. папка {} успешно удалена.".format(RemoveDirName))
    else:
        print("ОШИБКА. папка {} не существует. Ничего не делаю.".format(RemoveDirName))

def ActionCopyFileDir(): # 3 копировать (файл/папку)
    CopyDirFileName = input("Какой файл или папку копировать? ")
    CopyDirFileNameDestination = input("Как назвать файл или папку? ")
    if os.path.exists(CopyDirFileNameDestination):
        print("ОШИБКА. папка или файл {} уже существует.".format(CopyDirFileNameDestination))
    elif not os.path.exists(CopyDirFileName):
        print("ОШИБКА. папка {} не существует. Ничего не делаю.".format(CopyDirFileName))
    else:
        if os.path.isfile(CopyDirFileName):
            shutil.copy(CopyDirFileName, CopyDirFileNameDestination)
        else:
            shutil.copytree(CopyDirFileName, CopyDirFileNameDestination)
        print("УРА. Скопировал {} в {}".format(CopyDirFileName, CopyDirFileNameDestination))

def ActionLsDir(key=""): # 4 просмотр содержимого рабочей директории
    """
    :param key: "" - everything, "-d" - only dirs, no subdirs, "-f" - only files, no subdirs
    :return:
    """
    if key == "":
        print("Содержимое текущей директории: ")
        for x in os.listdir():
            print(x)
        print("УРА. Удалось показать всё содержимое директории!!! ВАУ!!!")
    elif key == "-d":
        onlydirs = [f for f in os.listdir() if os.path.isdir(f)]
        print("Содержимое текущей директории (только директории): ")
        for x in onlydirs:
            print(x)
        print("УРА. Удалось показать все директории!!! ВАУ!!!")
    elif key == "-f":
        onlyfiles = [f for f in os.listdir() if os.path.isfile(f)]
        print("Содержимое текущей директории (только файлы): ")
        for x in onlyfiles:
            print(x)
        print("УРА. Удалось показать все файлы из директории!!! ВАУ!!!")
    else:
        print("ОШИБКА, функции передан неверный ключ.")

def ActionChDir():
    print("текущая директория: os.getcwd()={}".format(os.getcwd()))
    NewDir = input("Введите новую директорию: ")
    if NewDir.find("\\"):
        print("found \\")
        os.chdir(NewDir)
    else:
        os.chdir(os.getcwd() + "\\" + NewDir)
    print("текущая директория: os.getcwd()={}".format(os.getcwd()))

while SelectedAction != 12:
    if SelectedAction == 1: # создать папку
        ActionMkDir()
    elif SelectedAction == 2: # удалить (файл/папку)
        ActionRmFileDir()
    elif SelectedAction == 3: # копировать (файл/папку)
        ActionCopyFileDir()
    elif SelectedAction == 4: # просмотр содержимого рабочей директории
        ActionLsDir()
    elif SelectedAction == 5: # посмотреть только папки
        ActionLsDir("-d")
    elif SelectedAction == 6: # посмотреть только файлы
        ActionLsDir("-f")
    elif SelectedAction == 7: # просмотр информации об операционной системе
        print("sys.version_info: ", sys.version_info)
    elif SelectedAction == 8: # создатель программы
        print("Программу сию написал Гэндальф Белый, о мой юный подаван.")
    elif SelectedAction == 9: # играть в викторину
        victory.Victorina()
    elif SelectedAction == 10: # мой банковский счет
        use_functions.AccountManagement()
    elif SelectedAction == 11: # смена рабочей директории (*необязательный пункт)
        ActionChDir()
    elif SelectedAction == 12: # выход
        break
    else:
        print("Ошибка, некорректный ввод.")
    SelectedAction = Invitation()
