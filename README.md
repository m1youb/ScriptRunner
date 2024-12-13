# ScriptRunner
A python script to automate running scripts on hosts without manual login into them.
> Don't forget to install the required python library `paramiko` before running `runner.py`, using:
> ```sh
>   pip install paramiko
> ```
# Example:
```bash
python3 runner.txt -i 10.10.10.10 -u root -a pass123 -s script.txt
```
