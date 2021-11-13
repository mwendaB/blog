import os
import cloudinary
class Config:

    SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://moringaschool:mwendaB@localhost/blog'

    UPLOADED_PHOTOS_DEST ='app/static/photos'

    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SUBJECT_PREFIX = 'MWENDA Blog!'
    SENDER_EMAIL = 'brianmwenda255@gmail.com'
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True

        
