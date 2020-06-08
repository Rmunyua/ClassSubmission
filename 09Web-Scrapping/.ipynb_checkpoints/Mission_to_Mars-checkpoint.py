from bs4 import BeautifulSoup
import requests
import pprint
from splinter import Browser
import time 
import pandas as pd

# define an overal function
def scrape_all():
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)
    title,paragraph = mars_new(browser)
    data={"title": title,
         "paragraph": paragraph,
         "feature_image": featured_img(browser),
         "weather": mars_weather(browser),
         "fact": mars_facts(browser),
         "hemisphere_image_urls": hemisphere(browser)
    }

    browser.quit()
    return data

# define function for latest headline
def mars_new(browser):
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)
    time.sleep(2)
    html = browser.html
    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')
    # Extract article title and paragraph text

    try: 
        result = soup.find("div", class_='list_text')
        title = result.find("div", class_="content_title").text
        paragraph = result.find("div", class_ ="article_teaser_body").text
    except AttributeError:
        return None, None
    return title,paragraph

#define a function for featured images
def featured_img(browser):
    url2="https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url2)
    # click the "Full IMAGE" button
    browser.click_link_by_partial_text('FULL IMAGE')
    time.sleep(1)
    # click "more infomration" button
    browser.click_link_by_partial_text('more info')
    time.sleep(1)

    #Access the webpage
    html2 = browser.html

    # Parse HTML with Beautiful Soup
    soup2 = BeautifulSoup(html2, 'html.parser')
    featureimage= soup2.find('figure', class_='lede')
    image_url=featureimage.a['href']
    featured_image_url="https://www.jpl.nasa.gov" + image_url
    return featured_image_url

# define a function for Mars weather
def mars_weather(browser):
    url3="https://twitter.com/marswxreport?lang=en"
    browser.visit(url3)
    time.sleep(1) # https://stackoverflow.com/questions/15866426/beautifulsoup-not-grabbing-dynamic-content
    html3 = browser.html
    soup = BeautifulSoup(html3, 'html.parser')

    result_3 = soup.findAll("span", {'class':'css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0'})

    for result in result_3:
        if "InSight sol" in result.text and "low" in result.text:
            mars_weather=result.text
            break
    return mars_weather

# define a function for Mars facts
def mars_facts(browser):
    url4 = "https://space-facts.com/mars/"
    fact_table = pd.read_html(url4)
    fact_df=fact_table[0]
    fact_df.columns = ['description', 'value']
    fact_df.set_index('description', inplace=True)
    html_table = fact_df.to_html(classes="table table-striped")
    return html_table

# define a function for Mars hemispheres
def hemisphere(browser):
    url5="https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url5)
    time.sleep(2) 

    html5 = browser.html
    soup = BeautifulSoup(html5, "html.parser")
    hemisphere= soup.findAll("div", class_="description")
    hemi_list=[]
    base_url="http://astrogeology.usgs.gov"

    # for loop to go through four hemispheres
    for record in hemisphere:
        title=record.find('a', class_="itemLink product-item").text
        # click the hyperlink using the title info
        browser.click_link_by_partial_text(title)
        time.sleep(1)
        #Access to the new webpage
        html6 = browser.html
        # Parse HTML with Beautiful Soup
        soup6 = BeautifulSoup(html6, 'html.parser')
        # obtain the link for full size picture
        image_url = soup6.find('img', class_='wide-image')['src']
        # add the base_url
        url=base_url+image_url
        #put title and url in the list
        hemi_summary={}
        hemi_summary['title']=title
        hemi_summary['url']=url
        hemi_list.append(hemi_summary)
        #reset the browser visit to the original page
        browser.visit(url5)
        time.sleep(1)
    return hemi_list