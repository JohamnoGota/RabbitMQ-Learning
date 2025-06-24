import pika, sys, os, time

def main():
    # Connection to rabbitMQ
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Declaring the queue, we can do this as many times as we want so we do it everytime 
    channel.queue_declare(queue='task_queue', durable=True) # Making it durable means it will outlive a node reset
    
    # Callback function that processes the message in the queue
    def callback(ch, method, properties, body):
        print(f" [x] Received {body.decode()}")
        time.sleep(body.count(b'.'))
        print(" [x] Done")
        ch.basic_ack(delivery_tag = method.delivery_tag)

    # We initialize the consuming for the queue
    channel.basic_consume(queue='task_queue', on_message_callback=callback)

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
            