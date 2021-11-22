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
    p_result = soup.find_all('p')
    
    
    for paragraph in p_result:
        if paragraph.findChildren('span'):
            result+=paragraph.text         
    return result 




print(get_citations_needed_count(url))
print(get_citations_needed_report(url))

