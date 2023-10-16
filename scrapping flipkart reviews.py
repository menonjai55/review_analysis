from cmath import e
from selenium import webdriver
from bs4 import BeautifulSoup
import requests as rq
from selenium.webdriver.chrome.service import Service
import pandas as pd
from time import sleep
import re

# Input the URL of the product page
product_url = input('Enter URL: ')

# Creating variables to store the data
rating = []
review = []
comment = []
link = []

# Set up a headless Firefox WebDriver
options = webdriver.FirefoxOptions()
options.headless = True
driver = webdriver.Firefox(options=options)


try:
    # Open the product page
    driver.get(product_url)
    sleep(2)  # Add a delay to ensure page loading

    # Scroll down to all reviews hyperlink (adjust the scroll amount as needed)
    for _ in range(5):
        driver.execute_script("window.scrollBy(0, 1000);")
        sleep(1)

    # Get the page source after scrolling
    page_source = driver.page_source

    # Parse the page source with BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find all 'a' elements with 'href' containing '/product-reviews/'
    review_links = soup.find('a', href=re.compile('/product-reviews/'))
    review_url = review_links.get('href')
    print(review_url)
    f_url = ('https://www.flipkart.com' + str(review_url))
    print(f_url)

    # # If multiple page links with the same name in the url are present create list with multiple entries
    # for link in review_links:
    #     review_url = link.get('href')
    #     review_urls.append(review_url)
    #
    # # Print the review URLs
    # for url in review_urls:
    #     print("Review URL:", url)

    # Go to the review pages and run beautiful soup on the page
    driver.get(f_url)

    # scroll to bottom of the page
    for _ in range(3):
        driver.execute_script("window.scrollBy(0, 1000);")
        sleep(1)

    # Get the page source after scrolling
    page_source2 = driver.page_source

    # Parse the page source with BeautifulSoup
    soup2 = BeautifulSoup(page_source2, 'html.parser')

    div = soup2.find('div', {'class': '_2MImiq _1Qnn1K'})

    # Find the number of review pages to scrape
    if div:
        span = div.find('span')
        if span:
            text = span.text
            print(text)
            y = int(text.split("of")[-1].strip())
            print(y)
        else:
            print("Span element not found")
    else:
        print("Div element not found")


    # iterating through the review pages
    i = 1
    while i <= y:
        driver.get(str(f_url) + "&page=" + str(i))
        page_source3 = driver.page_source
        soup3 = BeautifulSoup(page_source3, 'html.parser')
        classes = ['_3LWZlK _1BLPMq', '_3LWZlK _32lA32 _1BLPMq', '_3LWZlK _1rdVr6 _1BLPMq']

        # populate the rating of the review
        for class_name in classes:
            try:
                for ra in soup3.find_all('div', {'class': class_name}):
                    aa = ra.getText()
                    rating.append(aa)
            except:
                pass
        # populate the title of the review
        for re in soup3.find_all('p', {'class': '_2-N8zT'}):
            bb = re.get_text()
            review.append(bb)
        # populate the text of the review
        for co in soup3.find_all('div', {'class': 't-ZTKy'}):
            cc = co.getText()
            comment.append(cc)
        sleep(1)
        i += 1

    # converting the content into a dataframe and exporting it to a csv file
    df = pd.DataFrame({'rating': rating, 'review': review, 'comment': comment})
    df.to_csv('fkart_rev.csv', index=False)

except Exception as e:
    print(f"An error occurred: {str(e)}")

finally:
    # Close the WebDriver
    driver.quit()



