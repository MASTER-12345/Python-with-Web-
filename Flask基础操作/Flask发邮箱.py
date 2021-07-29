from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.qq.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = "xxxxxx@qq.com"
app.config['MAIL_PASSWORD'] = "oxdjfsuyvcwxxxx"         # 后几位被我用xxxx代替，非真实可用的
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)
with app.app_context():
    message = Message(subject='hello flask-mail', sender="xxxxxx@qq.com", recipients=['294405121@qq.com'], body='测试邮件')
    mail.send(message)
