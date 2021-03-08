import bs4
import requests

url = 'https://id.carousell.com/carousell_id/'
contents = requests.get(url)
#print(contents.text)

response = bs4.BeautifulSoup(contents.text, 'html.parser')
#print(response)

data = response.find_all('div','D_afo D_aS M_hs D_aU M_hu')
print(data[0].text)




