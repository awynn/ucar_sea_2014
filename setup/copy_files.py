#!/usr/bin/env python
import subprocess
import shutil
import re

# Copy files for each user
with open('/etc/passwd', 'r') as users:
	data = users.read()

user_list = list(set(re.findall(r'(user[0-9]{3})', data)))

for i in user_list:
	
	# Copy notebooks
	src = '/root/ucar_sea_2014/notebooks/'
	dest = '/home/{0}/notebooks/'.format(i)
	try:
		shutil.rmtree(dest)
	except:
		pass

	shutil.copytree(src, dest)

	cmd = ['chown', '-R', '{0}:{0}'.format(i), dest]
	pid = subprocess.Popen(cmd)
	pid.wait()

	# Create ipython profile
	src = '/root/ucar_sea_2014/.ipython'
	dest = '/home/{0}/.ipython/'.format(i)
	try:
		shutil.rmtree(dest)
	except:
		pass

	shutil.copytree(src, dest)
	cmd = ['chown', '-R', '{0}:{0}'.format(i), dest]
	pid = subprocess.Popen(cmd)
	pid.wait()






