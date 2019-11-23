import os
import subprocess

#subprocess.run(['docker', 'build', '-t', 'iric/solver-build-test', 'iric-solver-build-test'])
subprocess.run(['docker', 'build', '-t', 'iric/solver-build', 'iric-solver-build'])
#ret = subprocess.run(['docker', 'create', 'iric/solver-build-test'], stdout=subprocess.PIPE)
ret = subprocess.run(['docker', 'create', 'iric/solver-build'], stdout=subprocess.PIPE)
c_id = ret.stdout.decode('utf-8').strip()
ret = subprocess.run(['docker', 'cp', c_id + ':/usr/local/lib/libiriclib.so', 'iric-solver-run/libiriclib.so'])
#ret = subprocess.run(['docker', 'cp', c_id + ':/data/iriclib-0.2/build/unittests_cgnsfile/unittests_cgnsfile', 'iric-solver-run/unittests_cgnsfile'])
subprocess.run(['docker', 'container', 'rm', c_id])
subprocess.run(['docker', 'build', '-t', 'iric/solver-run', 'iric-solver-run'])

os.remove('iric-solver-run/libiriclib.so')
