url1='''https://cau.commonscdn.com/contents8/cau1000001/##/contents/media_files/mobile/ssmovie.mp4'''
url2='''https://cau.commonscdn.com/contents11/cau1000001/##/contents/media_files/mobile/ssmovie.mp4'''
from threading import Thread
import requests
def work(id, start, end, result):
    total = 0
    for i in range(start, end):
        s = hex(i)
        token = '%11s' % s[2:]
        token = token.replace(" ", "0")
        url='''https://cau.commonscdn.com/contents8/cau1000001/5e'''+token+'''/contents/media_files/mobile/ssmovie.mp4'''
        print(url+":",end='')
        response=requests.get(url)
        print(response.status_code)
    return


if __name__ == "__main__":
    START, END = 1099511627776, 17592186044415
    result = list()
    th1 = Thread(target=work, args=(1, START, END // 4, result))
    th2 = Thread(target=work, args=(2, END // 4, END // 2, result))
    th3 = Thread(target=work, args=(3, END // 2, (END // 4 )* 3, result))
    th4 = Thread(target=work, args=(4, (END // 4 )* 3, END, result))
    th1.start()
    th2.start()
    th3.start()
    th4.start()
    th1.join()
    th2.join()
    th3.join()
    th4.join()