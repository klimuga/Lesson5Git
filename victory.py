import random

def Victorina():
    birthdays = {'11': '01.01.1991', '12': '02.02.1992', '13': '03.03.1993', '14': '04.04.1994', '15': '05.05.1995'
        , '16': '06.06.1996', '17': '07.07.1997', '18': '08.08.1998', '19': '09.09.1999', '10': '00.00.1990'}

    RandomNames = random.sample(birthdays.keys(), 2)


    print(RandomNames)
    #print(birthdays.get('11'))
    Dates = []
    CorrectAnswers = 0
    InCorrectAnswers=0
    for i in range(len(RandomNames)):
    #    print(RandomNames[i])
        Date = input('введите дату рождения персонажа '+ RandomNames[i]+': ')
    #    Dates.append(Date)
        print('Верный ответ: ', birthdays.get(RandomNames[i]))
        if Date == birthdays.get(RandomNames[i]):
            print('Вы дали верный ответ.')
            CorrectAnswers+=1
        else:
            print('Ваш ответ не верен.')
            DaysList = ['первое', "второе", "третье", "четвертое","пятое", "шестое", "седьмое", "восьмое", "девятое", "десятое",
                        "одиннадцатое", "двенадцатое", "тринадцатое", "четырнадцатое", "пятнадцатое", "шестнадцатое", "семнадцатое",
                        "восемнадцатое", "девятнадцатое", "двадцатое", "двадцать первое", "двадцать второе", "двадцать третье",
                        "двадцать четвертое","двадцать пятое", "двадцать шестое", "двадцать седьмое", "двадцать восьмое",
                        "двадцать девятое","тридцатое", "тридцать первое"]
            MonthsList = ["январь", "февраль", "март", "апрель", "май", "июнь", "июль", "август", "сентябрь", "октябрь", "ноябрь", "декабрь"]
            DateAsNumbers=birthdays.get(RandomNames[i]).split(".")
    #        print(DateAsNumbers)
            print("Верный ответ: ", DaysList[int(DateAsNumbers[0])-1], MonthsList[int(DateAsNumbers[1])-1], DateAsNumbers[2])
            InCorrectAnswers+=1

    print("Верных ответов: ", CorrectAnswers, ". Неверных ответов: ", InCorrectAnswers, ". Возрващайтесь еще :)")
    return