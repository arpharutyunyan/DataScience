import requests
from bs4 import BeautifulSoup 
from requests_html import HTML


link="https://httpstatuses.com/"
req=requests.get(link)
reader=req.text
def variant_1():
    print("Result N 1: ")

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


def variant_2():
    print("Result N 2: ")

    soup=BeautifulSoup(req.text)
    # selec "a" in "li"
    tag_a=soup.select("li a")
    for link in tag_a:
        print(link.get_text())


def variant_3():
    print("Result N 3: ")

    with open("my_file.html") as f:
        read_file=f.read()
        html=HTML(html=read_file)
    tags=html.find("li a")
    for tag in tags:
        print(tag.text)

variant_1()
variant_2()
variant_3()