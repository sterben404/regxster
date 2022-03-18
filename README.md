# RegXster

This tool is used to extract the desired character from a string

# How does it work?

https://regxster.herokuapp.com/?

```Parameter```
- /json/ __results will be type JSON__
- strings=__whole string__
- before=__string before the character you want to retrieve__
- after=__string after the character you want to retrieve__

> Note: if the string contains special characters or the like. have to encrypt the URL Encoding type first

# Example

__Input__

```
https://regxster.herokuapp.com/?strings=<script>alert('hello word')</script>&before=<script>&after=</script>
```

__Output__

```
alert('hello word')
```
## With JSON
__Input__

```
https://regxster.herokuapp.com/json?strings=<script>alert('hello word')</script>&before=<script>&after=</script>
```

__Output__
```
["alert('hello word')"]
```

## If Contain Special Character
__Without URL Encode__
> <script>#alert@('hello word')</script>
__With URL Encode__
> %3Cscript%3E%23alert%40%28%27hello%20word%27%29%3C%2Fscript%3E

__Input__
```
https://regxster.herokuapp.com/json/?strings=%3Cscript%3E%23alert%40%28%27hello%20word%27%29%3C%2Fscript%3E&before=%3Cscript%3E&after=%3C/script%3E
```

__Output__
```
["#alert@('hello word')"]
```




```diff
- The point is if it contains special characters or has many characters, use URL Encoding
```
## Example with Scripting Code
Python
```python
import requests
import urllib.parse

encode = urllib.parse.quote('<script>alert(0)</script>') ## Encoding Strings


req2 = requests.get('https://regxster.herokuapp.com/?strings={}&before=<script>&after=</script>'.format(encode)) ## request URL regxster for retrieve font color value
print(req2.text)
```

__Output__

```alert(0) ```

Thanks
