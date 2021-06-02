# На данный момент не работает так как API youtube'а был изменен
import json
from urllib.request import urlopen
url = "https://www.googleapis.com/youtube/v3/videos?id=7lCDEYXw3mM&ke"
response = urlopen(url)
contents = response.read()
text = contents.decode('utf8')
data = json.loads(text)
for video in data['error']['code'][0:1]:
	print(video['title']['$t'])