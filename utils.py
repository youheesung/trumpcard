import urllib.request
import xml.etree.ElementTree as etree
from search.models import Play
from search.models import Theater

url = 'http://www.kopis.or.kr/openApi/restful/prfplc?service=2bb0854b244b4b6e853de44c0a34cc16&cpage=1&rows=2000'

data = urllib.request.urlopen(url).read()

filename = 'theater.xml'
f = open(filename, "wb")
f.write(data)
f.close()

tree = etree.parse(filename)
root = tree.getroot()
str = 'http://kopis.or.kr/openApi/restful/prfplc/{0}?service=2bb0854b244b4b6e853de44c0a34cc16'
for a in root.findall('db'):
    url = str.format(a.findtext('mt10id'))
    data = urllib.request.urlopen(url).read()
    file = 'theater_detail.xml'
    f = open(file, "wb")
    f.write(data)
    f.close()
    tr = etree.parse(file)
    roo = tr.getroot()
    b = roo.find('db')
    if 'http' in b.findtext('lo'):
        print('%s 위도 설정 필요!!!' % b.findtext('fcltynm'))
        Theater.objects.create(placeid=b.findtext('mt10id'),name=b.findtext('fcltynm'),theater_count=b.findtext('mt13cnt'),tel=b.findtext('telno'),page=b.findtext('relatedurl'),address=b.findtext('adres'),latitude=b.findtext('la'),longitude=0)
    else:
        print('good')
        Theater.objects.create(placeid=b.findtext('mt10id'),name=b.findtext('fcltynm'),theater_count=b.findtext('mt13cnt'),tel=b.findtext('telno'),page=b.findtext('relatedurl'),address=b.findtext('adres'),latitude=b.findtext('la'),longitude=b.findtext('lo'))