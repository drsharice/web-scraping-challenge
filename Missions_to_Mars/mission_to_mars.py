#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Dependencies
from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import requests


# In[2]:


# NASA Mars News page to be scraped
news_url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'


# In[3]:


# Retrieve page with the requests module
response = requests.get(news_url)


# In[4]:


# Create BeautifulSoup object; parse with 'html.parser'
soup = BeautifulSoup(response.text, 'html.parser')


# In[5]:


# Examine the results, then determine element that contains sought info
print(soup.prettify())


# In[6]:


# results are returned as an iterable list
results = soup.find_all('li', class_="result-row")


# In[8]:


#NASA Mars Assign the text to variables

news_title = soup.title

news_p = soup.p


# In[3]:


# Setup splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[16]:


#JPL Mars Space
url = 'https://www.jpl.nasa.gov/images?search=&category=Mars'
browser.visit(url)


# In[6]:


browser.quit()


# In[7]:


# URL of page to be scraped
mars_fact_url = 'https://space-facts.com/mars/'


# In[8]:


# Retrieve page with the requests module
response = requests.get(mars_fact_url)


# In[9]:


# Create BeautifulSoup object; parse with 'html.parser'
soup = BeautifulSoup(response.text, 'html.parser')


# In[10]:


# Examine the results, then determine element that contains sought info
print(soup.prettify())


# In[ ]:


img = 


# In[31]:


# Setup splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[40]:


# URL of page to be scraped
USGS_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(USGS_url)


# In[39]:


#Mars Hemisphere
links_found = browser.links.find_by_partial_text('Hemisphere Enhanced')

hemisphere_url_list=[]
for link in links_found:
    link.click()
    sample_dict={}
    sample_dict["img_url"]=browser.links.find_by_partial_text('Sample')[0]["href"]
    sample_dict["title"]=browser.find_by_css('h2.title').text
    hemisphere_url_list.append(sample_dict)
    


# In[38]:


#Mars Hemisphere
links_found = browser.links.find_by_partial_text('Hemisphere Enhanced')

hemisphere_url_list=[]

for i in range(len(links_found)):
    links_found = browser.links.find_by_partial_text('Hemisphere Enhanced')
    link = links_found[i]
    link.click()
    pictures_found = browser.links.find_by_partial_text('Sample')
    title_found = browser.find_by_css('h2.title')
    
    sample_dict= {}
    
    #add something in dictionary
    #add the dictionary to the list
    
    
    
    #sample1 = pictures_found[0]
    
    #sample1_href= sample1['href']
   
    
    #how to pull an element from the picture
    
   #print(sample1_href)
    
    
   
    
    browser.back()
  


# In[ ]:




