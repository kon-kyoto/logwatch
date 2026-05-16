import subprocess
import yaml
import re

config = "config/config.yaml"

def main():
    try:
        logs = subprocess.run(
            'journalctl -n 200 | cat',
            shell=True,
            capture_output=True,
            text=True
        )

        with open(config, 'r') as f:
            rules = yaml.safe_load(f)['rules']
        result = ""

        for line in logs.stdout.strip().split('\n'):
            for rule in rules:
                if re.search(rule['pattern'], line):
                    result += f"{rule['severity']}\n"
                    result += f"\t{line}\n"

        return result, False # logs and isError flag
    except Exception as e:
        return str(e), True

if __name__ == "__main__":
    res, isError = main()
    if (isError):
        print("I got some error!!!!\nPLS check `make test`")
    else:
        print(res)
