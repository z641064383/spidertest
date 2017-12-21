
import   requests
from lxml  import   etree

def  get_html():
    url='http://www.mm131.com'
    res=requests.get(url).content
    html=etree.HTML(res.decode('gbk'))
    hrefs=html.xpath("//div[@class='nav']/ul/li/a")

    del  hrefs[0]
    return    hrefs

def   get_leixing_urls(url):
    res=requests.get(url).content
    html=etree.HTML(res.decode('gbk'))
    hrefs=html.xpath(u"//div[@class='main']/dl[@class='list-left public-box']/dd/a[@target='_blank']")
    # print  hrefs
    # next_urls=html.xpath("//div[@class='main']//dd[@class="page"]/a")
    # print  next_urls
    return  hrefs

def  get_next_page(url):
    res=requests.get(url).content
    html=etree.HTML(res.decode('gbk'))
    nextpages=html.xpath(u"//div[@class='main']/dl[@class='list-left public-box']/dd[@class='page']//a")
    return  nextpages

def   get_pic_info(url):
    res=requests.get(url).content
    html=etree.HTML(res.decode('gbk'))
    next_pic_info=html.xpath(u'//div[@class="content-page"]/a')
    # next_pic_info=next_pic_info[-1]
    return   next_pic_info


for   href in  get_html():

    urls=href.attrib['href']
    name=href.text
    print  urls
    for  leixingurls  in   get_leixing_urls(urls):
        leixingurl=leixingurls.attrib['href']
        leixingname=leixingurls.xpath('string(.)')
        print   leixingurl,leixingname
        pic_info=get_pic_info(leixingurl)
        pic_info_url=pic_info[-2].get('href')
        qiepian=pic_info_url.split('.')[0]
        en=qiepian.split('_')[-1]

        # pic_pingjie_url=''.join(leixingurl.split('.') +'.html')
        # print  pic_info_url ,qiepian ,pic_pingjie_url
    break
                        

    next_page_url=get_next_page(urls)[-1].get('href')
    print  next_page_url
    num=next_page_url.split('.')[0].split('_')
    number=num[-1]
    next_page_url="".join(leixingurl+"/"+next_page_url)
    pingjieurl=''.join(num[0]+'_'+num[1]+'_')
    print   next_page_url,pingjieurl,number
    i=2
    while  i<int(number)+1:
        pingjieurl_new=''.join(pingjieurl+str(i)+'.html')
        i=i+1
        pingjieurl_new=''.join(urls+pingjieurl_new)
        print   pingjieurl_new
        for  leixingurls  in   get_leixing_urls(pingjieurl_new):

            leixingurl=leixingurls.attrib['href']        

            leixingname=leixingurls.xpath('string(.)')

            print   leixingurl,leixingname
            get_pic_info(leixingurl)
    break




