import sys
import os
import pytest

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
        print("{{SUCCSESS}} daemon is READY")
    else:
        pass

def test_parseLogs():
    try:
        result = parseLogs()
        print("{{SUCCSESS}} parseLogs is READY")

        return 0

    except Exception as e:
        if "Journal failed" in str(e):
            print("[ERROR] Journal don't opened pls check journalctl util")
        elif "Parse error" in str(e):
            print("[ERROR] Parse error")
        else:
            pytest.fail(f"[ERROR] {e.value}")

        return 1

def test_matchLogs(logs):
    try:
        matchLogs(logs)
        print("{{SUCCSESS}} matchLogs is READY")
        
        return 0

    except Exception as e:
        if "Config not found" in str(e):
            print("[ERROR] Config not found pls check to config")
        elif "Invalid YAML" in str(e):
            print("[ERROR] Invalid yaml pls check config")
        else:
            print(f"[ERROR] {e.value}")

        return 1

if __name__ == '__main__':
    test_journal_reader()
