import requests
import json
import pymysql
from datetime import datetime
import time
import random
import numpy
import re

class downdata:
    def __init__(self):
        self.url1 = "https://voice.baidu.com/newpneumonia/get?target=trend&isCaseIn=1&stage=publish"
        self.url2 = "https://voice.baidu.com/newpneumonia/get?target=trend&isCaseIn=0&stage=publish"
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
        self.headers={"User-Agent":random.choice(user_agents)
        }
    def get_url(self,url):
        data = requests.get(url=url,headers=self.headers)
        data1 = data.content.decode("utf-8")
        return data1
    def deal_with_foreign(self,basedata):
        r = json.loads(basedata)
        names = []
        confirmeds = []
        cures = []
        deaths = []
        The_new_diagnosiss = []
        timedatas = []
        timedata1s = []
        #每日世界总计
        sumworldconfirmed = {}
        #累计确诊
        sumworldcure = {}
        #累计治愈
        sumworlddeath = {}
        #累计死亡
        sumworldThe_new_diagnosis = {}
        #新增
        dic = {}
        for each1 in range(len(r["data"])):
            timedata1 = r["data"][each1]["trend"]["updateDate"]
            timedata1s = list(set(timedata1s+timedata1))
        timedata1s.sort()
        timedata2s = timedata1s[0:-7]
        #print(timedata2s)
        #conn = pymysql.connect(host="121.41.228.236", user="root",password="0000",database="nice",charset="utf8")
        #cursor = conn.cursor()
        #cursor.execute("DROP TABLE IF EXISTS foregin")
        #sql = """"""
        for each1 in range(len(r["data"])):
            name = r["data"][each1]["name"]
            names.append(name)
            timedata = r["data"][each1]["trend"]["updateDate"]
            timedatas = list(set(timedatas+timedata))
            confirmed = r["data"][each1]["trend"]["list"][0]["data"]
            confirmeds.append(confirmed)
            cure = r["data"][each1]["trend"]["list"][1]["data"]
            cures.append(cure)
            death = r["data"][each1]["trend"]["list"][2]["data"]
            deaths.append(death)
            The_new_diagnosis = r["data"][each1]["trend"]["list"][3]["data"]
            The_new_diagnosiss.append(The_new_diagnosis)
            #everyday是每天的数据日期为键 数据为值
            everydayconfirmed = dict(zip(timedata,confirmed))
            everydaycure = dict(zip(timedata,cure))
            everydaydeath = dict(zip(timedata,death))
            everydayThe_new_diagnosis = dict(zip(timedata,The_new_diagnosis))
            #sumworld是国外每天的总数
            #for key,value in everydayconfirmed.items():
                #if key in sumworldconfirmed:
                    #sumworldconfirmed[key] += value
                #else:
                    #sumworldconfirmed[key] = value
            #for key,value in everydaycure.items():
                #if key in sumworldcure:
                    #sumworldcure[key] += value
                #else:
                    #sumworldcure[key] = value
            #for key,value in everydaydeath.items():
                #if key in sumworlddeath:
                    #sumworlddeath[key] += value
                #else:
                    #sumworlddeath[key] = value
            #for key,value in everydayThe_new_diagnosis.items():
                #if key in sumworldThe_new_diagnosis:
                    #sumworldThe_new_diagnosis[key] += value
                #else:
                    #sumworldThe_new_diagnosis[key] = value
        #print(sumworlddeath)
        #print(sumworldcure)
        #print(sumworldconfirmed)
        #print(sumworldThe_new_diagnosis)
        #cursor.close()
        #conn.close()
    def deal_with_chinacity(self,basedata):
        r = json.loads(basedata)
        names = []
        #全国每天的详细数据
        confirmeds = []
        cures = []
        deaths = []
        The_new_diagnosiss = []
        #新增
        timedatas = []
        timedata1s = []
        #sumchina是全国每天的总数
        sumchinaconfirmed = {}
        #累计确诊
        sumchinacure = {}
        #累计治愈
        sumchinadeath = {}
        #累计死亡
        sumchinaThe_new_diagnosis = {}
        #新增
        for each in range(len(r["data"])):
            timedata1 = r["data"][each]["trend"]["updateDate"]
            timedata1s = list(set(timedata1s+timedata1))
        timedata1s.sort()
        timedata2s = timedata1s[0:-7]
        #print(timedata2s)
        conn = pymysql.connect(host="121.41.228.236", user="root",password="000000",database="nice",charset="utf8")
        cursor = conn.cursor()
        sql = "truncate table App_china;"
        cursor.execute(sql)
        conn.commit()
        j = 0
        idd = 0 
        idds = []
        for each in range(len(r["data"])):
            name = r["data"][each]["name"]
            names.append(name)
            timedata = r["data"][each]["trend"]["updateDate"]
            pname = []
            for i in range(len(timedata)):
                pname.append(name)

            timedatas = list(set(timedatas+timedata))
            confirmed = r["data"][each]["trend"]["list"][0]["data"]
            #sumchina = numpy.array(sumchina1)
            #confirmed1 = numpy.array(confirmed)
            #sumchina1 = sumchina + confirmed1
            confirmeds.append(confirmed)
            cure = r["data"][each]["trend"]["list"][1]["data"]
            cures.append(cure)
            death = r["data"][each]["trend"]["list"][2]["data"]
            deaths.append(death)
            The_new_diagnosis = r["data"][each]["trend"]["list"][3]["data"]
            The_new_diagnosiss.append(The_new_diagnosis)
            #everyday是每天的数据日期为键 数据为值
            everydayconfirmed = dict(zip(timedata,confirmed))
            everydaycure = dict(zip(timedata,cure))
            everydaydeath = dict(zip(timedata,death))
            everydayThe_new_diagnosis = dict(zip(timedata,The_new_diagnosis))
            #sumchina是全国每天的总数
            #for key,value in everydayconfirmed.items():
               #if key in sumchinaconfirmed:
                    #sumchinaconfirmed[key] += value
                #else:
                    #sumchinaconfirmed[key] = value
            #for key,value in everydaycure.items():
                #if key in sumchinacure:
                    #sumchinacure[key] += value
                #else:
                    #sumchinacure[key] = value
            #for key,value in everydaydeath.items():
                #if key in sumchinadeath:
                    #sumchinadeath[key] += value
                #else:
                    #sumchinadeath[key] = valuei
            datestrs = []
            for i in range(len(timedata)):
                pattern = r'[.]'                      # 定义分隔符
                url = str(timedata[i]) # 需要拆分的字符串
                result = re.split(pattern, url) # 以pattern的值 分割字符串
                tmds = "2020-"+result[0]+"-"+result[1]
    # 字符串->time
                #datestr = time.strptime(tmds, "%Y-%m-%d")
                datestrs.append(tmds)
            print(datestrs)
            #for key,value in everydayThe_new_diagnosis.items():
                #if key in sumchinaThe_new_diagnosis:
                    #sumchinaThe_new_diagnosis[key] += value
                #else:
                    #sumchinaThe_new_diagnosis[key] = value
            j=j+each
            v = list(map(lambda x: x[0]-x[1], zip(confirmed, cure)))
            now = list(map(lambda x: x[0]-x[1], zip(v, death)))
            for i in range(len(timedata)):
                j = j + i
                idds.append(j)
                sql2 = "INSERT INTO App_china(id,date,add_new,sum_definite,sum_suspected,sum_cure,sum_die,province_name) \
                    VALUES (%s,str_to_date(\'%s\','%%Y-%%m-%%d'),%s , %s ,  %s,  %s,  %s ,' %s')"%(idds[i],datestrs[i],The_new_diagnosis[i],confirmed[i],now[i],cure[i],death[i],pname[i])
    # 执行sql语句
                cursor.execute(sql2)
                conn.commit()
                print("ok")
    # 提交到数据库执行
            #    except:
    # Rollback in case there is any error
            #       print("wrong")
            #       conn.rollback()
        #print(sumchinacure)
        #print(sumchinaconfirmed)
        #print(sumchinaThe_new_diagnosis)
        cursor.close()
        conn.close()
        print("finish")
            
            
    def foreign_run(self):
        base_data1 = self.get_url(self.url1)
        dealwith = self.deal_with_foreign(base_data1)
    def chinacity_run(self):
        base_data2 = self.get_url(self.url2)
        dealwith1 = self.deal_with_chinacity(base_data2)

localtime = time.localtime(time.time())
def timer(n):
    while True:
            yunxing = downdata()
            yunxing.foreign_run()
            yunxing.chinacity_run()
            time.sleep(n)
# 
timer(43200)
