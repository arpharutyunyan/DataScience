import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from creating_mongo import  mongo_connection, find_link, getting_ids, get_path

SITE_PROTOCOL = "http://"
SITE_NAME = "foodtime.am"


def get_content(url):

    """
    Get one URL
    Return all content from html file

    """

    response = requests.get(url)
    # check if that page is success (200, 201, 202, .... , 208, 226)
    if 200 <= response.status_code <= 226:
        # get html content as text
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup
    # if the page is not found or another Errors
    return None
   

def get_page_links (soup, site_name=SITE_NAME):

    """
    Clear and take used tage 
    insert values into mongodb

    """

    for link in soup.find_all('a'):
        href = link.get('href')
        o = urlparse(href)
        # check if there is path
        if o.path:
            # find all inside domains
            if o.netloc == site_name or not o.netloc:
                # check if there is that path in mongodb
                res = find_link(o.path)                       
                if res==0:
                    data = {'protocol': o.scheme, 'domain': o.netloc, 'path': o.path}
                    # get id and save dict in mongodb
                    index = mongo_connection(data)
                    # save htm file
                    save_html(soup, index, o.path)
                 

def getting_sublinks ():

    explored = set()
    i = 0
    while True:
        # get ids from mongodb
        list_ids = getting_ids()
        # break if all ids explored
        if len(explored) + 1 == len(list_ids):
            break
        # get one id
        id = list_ids[i]
        if id not in explored:
            explored.add(id)
            # get path with that id
            path = get_path(id)
            # get page content 
            soup = get_content(SITE_PROTOCOL + SITE_NAME + path)
            # clearing page content
            get_page_links(soup)
        i+=1

        
        
def save_html (soup, id, link):
    """
    Getting id from mongodb
    Save file as html with id's name
    """

    full_path = '/home/arpine/Desktop/ML/parser/html_files/'
  
    with open (f'{full_path + str(id)}.html', 'w') as f:
        f.writelines(str(soup))

