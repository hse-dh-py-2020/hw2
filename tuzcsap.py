import requests

print('Введите ФИО преподавателя')
print('Фамилия:', end=' ')
last_name = input()
print('Имя:', end=' ')
first_name = input()
print('Отчество:', end=' ')
patronymic = input()

# Request json with data about lecturers by their names
res1 = requests.get(
    f'https://ruz.hse.ru/api/search?term={last_name}%20{first_name}%20{patronymic}&type=person')

# Make sure that request was successful (status code 200: OK)
assert(res1.status_code == 200)

# Get lecturers' id
id = int(res1.json()[0]['id'])

# Request lecturer's timetable given his id and hardcoded time interval
res2 = requests.get(
    f'https://ruz.hse.ru/api/schedule/person/{id}?start=2020.09.07&finish=2020.09.13&lng=1')

assert(res2.status_code == 200)

# print useful data from timetable json
timetable = res2.json()

if len(timetable) > 0:
    print('Расписание:\n')
    for entry in timetable:
        #print('Преподаватель', entry['lecturer'])
        print('Дата:', entry['date'])
        print('День недели:', entry['dayOfWeekString'])
        print('Предмет:', entry['discipline'])
        print('Группа:', entry['group'])
        print('с', entry['beginLesson'])
        print('до', entry['endLesson'])
        print('Корпус:', entry['building'])
        print('Аудитория:', entry['auditorium'])
        print('Вид занятия:', entry['kindOfWork'])
        print('\n')
else:
    print('В этом интервале времени пар не найдено')
