#python3
import requests
url = "http://167.71.248.246/secure/"
r = requests.post(url)
print(r.text)
# our secret flag is: EGCTF{0xae11d8_is_a_t4mp3rat0r}
