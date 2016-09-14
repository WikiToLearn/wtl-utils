import subprocess
with open('ListaEng', 'r') as f:
  for line in f:
    subprocess.call("./run_docker.sh tuttorotto en au " + line, shell=True)
