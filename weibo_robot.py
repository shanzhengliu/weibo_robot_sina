from requestium import *
from requestium import Session, Keys


def login_Getcookie(myaccount,mypassword):#webdriver_option来确定是否使用浏览器显示或者静默登陆
    rq = Session(webdriver_path='C:\Program Files (x86)\Google\Chrome\Application\chromedriver',
                browser='chrome',
                default_timeout=15,
                #webdriver_options={'arguments': ['headless']}
                 )
    rq.driver.get("https://passport.weibo.cn/signin/login")


    inputname = rq.driver.find_element("xpath",'//*[@id="loginName"]')
    password = rq.driver.find_element_by_xpath('//*[@id="loginPassword"]')
    login_button = rq.driver.find_element_by_xpath('//*[@id="loginAction"]')
    rq.driver.implicitly_wait(10)
    inputname.send_keys(myaccount)
    password.send_keys(mypassword)
    login_button.click()
    rq.driver.implicitly_wait(15)
    # ver_button = rq.driver.find_element_by_xpath('//*[@id="embed-captcha"]/div/div[2]/div[1]/div[3]')
    # ver_button.click()
    #验证码不知道啥时候会有，反正登陆几次把
    rq.transfer_driver_cookies_to_session()
    return rq

rq = login_Getcookie("youraccount","yourpassword")#这里输入你的账号密码
data= rq.get("https://s.weibo.com/top/summary?Refer=top_hot&topnav=1&wvr=6").xpath('//*[@id="pl_top_realtimehot"]/table/tbody/tr/td[2]')
list = []
#热搜爬取
for i in data:
    print(i.xpath('a/text()').extract())
    list.append("https://s.weibo.com/"+i.xpath('a/@href').extract()[0])


rq.driver.get(list[0])#之后操作自己搞把


