from flask import Flask, request
from flask_mail import Mail, Message
import os
import dotenv

dotenv.load_dotenv(dotenv.find_dotenv())

app = Flask("FirstAPI")
mail = Mail(app)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = os.getenv("MAIL_USERNAME")
app.config['MAIL_PASSWORD'] = os.getenv("MAIL_PASSWORD")
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)


@app.route('/olamundo', methods=['GET'])
def olaMundo():
    return {"ola": "mundo"}


@app.route('/sendemail', methods=['POST'])
def sendEmail():
    body = request.get_json()

    msg = Message(
        'Hello',
        sender=os.getenv("MAIL_USERNAME"),
        recipients=[body["email"]]
    )
    msg.body = 'Hello Flask message sent from Flask Mail'
    mail.send(msg)

    return body['email']


app.run()
