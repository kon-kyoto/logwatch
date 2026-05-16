import subprocess
import yaml
import re

def main():
    logs = parseLogs()
    result = matchLogs(logs.stdout)
    return result

def parseLogs():
    try:
        logs = subprocess.run(
            'journalctl -n 200 | cat',
            shell=True,
            capture_output=True,
            text=True,
            check=True
        )
        return logs
    except subprocess.CalledProcessError as e:
        raise Exception(f"Journal failed: {e}")
    except Exception as e:
        raise Exception(f"Parse error: {e}")

def matchLogs(logs):
    config = "config/config.yaml"
    result = ""

    try:
        with open(config, 'r') as f:
            rules = yaml.safe_load(f)['rules']
    except FileNotFoundError:
        raise Exception(f"Config not found: {config}")
    except yaml.YAMLError as e:
        raise Exception(f"Invalid YAML: {e}")
    
    for line in logs.strip().split('\n'):
        for rule in rules:
            if re.search(rule['pattern'], line):
                result += f"{rule['severity']}\n"
                result += f"\t{line}\n"

    return result

if __name__ == "__main__":
    res = main()
    print(res)
