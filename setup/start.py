#!/usr/bin/env python
import subprocess
import shutil
import re

# Copy files for each user
with open('/etc/passwd', 'r') as users:
	data = users.read()

user_list = list(set(re.findall(r'(user[0-9]{3})', data)))

# Start the notebooks on each node
with open('/etc/hosts', 'r') as hosts:
	data = hosts.read()

node_list = list(set(re.findall(r'(node[0-9]{3})', data)))

# Kill all notebooks
for node in node_list:
	cmd = ['ssh', node, '`pkill -f "ipython"`']
	pid = subprocess.Popen(cmd)
	pid.wait()

for user, node in zip(sorted(user_list), sorted(node_list)):

	#print user, node
	dest = '/home/{0}/notebooks'.format(user)
	print dest
	
	cmd = ['ssh', node, '`su - {0} -c "/usr/local/bin/ipython notebook --notebook-dir={1}"`'.format(user,dest)]
	#cmd = ['ssh', '{0}@{1}'.format(user, node), '`echo hostname`']
	pid = subprocess.Popen(cmd)
	#pid.wait()
