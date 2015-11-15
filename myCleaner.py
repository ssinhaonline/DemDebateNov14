from bs4 import BeautifulSoup
import re
import pdb

srcTxt = open('DemDebatesrc_11_14.html', 'r').read()

soup = BeautifulSoup(srcTxt)
tempstreamholder = soup.find('ol', {'id': 'stream-items-id'}).find_all('li', {'data-item-type': 'tweet'})
tweetdivs = []
for item in tempstreamholder:
    tweetdivs.append(item.find('div', {'class':'tweet'}))
#print tweetdivs[0].prettify()
tweetlist = []
#pdb.set_trace()
pos = -1
f = open('debug_log.txt', 'w')
data = open('DemDebatedata2.csv', 'w')
for item in tweetdivs:
    pos += 1
    try:
        uname = item['data-screen-name']
        time = item.find('a', {'class': 'tweet-timestamp'})['title']
        content = item.find('div', {'class': 'content'}).find('p', {'class': 'tweet-text'}).text.replace('\n', ' ').replace('"', '')
        tweetlist.append({'user' : uname, 'time': time, 'content' : content})
        try:
            '''if pos % 100 == 0:
                ent = raw_input("Press enter to continue: ")
            print uname'''
            data.write(uname + '|' + time + '|' + content + '\n')
        except:
            print 'Data write unsuccessful at: ' + int(pos)
            print uname + '|' + time + '|' + content + '\n'
    except:
        f.write('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n')
        f.write('Skipped item:' + str(pos) + '\n')
        f.write(str(tempstreamholder[pos]) +  '\n')
        pass
data.close()
