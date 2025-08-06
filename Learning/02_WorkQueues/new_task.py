import pika, sys

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declaring the queue, we can do this as many times as we want 
channel.queue_declare(queue='task_queue', durable=True) # Making it durable means it will outlive a node reset

# Takes a command line argument or if none is given just 'Hello, World!'
message = ' '.join(sys.argv[1:]) or "Hello World!"

# The exchange is an empty string by which we connect to the queue, this is the method by which we publish it 
channel.basic_publish(exchange='',
                      routing_key='task_queue',
                      body=message,
                      properties=pika.BasicProperties(
                         delivery_mode = pika.DeliveryMode.Persistent
                      ))

print(f" [x] Sent {message}")

connection.close()