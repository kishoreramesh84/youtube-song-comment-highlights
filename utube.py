from selenium import webdriver
import sys
import numpy as np
from PIL import Image
import time
from wordcloud import wordcloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
driver=webdriver.Chrome()
driver.get('https://www.youtube.com/watch?v=9eX-HRFwCnU')
driver.execute_script('window.scrollTo(1, 500);')
#now wait let load the comments
time.sleep(10)
driver.execute_script('window.scrollTo(1, 3000);')
comment_div=driver.find_element_by_xpath('//*[@id="contents"]')
comments=comment_div.find_elements_by_xpath('//*[@id="content-text"]')
mimg=np.array(Image.open("C:/Users/Sony/Downloads/images (1).jpg"))
mcolour=ImageColorGenerator(mimg)
text="".join(r.text for r in comments)
wordcloud1 =wordcloud.WordCloud(stopwords=set(STOPWORDS),background_color="white",mask=mimg,contour_width=2,contour_color='yellow',max_font_size=40)
wordcloud1.generate(text)
plt.figure(figsize=(10,10))
plt.imshow(wordcloud1.recolor(color_func=mcolour), interpolation='bilinear')
plt.axis("off")
plt.show()
