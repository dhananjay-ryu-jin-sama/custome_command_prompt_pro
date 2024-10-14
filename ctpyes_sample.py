import subprocess

# Start a process
process = subprocess.Popen(['DATE'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Get the output and errors
stdout, stderr = process.communicate()

print(stdout.decode())
if stderr:
    print(stderr.decode())