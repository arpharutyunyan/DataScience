import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from creating_mongo import  insert_pages, find_link, getting_ids, get_path
from config import SITE_NAME, SITE_PROTOCOL

def get_response(url):
    # get response
    response = requests.get(url)
    return response


def get_content(url):

    """
    Get one URL
    Return all content from html file

    """

    response = get_response(url)
    # check if that page is success (200, 201, 202, .... , 208, 226)
    if 200 <= response.status_code <= 226:
        # get html content as text
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup
    # if the page is not found or another Errors
    return None
   

def get_page_links (soup):

    """
    Clear and take used tage 
    insert values into mongodb

    """
    if soup:
        for link in soup.find_all('a'):
            href = link.get('href')
            o = urlparse(href)
            # check if there is path
            if o.path:
                # find all inside domains
                if o.netloc == SITE_NAME or not o.netloc:
                    # check if there is that path in mongodb
                    res = find_link(o.path)                       
                    if res==0:
                        data = {'protocol': o.scheme, 'domain': o.netloc, 'path': o.path}
                        # get id and save dict in mongodb
                        insert_pages(data)
                        # index = mongo_connection(data)
                        # save htm file
                        # save_html(soup, index)
                    

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