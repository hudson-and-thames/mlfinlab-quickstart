import subprocess
import webbrowser

# First make sure service isn't running
cmd = ["docker", "compose", "down"]
subprocess.check_call(cmd)

# Start docker compose service
cmd = ["docker", "compose", "up"]
process = subprocess.Popen(
    cmd,
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT,
    text=True
)

try:
    for line in process.stdout:
        print(line, end='')
        if "127.0.0.1" in line:
            url = line.split("|")[-1].strip()
            webbrowser.open(url)
except KeyboardInterrupt:
    process.terminate()
    process.wait()
    cmd = ["docker", "compose", "down"]
    subprocess.check_call(cmd)
