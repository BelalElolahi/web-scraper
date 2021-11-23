import requests
from bs4 import BeautifulSoup


url='https://en.wikipedia.org/wiki/History_of_Mexico'

def get_citations_needed_count(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content,'html.parser')
    result = soup.findAll('span',text='citation needed')
    print(result)
    return len(result)

def  get_citations_needed_report(url):
    result = ''
    page=requests.get(url)
    soup=BeautifulSoup(page.content, 'html.parser')
    sup_result = soup.find_all('sup')
    
    
    for sup in sup_result:
        if sup.findChildren('span'):
            #print(sup)
            result+= f'\n - { sup.previous_sibling }[citation needed] .'
            result+=' \n '  
              
    return result 

print(get_citations_needed_count(url))
print(get_citations_needed_report(url))

