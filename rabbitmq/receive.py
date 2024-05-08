import os
import sys

import pika

"""Receives messages from the queue and prints them in the screen"""


def main():
    # Make connection to broker
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Connect to server, declaring again in case receive.py gets executed before send.py
    channel.queue_declare(queue='hello')

    # Need to subscribe a callback function to a queue when receiving messages
    # Whenever we receive a message, this function is called by the Pika library
    def callback(ch, method, properties, body):
        print(f" [x] Received {body}")

    channel.basic_consume(queue='hello',
                          auto_ack=True,
                          on_message_callback=callback)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
