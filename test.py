import requests

return_str = requests.get('http://127.0.0.1:5000/')
return_str.encoding = 'utf-8' 

is_pass = 'Hello' in return_str.text
if(is_pass):
    print("pass")
