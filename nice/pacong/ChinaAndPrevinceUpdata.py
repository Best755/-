import time
import json
import csv
import requests
import random
import numpy
import pymysql
#ExcelName = 'C:/Users/Administrator/Desktop/新建文件夹 (5)/445.csv'

#当前日期时间戳
number = format(time.time() * 100, '.0f')
user_agents = [
            "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
            "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
            "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0",
            "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; InfoPath.3; rv:11.0) like Gecko",
            "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)",
            "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
            "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
            "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
            "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
            "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
            "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
            "Mozilla/5.0 (iPod; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
            "Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
            "Mozilla/5.0 (Linux; U; Android 2.3.7; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
            "MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
            "Opera/9.80 (Android 2.3.4; Linux; Opera Mobi/build-1107180945; U; en-GB) Presto/2.8.149 Version/11.10",
            "Mozilla/5.0 (Linux; U; Android 3.0; en-us; Xoom Build/HRI39) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13",
            "Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en) AppleWebKit/534.1+ (KHTML, like Gecko) Version/6.0.0.337 Mobile Safari/534.1+",
            "Mozilla/5.0 (hp-tablet; Linux; hpwOS/3.0.0; U; en-US) AppleWebKit/534.6 (KHTML, like Gecko) wOSBrowser/233.70 Safari/534.6 TouchPad/1.0",
            "Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaN97-1/20.0.019; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/525 (KHTML, like Gecko) BrowserNG/7.1.18124",
            "Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0; HTC; Titan)",
            "UCWEB7.0.2.37/28/999",
            "NOKIA5700/ UCWEB7.0.2.37/28/999",
            "Openwave/ UCWEB7.0.2.37/28/999",
            "Mozilla/4.0 (compatible; MSIE 6.0; ) Opera/UCWEB7.0.2.37/28/999",
            "Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25",
        ]
headers={"User-Agent":random.choice(user_agents)}

url = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5&callback=&_=%s' % number
datas = json.loads(requests.get(url=url,headers=headers).json()['data'])

print('更新时间：' + datas['lastUpdateTime'])
tmds = datas['lastUpdateTime']
tmds=tmds[0:-9]
print(tmds)
sheng = []
city1 = []
new = []
now = []
death = []
cure = []
summ = []


#写入表头
#with open(ExcelName, 'w', encoding='utf-8', newline='') as csvfile:
    #writer = csv.writer(csvfile)
    #writer.writerow(["省份","城市","新增","确诊","现有","死亡","治愈","时间"])
conn = pymysql.connect(host="121.41.228.236", user="root",password="0000",database="nice",charset="utf8")
cursor = conn.cursor()  
#sql1 = "truncate table App_province"
#cursor.execute(sql1)
#conn.commit()
for contry in datas['areaTree']:
    if contry['name'] == '中国':
        for province in contry['children']:
            sun_new = 0
            sun_sum = 0
            sun_cure = 0
            sun_death = 0
            sun_now = 0
            for city in province['children']:
                province_name = province['name']
                #with open(ExcelName, 'a', encoding='utf-8', newline='') as csvfile:
                    #writer = csv.writer(csvfile)
                    #now = 1
                    #writer.writerow([province['name'],city['name'], str(city['today']['confirm']),str(city['total']['confirm']),str(city['total']['confirm']-city['total']['dead']-city['total']['heal']),str(city['total']['dead']), str(city['total']['heal']),tmds])
                sun_new = sun_new + city['today']['confirm']
                sun_now = sun_now + (city['total']['confirm']-city['total']['dead']-city['total']['heal'])
                sun_cure = sun_cure + city['total']['heal']
                sun_death = sun_death + city['total']['dead']
                sun_sum = sun_sum + city['total']['confirm']
                #各个省市
                #sheng.append(province['name'])
                #city1.append(str(city['name']))
                #times.append(tmds)
                #death.append(city['total']['dead'])
                #new.append(city['today']['confirm'])
                #now.append(city['total']['confirm']-city['total']['dead']-city['total']['heal'])
                #cure.append(city['total']['heal'])
                #summ.append(city['total']['confirm'])
                #插入province表
                if  str(city['name'])=="地区待确认":
                    continue
                
                sql2 = "INSERT INTO App_province(date,add_new,sum_definite,sum_suspected,sum_cure,sum_die,province_name,city_name) \
                        VALUES ('%s','%s' , %s ,  %s,  %s,  %s,'%s','%s')"\
                            %(str(tmds),city['today']['confirm'],city['total']['confirm'],city['total']['confirm']-city['total']['dead']-city['total']['heal'],\
                                city['total']['heal'],city['total']['dead'],province['name'],str(city['name']))
                cursor.execute(sql2)
                conn.commit()
            #插入china表
            #sql3 = "INSERT INTO App_province(date,province_name,add_new,sum_definite,sum_suspected,sum_cure,sum_die) \
            #            VALUES ('%s','%s' , %s ,  %s,  %s,  %s,'%s')"\
            #                %(str(tmds),str(province_name),sun_new,sun_sum,\
            #                    sun_now,sun_cure,sun_death)
            #cursor.execute(sql3)
            #conn.commit()
print("finsh")
cursor.close()
conn.close()
