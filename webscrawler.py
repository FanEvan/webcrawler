from pyquery import PyQuery as pq
import requests
response = requests.get("https://movies.yahoo.com.tw/movie_thisweek.html")
doc = pq(response.text)
movie_names = doc(".release_info .release_movie_name>.gabtn").text()  
movie_levels = doc(".levelbox").text()   
movie_namesList = movie_names.split()    
movie_namesList1 = []
for j in movie_namesList:
    if j == '電影版':
        continue
    else:
        movie_namesList1.append(j)

movie_expectScore = movie_levels.split()[1::5]  
movie_expectPoint = []
for m in movie_expectScore:
    mm = m.replace("%","")
    int(mm)
    movie_expectPoint.append(mm)
    
movie_timetables = []  
for movie_timetable in doc(".release_btn.color_btnbox .btn_s_time.gabtn").items("a"):
    movie_timetables.append(movie_timetable.attr("href"))
    
movie_expectList = {}  
for x in range(len(movie_namesList1)):
    movie_expectList[movie_namesList1[x]] = movie_expectPoint[x]
    
movie_timetableList = {}  
for z in range(len(movie_namesList1)):
    movie_timetableList[movie_namesList1[z]] = movie_timetables[z]
    
n = 1  
for y in movie_expectList.keys():
    y1 = int(movie_expectList[y])
    if y1 > 80:
        print("待看電影清單",n,":",y,movie_timetableList[y])
        n += 1
