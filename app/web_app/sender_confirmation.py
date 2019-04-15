import pika


def send_confirmation(email, url):
    connection = pika.BlockingConnection(pika.ConnectionParameters('rabbit', 5672))
    channel = connection.channel()
    channel.queue_declare(queue='first-queue', durable=True)
    channel.basic_publish(exchange='',
                          routing_key='first-queue',
                          body=(email + ' ' + url),
                          properties=pika.BasicProperties(delivery_mode = 2))

    print("Requset  has been sent from: " + email)
