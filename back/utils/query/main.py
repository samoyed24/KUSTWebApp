import time
import pandas as pd
import requests
from bs4 import BeautifulSoup


def login(username: str, password: str, session: requests.Session) -> [bool, requests.Session]:
    s = session
    r = s.get(
        'https://cas.kmust.edu.cn/lyuapServer/login?service=http%3A%2F%2Fjwctsp.kmust.edu.cn%2Fintegration%2Fkcas-sso%2Flogin')
    r.encoding = 'utf8'
    soup1 = BeautifulSoup(r.text, 'html.parser')
    lt = soup1.find('input', {"name": "lt"}).attrs['value']
    execution = soup1.find('input', {"name": "execution"}).attrs['value']
    _eventId = soup1.find('input', {"name": "_eventId"}).attrs['value']
    data = {
        'username': username,
        'password': password,
        'captcha': '',
        'warn': True,
        'lt': lt,
        'execution': execution,
        '_eventId': _eventId
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
    }
    s.post(
        'https://cas.kmust.edu.cn/lyuapServer/login?service=http%3A%2F%2Fjwctsp.kmust.edu.cn%2Fintegration%2Fkcas-sso%2Flogin',
        data=data, headers=headers)
    s.get(
        'https://cas.kmust.edu.cn/lyuapServer/login?service=http%3A%2F%2Fjwctsp.kmust.edu.cn%2Fintegration%2Fkcas-sso%2Flogin',
        headers=headers)
    r = s.get('http://i.kust.edu.cn/')
    soup = BeautifulSoup(r.text, 'lxml')
    status = soup.head.title.text == "昆明理工大学师生信息服务平台"  # 判断是否成功登录
    return status, s


def get_grade(s: requests.Session) -> [requests.Session, pd.DataFrame]:
    r = s.get('http://jwctsp.kmust.edu.cn/integration/for-std/best/grade/sheet')
    r.encoding = 'utf-8'
    soup2 = BeautifulSoup(r.text, 'html.parser')
    studentid = soup2.find('form', {'target': 'student-grades'}).attrs['action'].split('/')[-1]
    r = s.get(f'http://jwctsp.kmust.edu.cn/integration/for-std/best/grade/sheet/info/{studentid}?semester=')

    soup3 = BeautifulSoup(r.text, 'html.parser')

    datadict = {
        '学期': [],
        '课程名称': [],
        '课程代码': [],
        '课程类别1': [],
        '课程类别2': [],
        '教学班代码': [],
        '成绩': [],
        '学分': [],
        '绩点': [],
        '学分绩点': [],
        '修读性质': [],
        '备注': []
    }

    gradeinfo = soup3.find_all('div', {'class': 'row'})
    for gradeblock in gradeinfo:
        sem = gradeblock.find_all('div', {'class': 'col-sm-12'})
        semname = sem[0].h3.text
        gradetb = sem[1]
        grades = gradetb.table.tbody.select('tr')
        for grade in grades:
            data = grade.select('td')
            datadict['学期'].append(semname)
            datadict['课程名称'].append(data[0].text.strip())
            datadict['课程代码'].append(data[1].text)
            datadict['课程类别1'].append(data[2].text)
            datadict['课程类别2'].append(data[3].text)
            datadict['教学班代码'].append(data[4].text)
            datadict['成绩'].append(data[5].text)
            datadict['学分'].append(data[6].text)
            datadict['绩点'].append(data[7].text)
            datadict['学分绩点'].append(data[8].text)
            datadict['修读性质'].append(data[9].text)
            datadict['备注'].append(data[10].text)
    df = pd.DataFrame(data=datadict)
    return s, df
