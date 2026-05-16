import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.journal_reader import main

def test_journal_reader():
    result, isError = main()

    assert result in not None, "[ERROR] Result can't be None"
    assert len(result) > 0, "[ERROR] Result can't be blank"

    if (isError):
        assert "Permission denied" in result, "[ERROR] Permission denied"
        assert "No such file" in result, "[ERROR] No such file or directory"


    print("{{SUCCSESS}} daemon is ready")

if __name__ == '__main__':
    test_journal_reader()
