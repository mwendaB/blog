from flask_mail import Message, render_template
from . import mail 

def mail_message(subject,template,to,**kwargs):
      sender_email = 'brianmwendah12@gmail.com'
