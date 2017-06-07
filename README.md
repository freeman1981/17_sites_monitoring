# Sites Monitoring Utility

Assume you have file foo.txt with urls - new url in new line.

For example
```
http://ya.ru
https://google.com
https://devman.org
```
Run 
```
python3 check_sites_health.py foo.txt 
```
Will show
```python
{'IS NOT EXPIRED FOR MONTH': True, 'URL': 'http://ya.ru', 'IS 200 OK': True}
{'IS NOT EXPIRED FOR MONTH': True, 'URL': 'https://google.com', 'IS 200 OK': True}
{'IS NOT EXPIRED FOR MONTH': True, 'URL': 'https://devman.org', 'IS 200 OK': True}
```

You should install 
```requirements python3 -m pip install requirements.txt```
in vitual enviroment.

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
