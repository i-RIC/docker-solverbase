import os
import subprocess

subprocess.run(['docker', 'build', '-t', 'iric/solver-build', 'iric-solver-build'])
ret = subprocess.run(['docker', 'create', 'iric/solver-build'], stdout=subprocess.PIPE)
c_id = ret.stdout.decode('utf-8').strip()
ret = subprocess.run(['docker', 'cp', c_id + ':/tmp/local.tar.gz', 'iric-solver-run/local.tar.gz'])
subprocess.run(['docker', 'container', 'rm', c_id])
subprocess.run(['docker', 'build', '-t', 'iric/solver-run', 'iric-solver-run'])

os.remove('iric-solver-run/local.tar.gz')
