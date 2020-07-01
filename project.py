import requests
link="https://httpstatuses.com/"
req=requests.get(link)
reader=req.text
with open('my_file.html', 'w') as f:
    writer=f.writelines(reader)
with open("my_file.html") as f:
    # to get line as a list
    for line in f.readlines():
        # to choose lines where there are <li> and not include </li>
        # or empty line
        if "li" in line and "span"  in line:
            
            new_line=line.split("</span>")
            # have a list like this
            # ['<li><a href="/409"><span>409', 
            #   ' Conflict</a></li>\n']

            discription=new_line[1].split("<")
            print(new_line[0][-3:], discription[0])
            