import requests
from multiprocessing.pool import ThreadPool
from pathlib import Path

headers = {'User-Agent': 'Principia/34 (ROllerozxa)',}

def download_level(i):
	j = 0
	while True:
		data = requests.get("http://img.principiagame.com/full/%s-%s-0.jpg" % (i, j), headers=headers)

		if data.status_code == 200:
			with open("%s-%s-0.jpg" % (i, j), 'wb') as file:
				file.write(data.content)

			j = j + 1
		elif data.status_code == 503:
			return "Caught by ratelimit!"
		elif data.status_code == 404 and j == 0:
			return "Level %s is %s" % (i, data.status_code)
		else:
			return "Level %s thumb downloaded (%s thumbs)" % (i, j)


def main():
	levels = []
	for x in range(30000):
		levels.append((x))

	results = ThreadPool(8).imap_unordered(download_level, levels)

	for lol in results:
		print(lol)


main()
