"""Task publisher 
Date: 23/06/2025
Author: Juan Manuel González Tapia

This script let's the user both clean and tokenize the txt files found in a given directory.
It will ask the user for the working directories and the directories where the files are to be placed.
It will do so by publishing them as tasks to a RabbitMQ queue 

"""

import pika, sys, os

def process_workdir():
    print("Bienvenido, escriba el working directory o solamente \"madre\" para usar el directorio madre")
    workdir = input()
    # Process string to get the parent directory
    if workdir == 'madre':
        workdir = os.getcwd() 
        workdir = workdir.split('/')
        workdir = workdir[:-1]
        workdir = '/'.join(workdir)
        return workdir
    else:
        # Check if work dir actually exists
        if os.path.isdir(workdir):
            print('Work directory existe')
        else:
            print('Working directory no existe, intentelo de nuevo')
            workdir = process_workdir()
        return workdir

def process_filedir():
    print("Escriba el directorio dentro de workdir donde se encuentran los archivos a procesar")
    filedir = workdir + input()
    # Check if work dir actually exists
    if os.path.isdir(workdir + filedir):
        print('File directory existe')
    else:
        print('Working directory no existe, intentelo de nuevo')
        filedir = process_filedir
    return filedir

# Getting the necessary directories 
workdir = process_workdir()
filedir = process_filedir()

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