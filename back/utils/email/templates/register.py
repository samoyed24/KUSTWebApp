from back.utils.email.templates.EmailBaseTemplate import EmailBaseTemplate
from back.utils import utils


class Register(EmailBaseTemplate):
    def __init__(self):
        super(Register, self)
        super().__init__()
        self.subject = "Register"
        self.body = "您的注册验证码为："
        self.get_valid_code()

    def get_valid_code(self):
        valid_code: str = utils.random_six_digits()
        self.body = self.body + valid_code


if __name__ == '__main__':
    r = Register()
    print(r.body)
