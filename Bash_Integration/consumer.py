import pika
import subprocess, sys, os
"""


"""
def processOutdir(workdir, step):
    outdir = workdir + '/output/' + step
    if os.path.isdir(outdir):
        print('Outdir existe')
        return outdir
    else:
        try:
            os.makedirs(outdir, exist_ok=True)
            print(f'Creando {outdir}')
        except OSError as error:
            print(error)
        return outdir

def processMessage(message):
    dirs = message.split('#')
    workdir = dirs[0]
    filedir = dirs[1]
    file = filedir + '/' + dirs[2]
    print(f"File passed to script {file}")
    outdir = processOutdir(workdir, "01_cleaning")
    command = ["/Users/juanmagonzalez/VsCode/RabbitLearning/RabbitAutomation/Bash_Scripts/01_clean.sh", 
            workdir, file, outdir]
    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        print("Script ran successfully!")
        print("STDOUT:\n", result.stdout)
        if result.stderr:
            print("STDERR:\n", result.stderr)
    except subprocess.CalledProcessError as e:
        print("Script failed!")
        print("Return code:", e.returncode)
        print("STDOUT:\n", e.stdout)
        print("STDERR:\n", e.stderr)

    



def main():
    # Connection to rabbitMQ
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Declaring the queue, we can do this as many times as we want so we do it everytime 
    channel.queue_declare(queue='task_queue', durable=True) # Making it durable means it will outlive a node reset
    
    # Callback function that processes the message in the queue
    def callback(ch, method, properties, body):
        dirs = body.decode()
        print(f" [x] Received {dirs}")
        processMessage(dirs)
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
            