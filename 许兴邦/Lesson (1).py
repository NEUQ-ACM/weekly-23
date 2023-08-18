import os
import requests
import threading
import time


def lesson(profid, classid, sname):
    sid = '8D6E46A6EC745D79C9F7646243311743'
    url = 'http://jwxt.neuq.edu.cn/eams/stdElectCourse!batchOperator.action?profileId=' + profid
    cookie = 'semester.id=81;JSESSIONID=' + sid + ';GSESSIONID=' + sid + ';' + 'SERVERNAME=' + sname
    header = {
        'Host':
        'jwxt.neuq.edu.cn',
        'Connection':
        'keep-alive',
        'Content-Length':
        '83',
        'Accept':
        'text/html, */*; q=0.01',
        'X-Requested-With':
        'XMLHttpRequest',
        #'SERVERNAME' : 'c1',
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.188',
        'Content-Type':
        'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin':
        'http://jwxt.neuq.edu.cn',
        'Referer':
        'http://jwxt.neuq.edu.cn/eams/stdElectCourse!defaultPage.action?electionProfile.id='
        + profid,
        'Accept-Encoding':
        'gzip, deflate',
        'Accept-Language':
        'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Cookie':
        cookie
    }
    data = {
        'optype': 'true',
        'operator0': classid + ':true:0',
        'lesson0': classid,
        'schLessonGroup_' + str(classid): 'undefined'
    }
    while (1 < 2):
        mes = requests.post(url, headers=header, data=data)
        f = open("res.html", "w")
        res1 = str(mes.content, 'utf-8')
        print(res1)
        if '权' in res1:
            print(classid + '成功')
            f.write(str(mes.content, 'utf-8'))
            # os.startfile(r'res.html')
            break
        elif '开放' in res1:
            print(classid + '未开放')
            time.sleep(3)
        else:
            print(classid + '失败')
            time.sleep(3)


def main():
    t1 = threading.Thread(target=lesson, args=('281', '58512', 'c3'))
    t2 = threading.Thread(target=lesson, args=('284', '58603', 'c3'))
    t3 = threading.Thread(target=lesson, args=('285', '58832', 'c3'))
    t4 = threading.Thread(target=lesson, args=('283', '59589', 'c3'))
    t1.start()
    time.sleep(0.8)
    t2.start()
    time.sleep(0.8)
    t3.start()
    time.sleep(0.8)
    t4.start()


main()
