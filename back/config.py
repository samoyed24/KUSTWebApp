from datetime import timedelta
class Config:
    tokenURL = 'token'
    PWD_SECRET_KEY = '32ea8d9c91203bea'
    EMAIL_SENDER = 'samoyed24@qq.com'
    EMAIL_PASSWORD = 'iobamagjjpgojjbg'
    # 邮箱验证码过期时间，初始10分钟
    EMAIL_VERIFICATION_EXPIRE_TIME = timedelta(minutes=10)
