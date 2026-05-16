import subprocess

def main():
    try:
        result = subprocess.run(
            'journalctl -n 50 | cat',
            shell=True,
            capture_output=True,
            text=True
        )
        return result.stdout, False # result and isError flag
    except Exception as e:
        return str(e), True

if __name__ == "__main__":
    res, isError = main()
    if (not isError):
        print(res)
