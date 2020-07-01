import requests
link="https://httpstatuses.com/"
req=requests.get(link)
reader=req.text
with open('my_file.html', 'a+') as f:
    writer=f.writelines(reader)
    


