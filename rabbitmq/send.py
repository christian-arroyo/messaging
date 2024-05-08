import pika

# Make connection to broker
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Create a hello queue
channel.queue_declare(queue='hello')

# Send message through default exchange
channel.basic_publish(exchange ='',
                      routing_key='hello',
                      body='Hello World!')
print(" [x] Sent 'Hello World!'")
connection.close()
