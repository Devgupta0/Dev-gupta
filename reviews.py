import requests  # request framework are use for extract data  from url

from bs4 import BeautifulSoup  # beautifulsoup frame work are used for cleaning html tags 

import pandas as pd  # pandas is library that are used to represent data in a effective way like tabular format
from pandas import ExcelWriter # excel writer are used for converting data in excel file format

review_dict = {'name':[], 'date':[], 'rating':[], 'review':[]}  # initializing a dictionary

for page in range(0,23):  #  describe a page range
    url = 'https://www.metacritic.com/game/switch/pokemon-sword/user-reviews?page='+str(page) # extracting data save in url
    user_agent = {'User-agent': 'Mozilla/5.0'}
    response  = requests.get(url, headers = user_agent) # I use requests to get data from url 
    
    soup = BeautifulSoup(response.text, 'html.parser')  # Using beautifulSoup for cleaning html tag
    
    for review in soup.find_all('div', class_='review_content'): # using for loop to get reviews content using div and class  
        if review.find('div', class_='name') == None:   # then initialise if condition  if class'name' is none
                       break               # when class is none it will break and come out from the loop
        review_dict['name'].append(review.find('div', class_='name').find('a').text)# then we finding name using div and class
        review_dict['date'].append(review.find('div', class_='date').text)# then finding data using class name :date
        review_dict['rating'].append(review.find('div', class_='review_grade').find_all('div')[0].text)# then find rating
        if review.find('span', class_='blurb blurb_expanded'): # then finding the actual reviews from span and class
            review_dict['review'].append(review.find('span', class_='blurb blurb_expanded').text)# then append in review_dict
        else:
            review_dict['review'].append(review.find('div', class_='review_body').find('span').text)# when review not find in 
            # class then we find review in span

df = pd.DataFrame(review_dict)   # then making a dataframe to provide data in a structure format 
k=ExcelWriter("C:/Users/Dell/Desktop/reviews.xlsx") # using excel writer to save data in excel file
df.to_excel(k,'sheet',index=False)  
k.save()
