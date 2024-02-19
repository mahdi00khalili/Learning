
# importing the necessary packages
import requests
from bs4 import BeautifulSoup

# URL of the webpage you want to scrape
input_url = 'https://12factor.net'
base_url = 'https://12factor.net'


# get footer info ...
def getting_footer_info(url):

    # Send a GET request to the URL
    response = requests.get(url)

    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the <footer> tag and parse it
    footer_tag_divs = soup.select('footer > div')

    # creating a dictionary of languages that supported in the site
    languages_dict = {}

    for item in footer_tag_divs[0].text.split('|'):

        temp_list_language =item.strip().split()
        abbr = temp_list_language[-1].replace('(', '').replace(')', '')
        lang = ' '.join(temp_list_language[:-1])

        # the final dictionary of supported languages
        languages_dict[abbr] = lang

    # find the writer info in the page
    writer =footer_tag_divs[1].text

    # find the last updated info in the page
    last_updated = footer_tag_divs[2].text

    # find the source code info in the page
    source_code_link = soup.select('footer > div')[3].find('a').get('href')

    # find the ePub info in the page
    ePub_link = base_url+ soup.select('footer > div')[4].find('a').get('href')
    
    context = {'languages_link':languages_dict,'ePub_link': ePub_link,'source_code_link':source_code_link, 'writer':writer,'last_updated':last_updated}

    return context



# get header info ...

def getting_header_info(url):

    # Send a GET request to the URL
    response = requests.get(url)

    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the <footer> tag and parse it
    header_tag_text = soup.find('header').text.strip()

    return header_tag_text



# get the chapters ...

def getting_chapters(url):

    # Send a GET request to the URL
    response = requests.get(url)

    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the <article> tag and parse it

    chapter_title_link_list = [] # [{'title':title,'link':href, 'description':description}]

    chapter = soup.find_all('article')[-1]
    chapter_titles_links = chapter.find_all('a')
    chapter_description = chapter.find_all('h3')
 


    for i in range(len(chapter_titles_links)):
        # print(chapter_titles_links[i])
        chapter_title = chapter_titles_links[i].text
        chapter_link =chapter_titles_links[i].get('href')
        chapter_desc = chapter_description[i].text
        chapter_title_link_list.append({'title':chapter_title,'link':chapter_link, 'description':chapter_desc})
    return chapter_title_link_list




def getting_chapter_main_content(url):

    # Send a GET request to the URL
    response = requests.get(url)

    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # the main content
    main_content = soup.select('section.abstract')[0]
    

    return main_content








