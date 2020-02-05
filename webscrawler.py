from pyquery import PyQuery as pq
import requests
response = requests.get("https://movies.yahoo.com.tw/movie_thisweek.html")
doc = pq(response.text)
movie_names = doc(".release_info .release_movie_name>.gabtn").text()  #抓下本週電影名稱
movie_levels = doc(".levelbox").text()   #抓下本週電影期待度
movie_namesList = movie_names.split()    #整理本週電影名稱做成清單
movie_namesList1 = []
for j in movie_namesList:
    if j == '電影版':
        continue
    else:
        movie_namesList1.append(j)

movie_expectScore = movie_levels.split()[1::5]  #整理本週電影期待度做成清單
movie_expectPoint = []
for m in movie_expectScore:
    mm = m.replace("%","")
    int(mm)
    movie_expectPoint.append(mm)
    
movie_timetables = []  #抓下電影時刻表的網址連結
for movie_timetable in doc(".release_btn.color_btnbox .btn_s_time.gabtn").items("a"):
    movie_timetables.append(movie_timetable.attr("href"))
    
movie_expectList = {}  #把電影名稱跟期待度做成對應字典
for x in range(len(movie_namesList1)):
    movie_expectList[movie_namesList1[x]] = movie_expectPoint[x]
    
movie_timetableList = {}  #把電影名稱跟時刻表網址做成對應字典
for z in range(len(movie_namesList1)):
    movie_timetableList[movie_namesList1[z]] = movie_timetables[z]
    
n = 1  #選出電影期待度高於80分的電影，列出名稱跟網址連結
for y in movie_expectList.keys():
    y1 = int(movie_expectList[y])
    if y1 > 80:
        print("待看電影清單",n,":",y,movie_timetableList[y])
        n += 1
