import requests
import re
import json
import datetime

surname=input("Фамилия:")
name=input("Имя:")
patronym=input("Отчество:")

monday=input("Понедельник той недели, расписание которой надо посмотреть (в формате гггг.мм.дд.):").split('.')
mondaydate = datetime.date(int(monday[0]), int(monday[1]), int(monday[2])) #приводим дату понедельника в формат datetime
sundaydate = mondaydate+datetime.timedelta(days=6) #Отсчитываем от понедельника дату следующего воскресенья

ruz1 = requests.get("https://ruz.hse.ru/api/search?term="+surname+"%20"+name+"%20"+patronym+"&type=person").content
personid = json.loads(ruz1)[0].get('id') #Узнаём id нужного нам препода
#Скачиваем информацию о парах препода на нужной нам неделе
ruz2 = requests.get("https://ruz.hse.ru/api/schedule/person/"+personid+"?start="+monday[0]+"."+monday[1]+"."+monday[2]+"&finish="+str(sundaydate.year)+"."+str(sundaydate.month)+"."+str(sundaydate.day)+"&lng=1").content

massive = (json.loads(ruz2)) #Интерпретируем строку как питонный объект. Это список словарей, каждый из которых соответствует одной паре.
#Выбираем из этой информации только то, что может заинтересовать пользователя РУЗа
for i in range(len(massive)):
	print ("Дата:", massive[i].get('date'))
	print("День недели:", massive[i].get('dayOfWeekString'))
	print("Начало пары:", massive[i].get('beginLesson'))
	print("Конец пары:", massive[i].get('endLesson'))
	print("Пара №", massive[i].get('lessonNumberStart'))
	print("Здание:", massive[i].get('building'))
	print("Аудитория:", massive[i].get('auditorium'))
	print("Препод:", massive[i].get('lecturer'))
	print("Тип пары:", massive[i].get('kindOfWork'))
	print("Предмет:", massive[i].get('discipline'))
	print("Студенты:", massive[i].get('group'))
	print("\n") #Отделяем пустой строкой одну пару от другой
	
	

	

