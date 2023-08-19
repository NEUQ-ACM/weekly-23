import requests
import threading
import time
import os

def lesson(classid, cid):
    n = 0
    while (1 > 0):
        sid = '04368FC68114D2AF65413C6C327EEF86'#'D025374553894D51C7503E4684A3425E'
        url = 'http://jwxt.neuq.edu.cn/eams/stdElectCourse!batchOperator.action?profileId='+cid
        cookie = 'JSESSIONID=' + sid + ';GSESSIONID=' + sid + ';'
        cookie = 'semester.id=81; JSESSIONID=' + sid + '; SERVERNAME=c1; GSESSIONID=' + sid
        header = {
            #'Host': 'jwxt.neuq.edu.cn',
            #'Connection': 'keep-alive',
            #'Content-Length': '83',
            #'Accept': 'text/html, */*; q=0.01',
            #'X-Requested-With': 'XMLHttpRequest',
            'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.188',
            #'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            #'Origin': 'http://jwxt.neuq.edu.cn',
            'Referer':
            'http://jwxt.neuq.edu.cn/eams/stdElectCourse!defaultPage.action?electionProfile.id='+cid,
            #'Accept-Encoding': 'gzip, deflate',
            #'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cookie': cookie
        }
        data = {
            'optype': 'true',
            'operator0': classid + ':true:0',
            'lesson0': classid,
            'schLessonGroup_' + str(classid): 'undefined'
        }

        mes = requests.post(url, headers=header, data=data)
        f = open("res.html", "w")
        # res = str(mes.content, 'utf-8')
        # print(res)
        f.write(str(mes.content, 'utf-8'))
        os.startfile(r'res.html')

        print(classid+"成功")
        time.sleep(3)


thread1 = threading.Thread(target=lesson, args=('58512', '281',))
thread1.start()
time.sleep(0.75)
thread2 = threading.Thread(target=lesson, args=('58603', '284',))
thread2.start()
time.sleep(0.75)
thread3 = threading.Thread(target=lesson, args=('58832', '285',))
thread3.start()
time.sleep(0.75)
thread4 = threading.Thread(target=lesson, args=('59589', '283',))
thread4.start()


def main():
    while (1 > 0):
        i = 1
    #  lesson('58512')
    #   t=  threading.Thread(target=lesson,args=('58516'))
    #   t.start()

#     threading.Thread(target=lesson,args=('58516'))
#     threading.Thread(target=lesson,args=('58516'))
main()
