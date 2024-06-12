import subprocess

__version__=subprocess.run("git tag | tail -n1", shell=True, stdout=subprocess.PIPE).stdout.decode('utf-8').strip()