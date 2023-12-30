import requests
from multiprocessing.pool import ThreadPool
from pathlib import Path

headers = {'User-Agent': 'Principia/34 (ROllerozxa)',}

def download_user(i):
	if Path("%s.html" % i).exists():
		return "User %s already downloaded, skipping" % i

	data = requests.get("http://archive.principiagame.com/user/%s" % i, headers=headers)

	if data.status_code == 200:
		with open("%s.html" % i, 'wb') as file:
			file.write(data.content)

		return "User %s downloaded" % i
	elif data.status_code == 503:
		return "Caught by ratelimit!"
	else:
		return "User %s is %s" % (i, data.status_code)


def main():
	"""for x in range(13798):
		print(download_user(x))"""

	users = []
	for x in range(13798):
		users.append((x))

	results = ThreadPool(10).imap_unordered(download_user, users)

	for lol in results:
		print(lol)

main()
