from selenium import webdriver

driver_path = "/Users/kuoyufan/pytest/webdriver/chromedriver"
option = webdriver.ChromeOptions()
option.add_argument("headless") 
driver = webdriver.Chrome(driver_path)
driver.implicitly_wait(10)

url = "https://movies.yahoo.com.tw/movie_thisweek.html"
name_path = "//main//div/div[@class='release_movie_name']/a"
score_path = "//*[@id='content_l']//dl/dt/div[2]/span"

driver.get(url)
movie_names = driver.find_elements_by_xpath(name_path)
expect_scores = driver.find_elements_by_xpath(score_path)

namelists, scorelists, linklists = [],[],[]
for name, score, link in zip(movie_names, expect_scores, movie_names):
    namelists.append(name.text)
    scorelists.append(int((str(score.text).replace("%",""))))
    linklists.append(name.get_attribute("href"))

mylist={}
for i in range(len(scorelists)):
    if scorelists[i] >= 80:
        mylist[namelists[i]] = linklists[i]
print("必看電影清單: ", mylist)
