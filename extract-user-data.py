from bs4 import BeautifulSoup
import json

def replace_all(text, dic):
    for i, j in dic.items():
        text = text.replace(i, j)
    return text

data = []

for i in range(13798):
	if i == 0: continue

	with open('%s.html' % i, 'r') as f:
		html = f.read()

	soup = BeautifulSoup(html, 'html.parser')
	username = replace_all(str(soup.h2), {
		'<h2 class="fleft header">': '',
		'<h2>': '',
		'</h2>': '',
	})

	if username == "No user found.":
		continue

	#data.append({
    #    'id': i,
    #    'name': username
	#})

	print(username)

#with open("userdata.json", "w") as f:
#	json.dump(data, f, indent=4)
