import requests as _requests
from back.utils import query
from time import sleep


class Config:
    MAX_RETRIES = 3


class Student:
    def __init__(self, username: str, password: str) -> None:
        self.username = username
        self.password = query.RSA(password)
        self.login_status = False
        self.session = _requests.Session()
        self.login()
        self.result = None

    def login(self) -> None:
        self.login_status, self.session = query.login(
            self.username, self.password, self.session
        )
        if not self.login_status:
            raise ValueError(f"Login Failed")

    def get_grade(self) -> None:
        retries = 0
        try:
            self.session, self.result = query.get_grade(self.session)
        except AttributeError:
            if retries < Config.MAX_RETRIES:
                sleep(20)
                retries += 1
                self.session, self.result = query.get_grade(self.session)
            else:
                raise ConnectionRefusedError('Server too busy')


if __name__ == '__main__':
    s = Student('202210114104', '123456789qqq')
    s.get_grade()
