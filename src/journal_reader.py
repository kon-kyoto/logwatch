import subprocess

result = subprocess.run(
    'journalctl -n 50 | cat',
    shell=True,
    capture_output=True,
    text=True
)
print(result.stdout)
