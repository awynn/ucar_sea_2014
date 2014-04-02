#!/usr/bin/env python
import subprocess
import shutil
import re


# Start the notebooks on each node
with open('/etc/hosts', 'r') as hosts:
	data = hosts.read()

node_list = list(set(re.findall(r'(node[0-9]{3})', data)))

# Kill all notebooks
for node in node_list:
	cmd = ['ssh', node, '`pkill -f "ipython"`']
	pid = subprocess.Popen(cmd)
	pid.wait()
