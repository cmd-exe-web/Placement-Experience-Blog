import os


class Config:
    SECRET_KEY = '4PZDOQ6KvU'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'akash@akash.com'
    MAIL_PASSWORD = 'password'
