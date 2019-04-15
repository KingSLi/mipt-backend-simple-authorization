#!/usr/bin/env python
import pika
import traceback, sys

from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import smtplib

conn_params = pika.ConnectionParameters('rabbit', 5672)
connection = pika.BlockingConnection(conn_params)
channel = connection.channel()

channel.queue_declare(queue='first-queue', durable=True)

print("Waiting for messages. To exit press CTRL+C")

def callback(ch, method, properties, body):
    user_email, url_to_confirm = body.split(' ')
    msg = MIMEMultipart()

    sender = 'fantasticalbackenders@yandex.ru'
    password = 'press_F_to_pass_backend'

    msg['Subject'] = "Confirm your email"
    msg['From'] = sender
    msg['To'] = user_email
    
    msg_text = MIMEText('Click for confirm your email: %s' % url_to_confirm, 'plain')
    msg.attach(msg_text)

    try:
        server = smtplib.SMTP('smtp.yandex.ru', 587)
        server.ehlo()
        server.starttls()

        server.login(sender, password)

        server.sendmail(sender, user_email, msg.as_string())

        server.quit()
        print("Successfully sent email to %s" % user_email)
    
    except Exception as err:
        print("Error: unable to send email: %s" % err)

channel.basic_consume('first-queue', callback)

try:
    channel.start_consuming()
except KeyboardInterrupt:
    channel.stop_consuming()
except Exception:
    channel.stop_consuming()
    traceback.print_exc(file=sys.stdout)
