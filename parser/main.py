import get_links
import creating_mongo

SITE_PROTOCOL = "http://"
SITE_NAME = "foodtime.am"


def main():
    
    url = SITE_PROTOCOL + SITE_NAME
    # get page content
    soup = get_links.get_content(url)
    # clear soup and insert mongodb
    get_links.get_page_links(soup, SITE_NAME)
    # get sublinks
    get_links.getting_sublinks()
  


if __name__=='__main__':
    main()