from find_link import find_next_link
import urllib

def print_all_links(page):
    while True:
        url, endpos = find_next_link(page)
        if url:
            print url
            page = page[endpos:]
        else:
            break
print_all_links(urllib.urlopen("http://www.ibef.org/industry/oil-gas-india.aspx").read())
