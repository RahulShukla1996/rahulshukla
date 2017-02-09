def find_next_link(page):
    start_link =  page.find('<a href=')
    if start_link == -1:
        return 0, None
    start_quote = page.find('"',start_link)
    end_quote = page.find('"',start_quote+1)
    url = page[start_quote+1:end_quote]
    return url, end_quote

#url, endpos = find_next_link('this is a <a href="http://google.com">link!</a>')
#print url
