import get_links
import creating_mongo
from config import URL
from parsing_html import create_directory, save_html, load_files, tokenize, compute_idfs


def main():
    
    # get page content
    print('Loading pages...')
    soup = get_links.get_content(URL)
    # clear soup and insert mongodb
    get_links.get_page_links(soup)
    # get sublinks
    get_links.getting_sublinks()
    print('Pages loaded.')

    path = create_directory()

    print('Saving html...')
    save_html(path)
    print('Html saved.')
    # get files list
    files = load_files(path)
    # dict with filenames key and value as cleaning list
    file_words = {
        filename: tokenize(files[filename])
        for filename in files
    }
    compute_idfs(file_words)

    


if __name__=='__main__':
    main()