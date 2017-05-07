#http://comic.naver.com/search.nhn?keyword=%EC%9D%B4%EB%B3%84%EB%A7%8C%ED%99%94
#이별만화 완성도
#http://comic.naver.com/webtoon/list.nhn?titleId=654333
import requests,time
from apscheduler.scheduler import Scheduler #For cron

cron = Scheduler(daemon=True)
cron.start()

webtoon_list_page = "http://comic.naver.com/webtoon/list.nhn?titleId="


def up_check():
	titleId = 644180
	#하루 3컷 -> titleId=644180
	#http://comic.naver.com/webtoon/list.nhn?titleId=654333
	#페이지에 들어갔을때 up 표시가 있으면? -> 업데이트가 된 것이다~
	r = requests.get(webtoon_list_page+str(titleId))
	#Up 표시는
	#src="http://static.naver.net/comic/images/2012/ico_toonup.png" 이다
	#<img src="http://static.naver.net/comic/images/2012/ico_toonup.png" width="27" height="15" alt="UP">
	#alt="UP"이 가장 확실한듯 src는 바뀔 수도 있으니깐
	#즉 페이지 소스에 저 문자열이 있는지 확인해서 있으면 업뎃이 된 것이다~
	if r.text.find('alt="UP"')!=-1:
		#r2 = requests.get(webtoon_detail_page+str(titleId))
		print('webtoon_is_up')
		#do something

cron.add_cron_job(up_check,second="*/10")
#cron에 argument넣는거도 잇음 나중에 찾아바

#업뎃이 되었으면 거기 페이지로 들어가게 하고 싶다.
webtoon_detail_page = "http://comic.naver.com/webtoon/detail.nhn?titleId="
#방법 1
#<a href="/webtoon/detail.nhn?titleId=644180&no=862&weekday=thu" onclick="clickcr(this,'lst.title','644180','862',event)">170508(월) - 등가교환</a>
#							<img src="http://static.naver.net/comic/images/2012/ico_toonup.png" width="27" height="15" alt="UP">
#로 가게 한다.
#같은 <td class="title"> 안에 있는 것으로 보아서 import json해서 파싱을 할 수 있었던 거 같다. 헷

#방법 2
#http://comic.naver.com/webtoon/detail.nhn?titleId=644180&no=862인데,
#no>862로 만들면, 예를 들어 9999로 만들면 자동으로 최신화로 가진다. 아니 걍 no에 아무것도 입력안하면 자동으로 최신화로 가진다...???
def main():
	time.sleep(20000)

###########
#지금까지 썼던 것들을 cron으로 감싼다 -> 1분 간격으로 돌리기 위해. 설마 밴먹나?
if __name__ == "__main__":
    main()
