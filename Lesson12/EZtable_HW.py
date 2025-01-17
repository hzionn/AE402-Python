from bs4 import BeautifulSoup
from selenium import webdriver
#記得import
from selenium.webdriver.chrome.options import Options
import time

#隱藏瀏覽器
chrome_options = Options()
chrome_options.add_argument('--headless')
userAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
chrome_options.add_argument('--user-agent={}.format(userAgent)')
chrome = webdriver.Chrome(options=chrome_options)

# 使用隱藏瀏覽器就不用加上第15行開啟瀏覽器
# chrome = webdriver.Chrome()
chrome.get('https://tw.eztable.com/search')
time.sleep(1)

for i in range(8):
	chrome.execute_script('window.scrollTo(0,document.body.scrollHeight);')
	time.sleep(1)

time.sleep(3)
soup = BeautifulSoup(chrome.page_source, 'html.parser')
# 使用隱藏瀏覽器就不用加上第26行關閉瀏覽器
# chrome.close()


for index, div in enumerate(soup.find_all('div', class_ = 'SearchResult__StyledRestaurantContent-alt2vy-4 ydffj')):
	name = div.find('a').text
	try:
		price = div.find('div', class_ = 'SearchResult__StyledPrice-alt2vy-13 ghERpV').text
	except:
		price = None
	
	print(index+1, name, price)
	if index+1 == 100:
		break
