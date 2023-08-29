import subprocess
import time
import webbrowser

# First make sure service isn't running
cmd = ["docker", "compose", "down"]
subprocess.check_call(cmd)

# Start docker compose service
cmd = ["docker", "compose", "up"]
process = subprocess.Popen(
    cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True
)
browser_opened = False

try:
    for line in process.stdout:
        print(line, end="")
        if not browser_opened and "127.0.0.1" in line:
            url = line.split("|")[-1].strip()
            webbrowser.open(url)
            browser_opened = True
except KeyboardInterrupt:  # If the user interrupts the script...
    # ...first kill the process
    process.terminate()
    process.wait()
    # ...then kill the Docker service.
    cmd = ["docker", "compose", "down"]
    subprocess.check_call(cmd)
