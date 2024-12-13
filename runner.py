import paramiko
from sys import argv

# Colors to organize the output
GREEN = "\033[92m"
YELLOW = "\033[33m"
CYAN = "\033[36m"
RESET = "\033[0m"

args = argv[1:]


def is_ip(ip):
    parts = ip.split('.')
    if len(parts) != 4:
        return False
    else:
        for part in parts:
            if int(part) > 255 or int(part) < 0:
                return False
            else:
                return True


# Finding the hostname/ip of the machine when -i is used:
usage = f'Usage: python {argv[0]} -i <IP> -u "<user>" -p "<pass>" -s "script.txt"'


if '-i' in args:
    ip = args[args.index('-i') + 1]
    if is_ip(ip):
        hostname = ip
    else:
        print('Your IP is not formatted correctly.')
else:
    print(usage)


# Finding the username:

if '-u' not in args:
    print('Provide a username: -u "<username"')
else:
    username = args[args.index('-u') + 1]

if '-p' not in args:
    print('Provide a password: -p "<password>"')
else:
    password = args[args.index('-p') + 1]

# Finding the script:
if '-s' not in args:
    print('Provide the path of the script: -s "<path-to-script>"')
else:
    with open(args[args.index('-s') + 1]) as file:
        commands = [line.strip() for line in file.readlines()]
        file.close()

# Create an SSH client instance 
client = paramiko.SSHClient() 
client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
 
# Connecting to the server 
client.connect(hostname, username=username, password=password)

# Executing the commands withing the script
print(f"{GREEN}HOST: {CYAN}{ip}{RESET}")
print(20*"-")
for command in commands:
    if command:
        print(f"$ {GREEN}{command}")
        stdin, stdout, stderr = client.exec_command(command)
        output = stdout.read().decode('utf-8')
        print(f"{YELLOW}{output}{RESET}")
        print(f"{CYAN}{40*"-"}{RESET}")

# Close the SSH connection 
client.close()
