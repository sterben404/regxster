import requests
import urllib.parse

encode = urllib.parse.quote('<script>alert(0)</script>') ## URL Encode result text Evil.com


req2 = requests.get('https://regxster.herokuapp.com/?strings={}&before=<script>&after=</script>'.format(encode)) ## request URL regxster for retrieve font color value
print(req2.text)