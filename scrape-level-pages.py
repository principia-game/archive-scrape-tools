import requests
from multiprocessing.pool import ThreadPool
from pathlib import Path

headers = {'User-Agent': 'Principia/34 (ROllerozxa)',}

def download_level(i):
	if Path("%s.html" % i).exists():
		return "Level %s already downloaded, skipping" % i

	data = requests.get("http://archive.principiagame.com/level/%s" % i, headers=headers)

	if data.status_code == 200:
		with open("%s.html" % i, 'wb') as file:
			file.write(data.content)

		return "Level %s downloaded" % i
	elif data.status_code == 503:
		return "Caught by ratelimit!"
	else:
		return "Level %s is %s" % (i, data.status_code)


def main():
	levels = []
	for x in range(28100):
		levels.append((x))

	results = ThreadPool(10).imap_unordered(download_level, levels)

	for lol in results:
		print(lol)


main()
