Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import urllib
>>> import urllib2
>>> values={}
>>> values['username'] = "2915912248@qq.com"
>>> values['password']="XXXX"
>>> 
KeyboardInterrupt
>>> data = urllib.urlencode(values)
>>> url = "https://github.com/zhucuicuia/ZCC40.git"
>>> geturl = url + "?"+data
>>> request = urllib2.Request(geturl)
>>> 
>>> response = urllib2.urlopen(request)
>>> 
KeyboardInterrupt
>>> print response.geturl()
https://github.com/zhucuicuia/ZCC40?username=2915912248%40qq.com&password=XXXX
>>> 
