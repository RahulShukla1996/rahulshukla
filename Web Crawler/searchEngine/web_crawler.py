def get_page(url):
    try:
        import urllib
        return urllib.urlopen(url).read()
    except:
        return "error"
    
def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1:
        return None, 0
    start_quote = page.find('"',start_link)
    end_quote = page.find('"',start_quote+1)
    url = page[start_quote+1:end_quote]
    return url, end_quote

def get_all_links(page):
    links = []
    while True:
        url, endpos = get_next_target(page)
        if url:
            links.append(url)
            page = page[endpos:]
        else:
            break
    return links

def union(tc,al):
    for i in al:
        if i not in tc:
            tc.append(i)        

def add_page_to_index(index,url,content):
    words = content.split()
    for word in words:
        add_to_index(index, word, url)

def add_to_index(index, keyword, url):
    for entry in index:
        if entry[0] == keyword:
           #if url not in entry[1]:
              entry.append(url)
        return
    index.append([[keyword],[url]])

def lookup(index,word):
    for entry in index:
        if entry[0] == word:
            return entry[1]
    return []    

def crawl_web(seed):
    tocrawl = [seed]
    crawled = []
    index = []
    while tocrawl:
        page = tocrawl.pop()
        if page not in crawled:
            content = get_page(page)
            add_page_to_index(index,page,content)
            union(tocrawl, get_all_links(content))
            crawled.append(page)
    return index        
            

print crawl_web("http://www.udacity.com/cs101x/index.html")
