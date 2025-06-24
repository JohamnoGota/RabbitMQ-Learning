import os
import subprocess

workdir = "/Users/juanmagonzalez/VsCode/RabbitLearning/Tutorials"
file = "Raw_files/raw1.txt"
outdir = "01_out_clean"
command = ["/Users/juanmagonzalez/VsCode/RabbitLearning/Tutorials/Bash_Scripts/01_clean.sh", 
            workdir, file, outdir]

subprocess.run(["/Users/juanmagonzalez/VsCode/RabbitLearning/Tutorials/Bash_Scripts/01_clean.sh", 
                "/Users/juanmagonzalez/VsCode/RabbitLearning/Tutorials", "Raw_files/raw1.txt", "01_clean"], text=True, shell=True)

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