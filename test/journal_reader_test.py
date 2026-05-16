import sys
import os

class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.journal_reader import main, parseLogs, matchLogs

def test_journal_reader():
    err_sum = 0
    test_logs = """
	May 16 11:55:13 cmp login[366189]: FAILED LOGIN 1 FROM tty3 FOR root, Authentication failure
	May 16 11:55:19 cmp login[366189]: FAILED LOGIN 2 FROM tty3 FOR user, Authentication failure
	May 16 12:10:23 cmp login[371106]: FAILED LOGIN 1 FROM tty3 FOR root, Authentication failure
	May 16 12:10:28 cmp login[371106]: FAILED LOGIN 2 FROM tty3 FOR user, Authentication failure
    """
    err_sum += test_parseLogs()
    err_sum += test_matchLogs(test_logs) 

    if err_sum == 0:
        print(f"{Colors.GREEN}{Colors.BOLD}[SUCCESS]{Colors.RESET} daemon is READY")
    else:
        pass

def test_parseLogs():
    try:
        result = parseLogs()
        print(f"{Colors.GREEN}{Colors.BOLD}[SUCCESS]{Colors.RESET} parseLogs is READY")

        return 0

    except Exception as e:
        if "Journal failed" in str(e):
            print(f"{Colors.RED}[ERROR]{Colors.RESET} Journal don't opened pls check journalctl util")
        elif "Parse error" in str(e):
            print(f"{Colors.RED}[ERROR]{Colors.RESET} Parse error")
        else:
            print(f"{Colors.RED}[ERROR]{Colors.RESET} {str(e)}")

        return 1

def test_matchLogs(logs):
    try:
        matchLogs(logs)
        print(f"{Colors.GREEN}{Colors.BOLD}[SUCCESS]{Colors.RESET} {Colors.GREEN}matchLogs is READY{Colors.RESET}")
        return 0

    except Exception as e:
        if "Config not found" in str(e):
            print(f"{Colors.RED}[ERROR]{Colors.RESET} Config not found pls check to config")
        elif "Invalid YAML" in str(e):
            print(f"{Colors.RED}[ERROR]{Colors.RESET} Invalid yaml pls check config")
        elif "Missing key" in str(e) or "missing required key" in str(e):
            print(f"{Colors.RED}[ERROR]{Colors.RESET} {str(e)}")
        elif "pattern" in str(e) and "KeyError" in str(type(e).__name__):
            print(f"{Colors.RED}[ERROR]{Colors.RESET} Rule missing 'pattern' key in config")
        else:
            print(f"{Colors.RED}[ERROR]{Colors.RESET} {str(e)}")
        return 1 

if __name__ == '__main__':
    test_journal_reader()
