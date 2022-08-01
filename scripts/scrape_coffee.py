#%%
#  import libraries

from time import sleep
from bs4 import BeautifulSoup
from time import sleep
from random import randint
#from tqdm.auto import tqdm

import requests
import pandas as pd
import matplotlib.pyplot as plt


#create url
url='https://www.coffeereview.com/advanced-search/?keyword=&search=Search+Now&score_all=on&score_96_100=on&score_93_95=on&score_90_92=on&score_85_89=on&score_85=on&roast_all=on&roast_light=on&roast_medium_light=on&roast_medium=on&roast_medium_dark=on&roast_dark=on&type_all=on&type_espresso=on&type_organic=on&type_fair_trade=on&type_decaffeinated=on&type_best_value=on&type_pod_capsule=on&type_blend=on&type_estate=on&type_peaberry=on&type_barrel_aged=on&type_aged=on&region_all=on&region_africa_arabia=on&region_caribbean=on&region_central_america=on&region_hawaii=on&region_asia_pacific=on&region_south_america=on&tree_variety_all=on&tree_variety_geisha=on&tree_variety_bourbon=on&tree_variety_catuai=on&tree_variety_caturra=on&tree_variety_maragogipe=on&tree_variety_maracaturra=on&tree_variety_mocca-moka=on&tree_variety_pacamara=on&tree_variety_robusta=on&tree_variety_sl-28-sl-34=on&tree_variety_typica=on&process_method_all=on&process_method_anaerobic-experimental=on&process_method_honey-pulped-natural=on&process_method_natural-dry=on&process_method_washed-wet=on&process_method_washed-wet-hulled=on&pg=97'
headers= {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36'}

#get request
response= requests.get(url, headers=headers)
response.status_code
print(response.content.decode())

#parse html
soup=BeautifulSoup(response.content,'html.parser')
soup.prettify()

#html code
productlist = soup.find_all('div', class_='column col-1')
print(productlist)

#function for link extract

productlinks = []

for x in range(1,3):
    response= requests.get(f'https://www.coffeereview.com/advanced-search/?keyword=&search=Search+Now&score_all=on&score_96_100=on&score_93_95=on&score_90_92=on&score_85_89=on&score_85=on&roast_all=on&roast_light=on&roast_medium_light=on&roast_medium=on&roast_medium_dark=on&roast_dark=on&type_all=on&type_espresso=on&type_organic=on&type_fair_trade=on&type_decaffeinated=on&type_best_value=on&type_pod_capsule=on&type_blend=on&type_estate=on&type_peaberry=on&type_barrel_aged=on&type_aged=on&region_all=on&region_africa_arabia=on&region_caribbean=on&region_central_america=on&region_hawaii=on&region_asia_pacific=on&region_south_america=on&tree_variety_all=on&tree_variety_geisha=on&tree_variety_bourbon=on&tree_variety_catuai=on&tree_variety_caturra=on&tree_variety_maragogipe=on&tree_variety_maracaturra=on&tree_variety_mocca-moka=on&tree_variety_pacamara=on&tree_variety_robusta=on&tree_variety_sl-28-sl-34=on&tree_variety_typica=on&process_method_all=on&process_method_anaerobic-experimental=on&process_method_honey-pulped-natural=on&process_method_natural-dry=on&process_method_washed-wet=on&process_method_washed-wet-hulled=on&pg={x}', headers=headers)
    soup=BeautifulSoup(response.content,'html.parser')
    productlist = soup.find_all('div', class_='column col-1')
    for item in (productlist):
        for link in item.find_all('a', href=True):
            productlinks.append(link['href'])
            wait_time=randint(1,2)
            print("I will sleep now for..."+str(wait_time)+"secs")
            sleep(wait_time)
    print(productlinks)
#

# scrape function
import random
df_total=pd.DataFrame()
for link in productlinks: 

    response= requests.get(link, headers=headers)
    soup=BeautifulSoup(response.content,'html.parser')
    name = soup.find('h1', class_='review-title').text.strip()
    roaster = soup.find('p', class_='review-roaster').text.strip()
    rating = soup.find('span', class_='review-template-rating').text.strip()
    feature= soup.find('div', class_='row row-2')
    values = [tr.find_all('td')[1].get_text() for tr in feature.find_all('tr')]
    keys = [tr.find_all('td')[0].get_text().rstrip(":") for tr in feature.find_all('tr')]
    keys.extend(['name','roaster','rating'])
    values.extend([name, roaster, rating])
    temp_row = {k:v for k, v in zip(keys, values)}
    df_total = pd.concat([df_total,pd.DataFrame(temp_row, index=[0])], axis = 0)
    

    wait_time=random.uniform(0.5,1.5)
    print("I will sleep now for..."+str(wait_time)+"secs")
    sleep(wait_time)
    
df_total = df_total.reset_index(drop=True)
#dataframe
df_total
# %%
