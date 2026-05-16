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
    except KeyError as e:
        raise Exception(f"Missing key in config: {e}")
    
    for line in logs.strip().split('\n'):
        for rule in rules:
            try:
                if re.search(rule['pattern'], line):
                    result += f"{rule['severity']}\n"
                    result += f"\t{line}\n"
            except KeyError as e:
                raise Exception(f"Rule missing required key: {e}")
            except re.error as e:
                raise Exception(f"Invalid regex pattern: {e}")

    return result

if __name__ == "__main__":
    try:
        res = main()
        print(res)
    except Exception as e:
        print(f"\n\nI got some error!!!!\nPLS check `make test`\n\n")
