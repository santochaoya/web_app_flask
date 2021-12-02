class Config:
    MAIL_SERVER = 'smtp.126.com'
    PORT = 465
    MAIL_USE_TLS = True
    MAIL_USERNAME = '<sender email here>'
    MAIL_PASSWORD = '<password here>'
    SECRET_KEY = '5791628bb0b13ce0c676dfde280ba245'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
