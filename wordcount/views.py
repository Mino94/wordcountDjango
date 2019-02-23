from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
import seaborn as sns


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html') 

def result(request):
    text = request.GET['fulltext'] #글 전체
    words = text.split()#공백 기준으로 나눈다    
    word_dictionary = {}
    
    #<단어 : 몇번:, 단어: 몇번>을 보여준다
    for word in words:
        if word in word_dictionary:
            #increase
            word_dictionary[word]+=1
        else:
            #add to dictionary
            word_dictionary[word]=1
    return render(request, 'result.html', {'full':text, 'total':len(words), 'dictionary': word_dictionary.items})

def CrawlingPage(request):
    # 크롤링한 데이터
    Crawlingtext = crawling()
    Crawlingwords = Crawlingtext.split()
    Crawling_dictionary = {}
    sns.set(style="white")
    mpg = sns.load_dataset("mpg")
    sns.relplot(x="horsepower", y="mpg", hue = "origin", size="weight",  sizes=(40, 400), alpha=.5, palette="muted",
            height=6, data=mpg)
    #<단어 : 몇번:, 단어: 몇번>을 보여준다
    for word in Crawlingwords:
        if word in Crawling_dictionary:
            #increase
            Crawling_dictionary[word]+=1
        else:
            #add to dictionary
            Crawling_dictionary[word]=1
    return render(request, 'CrawlingPage.html',{'crawl':Crawlingtext, 'dictionary2':Crawling_dictionary.items})

def crawling():
    url = "https://news.naver.com"
    req = requests.get(url)
    html = req.text
    soup = BeautifulSoup(html, "html.parser")

    content = soup.select('#today_main_news')

    for contents in content:
        result = contents.text
    return result