from typing import Union, Annotated
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from back.config import Config as GlobalConfig
from back.utils.email.templates.EmailBaseTemplate import EmailBaseTemplate


class Email:
    def __init__(
            self,
            receiver: str,
            subject: Union[str, None] = None,
            body: Union[str, None] = None,
            sender: str = GlobalConfig.EMAIL_SENDER,
            send_password: str = GlobalConfig.EMAIL_PASSWORD,
    ):
        self.sender = sender
        self.receiver = receiver
        self.body = body
        self.subject = subject
        self.send_password = send_password

    def use_template(self, template: EmailBaseTemplate):
        self.subject = template.subject
        self.body = template.body

    def send(self):
        con = smtplib.SMTP_SSL('smtp.qq.com', 465)
        con.login(self.sender, self.send_password)
        print(con)
        msg = MIMEText(self.body, 'plain', 'utf-8')
        subject = Header(self.subject, 'utf-8').encode()
        msg['Subject'] = subject
        msg['From'] = f'{self.sender} <{self.sender}>'
        msg['To'] = f'{self.receiver}'
        con.sendmail(self.sender, self.receiver, msg.as_string())
        con.quit()


if __name__ == '__main__':
    from back.utils.email.templates.register import Register
    r = Register()
    email = Email(receiver="samoyed24@qq.com")
    email.use_template(template=r)
    email.send()

