# ------------------  HTTP: для парсингу сайтів ----------------------------
'''

Приклад
парсингу сайтів із збереженням інформації до файлів різного формату
df.to_csv("output.csv")
df.to_excel("output.xlsx")
df.to_json("output.json")

Package                      Version
---------------------------- -----------
pip                          23.1
requests                     2.28.2
bs4                          0.0.1
pandas                       1.5.3

'''

import requests
from bs4 import BeautifulSoup as bs
import pandas as pd


def Parsing_Site_work_ua (URL_TEMPLATE):
    '''
    site parsing python
    web scraping / site scraping python
    Data scraping - швидше очищення та підготовка даних
    https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_excel.html

    :param URL_TEMPLATE: URL Site work.ua
    :return: class 'dict'
    '''

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
    }
    '''
    Зміни в аргументі для методу get: headers=headers - МИ "відрекомендувались" звичайним браузером при зверненні до серверу.
    '''
    r = requests.get(URL_TEMPLATE, headers=headers)

    result_list = {'href': [], 'title': [], 'about': []}
    print(r.status_code)
    print(r.text)
    soup = bs(r.text, "html.parser")
    vacancies_names = soup.find_all('h2', class_="")
    vacancies_info = soup.find_all('p', class_='overflow')
    constant = 5 # для балансування даних
    i = 0
    for name in vacancies_names:
        i = i + 1
        if (i < (len(vacancies_names) - constant)):
            print(name.a['title'])
            result_list['title'].append(name.a['title'])
            print('https://www.work.ua' + name.a['href'])
            result_list['href'].append('https://www.work.ua' + name.a['href'])
    i = 0
    for info in vacancies_info:
        i = i + 1
        if (i < (len(vacancies_names) - constant)):
            print(info.text)
            result_list['about'].append(info.text)

    print(result_list['title'])
    print(result_list['href'])
    print(result_list['about'])

    print(type(result_list))

    return result_list




URL_TEMPLATE = "https://www.work.ua/jobs-data+scientist/?page=1"

df = pd.DataFrame(data=Parsing_Site_work_ua(URL_TEMPLATE))
df.to_csv("output.csv")
df.to_excel("output.xlsx")
df.to_json("output.json")