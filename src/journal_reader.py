import subprocess
import yaml
import re

def main():
    try:
        logs = subprocess.run(
            'journalctl -n 200 | cat',
            shell=True,
            capture_output=True,
            text=True
        )

        result, isError = matchLogs(logs.stdout)

        if (isError): raise result

        return result, False # logs and isError flag
    except Exception as e:
        return str(e), True

def matchLogs(logs):
    config = "config/config.yaml"
    result = ""

    try:
        with open(config, 'r') as f:
            rules = yaml.safe_load(f)['rules']

        for line in logs.strip().split('\n'):
            for rule in rules:
                if re.search(rule['pattern'], line):
                    result += f"{rule['severity']}\n"
                    result += f"\t{line}\n"

        return result, False

    except Exception as e:
        return e, True


if __name__ == "__main__":
    res, isError = main()
    if (isError):
        print("I got some error!!!!\nPLS check `make test`")
    else:
        print(res)
