from bs4 import BeautifulSoup
import requests
from splinter import Browser
import pprint
import time 
import pandas as pd

# define app function
def scrape_all():
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)
    title,paragraph = mars(browser)
    data={"title": title,
         "paragraph": paragraph,
         "featured_image": featured_img(browser),
         "weather": mars_weather(browser),
         "fact": mars_facts(browser),
         "hemisphere": hemisphere(browser)
    }

    browser.quit()
    return data

# define function for latest headline
def mars(browser):
    #URL of page to be scraped
    news_url = "https://mars.nasa.gov/news/"
    browser.visit(news_url)
    time.sleep(2)
    html = browser.html
    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')

    #extract article title and paragraph text
    try: 
        slide = soup.find('div', class_='list_text')
        title = slide.find('div', class_="content_title").text
        paragraph = slide.find('div', class_="article_teaser_body").text
    except AttributeError:
        return None, None
    return title,paragraph

# define a function for featured images
def featured_img(browser):
    featured_image_url="https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(featured_image_url)
    #click the "Full IMAGE" button
    browser.click_link_by_partial_text('FULL IMAGE')
    time.sleep(1)
    #click "more infomration" button
    browser.click_link_by_partial_text('more info')
    time.sleep(1)

    #access the webpage and parse with Beautiful Soup
    html_img = browser.html
    soup = BeautifulSoup(html_img, 'html.parser')
    feature_image = soup.find('figure', class_='lede')
    image = feature_image.a['href']
    main_image = 'https://jpl.nasa.gov'
    image_url = main_image + image
    return image_url 

# define a function for Mars weather
def mars_weather(browser):
    #URL of page to be scraped
    weather_url="https://twitter.com/marswxreport?lang=en"
    browser.visit(weather_url)
    time.sleep(1)
    
    #access the webpage and parse with Beautiful Soup
    html_weather = browser.html
    soup = BeautifulSoup(html_weather, 'html.parser')

    tweets = soup.findAll("span", {'class':'css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0'})

    for tweet in tweets:
        if "InSight sol" in tweet.text and "low" in tweet.text:
            mars_weather=tweet.text
            break
    return mars_weather

# define a function for Mars facts
def mars_facts(browser):
    #URL of page to be scraped
    facts_url = "https://space-facts.com/mars/"
    table = pd.read_html(facts_url)
    facts_df=table[0]
    facts_df.columns = ['description', 'value']
    facts_df.set_index('description', inplace=True)
    html_table = facts_df.to_html(classes="table table-striped")
    return html_table

# define a function for Mars hemispheres
def hemisphere(browser):
    hemispheres_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(hemispheres_url)
    time.sleep(2) 

    html_hemispheres = browser.html
    soup = BeautifulSoup(html_hemispheres, "html.parser")
    hemispheres = soup.findAll("div", class_="description")
    list=[]
    main_url="http://astrogeology.usgs.gov"

    # loop to go through four hemispheres
    for record in hemispheres:
        title = record.find('a', class_="itemLink product-item").text
        #click the hyperlink using the title info
        browser.click_link_by_partial_text(title)
        time.sleep(1)
        #access the new webpage
        html2 = browser.html
        #Parse HTML with Beautiful Soup
        soup2 = BeautifulSoup(html2, 'html.parser')
        #obtain the link for full size picture
        image_url = soup2.find('img', class_='wide-image')['src']
        #add the main_url
        url = main_url+image_url
        #add title and url in the list
        Sum = {}
        Sum['title']=title
        Sum['url']=url
        list.append(Sum)
        #go to the original page
        browser.visit(hemispheres_url)
        time.sleep(1)
    return list