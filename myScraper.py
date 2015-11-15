"""
This module uses BeautifulSoup 4 and Requests package to scrape Twitter for data, and can be used to bypass the REST API request ceiling set by Twitter

@author ssinhaonline <homepage = "www.datanoobjournals.com/ssinhaonline" email = "ssinhaonline@gmail.com">
@date Nov 6, 2015
"""

def sourceExtractor(url):
    from selenium import webdriver
    from time import sleep
    import datetime
    tminus = datetime.datetime(2015, 11, 14, 23, 10, 00, 000000)
    while(datetime.datetime.now() < tminus):
        pass
    driver = webdriver.Firefox()
    driver.get(url)
    d1 = datetime.datetime.now()
    print 'Start: ' + str(d1)
    lensrc1 = len(driver.page_source)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
    sleep(2)
    lensrc2 = len(driver.page_source)
    d2 = datetime.datetime.now()
    while((lensrc1 < lensrc2) and ((d2 - d1).seconds <= 86399)):
        try:
            lensrc1 = lensrc2
            driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
            sleep(2)
            lensrc2 = len(driver.page_source)
            d2 = datetime.datetime.now()
            try:
                if (d2 - d1).seconds % 3600 == 0:
                    src = driver.page_source
                    f = open('DemDebatesrc_11_14.html', 'w')
                    f.write(src.encode('utf8'))
                    f.close()
                    print 'End: ' + str(d2) + ' Written at ' + str(int((d2 - d1).seconds/3600)) + 'th hour'
            except:
                pass
        except:
            print 'Some error. Exit at ' + str(d2)
            exit
    src = driver.page_source
    driver.close()
    print 'Completely parsed. Exit at ' + str(d2)
    return src

src = sourceExtractor('https://twitter.com/hashtag/demdebate?f=tweets&vertical=news&src=live')
f = open('DemDebatesrc_11_14.html', 'w')
f.write(src.encode('utf8'))
f.close()
