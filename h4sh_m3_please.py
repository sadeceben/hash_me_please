import requests, re, hashlib

class Flag:

	def __init__(self):
		self.username  = ""
		self.password  = ""
		self.regex     = '----- BEGIN MESSAGE -----<br />\r\n\t\t(\w+)'
		self.flag      = 'FLAG-\w+'
		self.login_url = "https://ringzer0ctf.com/login"
		self.url       = "https://ringzer0ctf.com/challenges/13/"
		self.wrong     = "Wrong answer or too slow!"
		self.run       = requests.session()

	def get(self):

		data = dict( username=self.username, password=self.password)
		first = self.run.post(self.login_url, data=data)
		req = self.run.post(self.url)
		req_e = self.run.post(self.url + self.hash(re.search(self.regex , req.text).group(1)))
		print(re.search(self.flag ,req_e.text).group(0))

	def hash(self , message):
		return hashlib.sha512(message.encode("ASCII")).hexdigest()

if __name__ == '__main__':
	run = Flag()
	run.get()

