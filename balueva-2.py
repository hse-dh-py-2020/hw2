#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click
import requests

@click.command()
@click.argument('surname')
@click.argument('name')
@click.argument('patronymic')
def get_shedule(surname,name,patronymic):
    person = 'https://ruz.hse.ru/api/search?term='+surname+' '+name+' '+patronymic+'&type=person'
    r1 = requests.get(person)

    prepod_id = r1.json()[0]['id']
    shedule = 'https://ruz.hse.ru/api/schedule/person/' + prepod_id + '?start=2020.09.20&finish=2020.09.30&lng = 1'
    r2 = requests.get(shedule)
    s = r2.json()
    for i in range(len(s)):
        print(str(i + 1) + ') ' + s[i]['date'] + ' ' + s[i]['dayOfWeekString'] + ' ' + s[i]['discipline'])
        print(s[i]['beginLesson'] + ' - ' + s[i]['endLesson'])
        print(s[i]['building'] + ' ' + s[i]['auditorium'])
        print(s[i]['group'])
        print('\n')

if __name__ == '__main__':
    get_shedule()
