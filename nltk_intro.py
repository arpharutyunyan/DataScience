import requests
from bs4 import BeautifulSoup
import unicodedata
import sys
import nltk

link = "https://httpstatuses.com/"
req = requests.get(link)

def main():
    importing_dataset()
    data=analyzing_data()
    words=token(data)
    print(words)


def importing_dataset():

    reader = req.text
    with open("my_file.html", "w") as f:
        writer = f.writelines(reader)


def analyzing_data():

    with open("my_file.html") as f:
        soup=BeautifulSoup(f, "html.parser")

        # remove useless tags
        for script in soup("script"):
            script.decompose()
        
        data=[i for i in soup.get_text("|", strip=True).split("|")]

        # get text removing extra whitespace
        # text_data=list(soup.stripped_strings)
        data=[soup.get_text()]
        simbols=dict.fromkeys(i for i in range (sys.maxunicode) if unicodedata.category(chr(i)).startswith("P"))
        data=[string.translate(simbols) for string in data]
        
        return data


def token(data):
    text=nltk.tokenize.word_tokenize(data[0])
    stop_words=nltk.corpus.stopwords.words("english")
    cleared=[word for word in text if word not in stop_words]
    not_repeated=set()
    porter=nltk.stem.porter.PorterStemmer()
    for word in cleared:
        not_repeated.add(porter.stem(word))
    return not_repeated
   

if __name__== "__main__":
    main()