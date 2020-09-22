import os
from pathlib import Path
from creating_mongo import  insert_pages, find_link, getting_ids, get_path
from config import SITE_NAME, SITE_PROTOCOL
from get_links import get_response, get_content
from bs4 import BeautifulSoup
import nltk
import string
from creating_mongo import insert_words



def create_directory ():
     # get absolute path
    path = Path().absolute()
    dir_name = 'html_files'
    # get full path that folder 
    full_path = os.path.join(path, dir_name)
    # create folder
    if not os.path.exists(full_path):
        os.makedirs(full_path)
    return full_path

def save_html (path):
    """
    Getting id from mongodb
    Save file as html with id's name
    """


    list_ids = getting_ids()
    for id in list_ids:
    
        with open (f'{path + "/" + str(id)}.html', 'w') as f:
            # get path with that id
            link = get_path(id)
            # get page content 
            url = SITE_PROTOCOL + SITE_NAME + link
            content = get_response(url)
            # clearing page content
            f.writelines(content.text)       

            
def load_files(directory):
    """
    Given a directory name, return a dictionary mapping the filename of each
    `.html` file inside that directory to the file's contents as a list.
    """
    data = {}
    dir_list = os.listdir(directory)
    for filename in dir_list:
        path = os.path.join(directory, f"{filename}")
        with open(path, 'r') as f:
            soup = BeautifulSoup(f)
            text = soup.get_text()
            data[filename] = text
          
    return data


def tokenize(document):
    """
    Given a document (represented as a string), return a list of all of the
    words in that document, in order.

    Process document by coverting all words to lowercase, and removing any
    punctuation or English stopwords.
    """
    # list with words from document
    token = nltk.word_tokenize(document)
    words_for_remove = []
    for index in range(len(token)):
        token[index] = token[index].lower()
        if token[index] in nltk.corpus.stopwords.words('english'):
            words_for_remove.append(token[index])
        if token[index] in string.punctuation:
            words_for_remove.append(token[index])

    if len(words_for_remove) != 0:
        for word in words_for_remove:
            token.remove(word)

    return token


def compute_idfs(documents):
    """
    Given a dictionary of `documents` that maps names of documents to a list
    of words, insert a dictionary that maps words to their IDF values in collection mongodb.
    """
    
    for key in documents:
        text = documents[key]
        for word in text:
            data = {'html_name': key, 'word': word, 'count': (text.count(word)/len(text))}
            insert_words(data)
    