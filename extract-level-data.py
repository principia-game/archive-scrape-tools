from bs4 import BeautifulSoup
import json
import time, datetime
import re

def replace_all(text, dic):
	for i, j in dic.items():
		text = text.replace(i, j)
	return text

data = []

for i in range(28100):
	if i == 0: continue

	with open('%s.html' % i, 'r', errors="replace") as f:
		html = f.read()

	if "A level with this ID does not exist." in html:
		continue

	soup = BeautifulSoup(html, 'html.parser')

	title = soup.h1.text
	author = soup.find(class_="user").get('href').replace('/user/', '')
	uploaded = time.mktime(datetime.datetime.strptime(soup.time.get('datetime'), "%Y-%m-%dT%H:%M:%S+00:00").timetuple())
	if i == 379:
		platform = "N/A"
	else:
		platform = re.search(r'from \w+', soup.find(class_="misc").text).group().replace('from ', '')
	if soup.find(id="lvl-box-info").text == "This level is locked.":
		locked = 1
	else:
		locked = 0

	cat_text = soup.find(class_="misc").text
	if "- Custom level -" in cat_text:
		cat = 1
	elif "- Adventure level -" in cat_text:
		cat = 2
	elif "- Puzzle level -" in cat_text:
		cat = 3

	if soup.find(class_="likemsg"):
		likes = soup.find(class_="likemsg").text.replace(' players liked this.', '').replace(' player liked this.', '').replace('One', "1")
	else:
		likes = 0

	if locked == 1:
		downloads = 0
	else:
		if soup.find(id="lvl-data"):
			downloads = re.search(r'Downloads: \d+', soup.find(id="lvl-data").text).group().replace('Downloads: ', '')
		else:
			downloads = 0

	data.append({
		'id': i,
		'cat': cat,
		'title': title,
		'author': int(author),
		'uploaded': int(uploaded),
		'platform': platform,
		'locked': locked,
		'likes': int(likes),
		'downloads': int(downloads)
	})

	print(str(i) + " - " + title)

with open("leveldata_bkjk.json", "w") as f:
	json.dump(data, f, indent=4)
