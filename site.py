import requests
from bs4 import BeautifulSoup
import re
from pymongo import MongoClient

url = 'https://filmix.co/'



def get_response(url, link_set):

    req = requests.get(url)
    reader = req.text

    soup = BeautifulSoup(reader)

    for link in soup.find_all('a', attrs={'href': re.compile('^https://filmix.co/')}):
        
        link_set.add(link.get('href'))

     

def main():
    #  the url wich we will search
    viewed_url = url
    
    stack = [] 
    # adding the url to list
    stack.append(viewed_url)
    # creating set for viewed urls
    explored = set ()

    while True:
        # to take one from list for searching
        node = stack.pop()
        
        explored.add(node)
        # loop the sub_links from searching url
        for link in  neighbors_link(node): 
            if link not in stack and link not in explored:
                # adding all links to list
                stack.append(link)
        
        # to stop loop 
        if len(stack) == 0:
            return explored
    


def neighbors_link (link):
    # getting all links frome webpage
    neighbors = set()
   
    get_response(link, neighbors)
    return list(neighbors)
   
print(main())

# creating list for mongodb
explored_resultat= main()
explored_list =[]
for i in explored_resultat:
    my_dict={'link': i}
    explored_list.append(my_dict)


#  MongoDb
client=MongoClient('localhost', 27017)
db=client['db_link']
col=db['link']
col.insert_many(explored_list)

for y in col.find():
    print(y)