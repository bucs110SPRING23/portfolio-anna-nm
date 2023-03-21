import json 

news = open("news.txt", 'r').read()
js_txt = open("subs.json", 'r')
js = json.load(js_txt)

for key, value in js.items():
    news = news.replace(key, value)
betterNews = open("betternews.txt", 'w')
betterNews.write(news)
betterNews.close()
