# coding: UTF-8
import urllib.request
from bs4 import BeautifulSoup
from time import sleep
import csv

# アクセスするURL
url = "http://www.nikkei.com/"

# URLにアクセスする htmlが帰ってくる → <html><head><title>経済、株価、ビジネス、政治のニュース:日経電子版</title></head><body....
html = urllib.request.urlopen(url)

# htmlをBeautifulSoupで扱う
soup = BeautifulSoup(html, "html.parser")

# タイトル要素を取得する → <title>経済、株価、ビジネス、政治のニュース:日経電子版</title>
title_tag = soup.title

# 要素の文字列を取得する → 経済、株価、ビジネス、政治のニュース:日経電子版
title = title_tag.string

# タイトル要素を出力
print(title_tag)

# タイトルを文字列を出力
print(title)

#contents > div:nth-child(11) > ul.pokemon_list > li:nth-child(3) > a
#contents > div:nth-child(11) > ul.pokemon_list > li:nth-child(2) > a
#contents > div:nth-child(11) > ul.pokemon_list > li:nth-child(1) > a
#contents > div:nth-child(11) > ul.pokemon_list > li:nth-child(1)

pokemon_tettei_kouryaku_url = "https://yakkun.com/"
url2 = "https://yakkun.com/swsh/zukan/"
html2 = urllib.request.urlopen(url2)
soup2 = BeautifulSoup(html2, "html.parser")
print(soup2.select_one("#contents > div:nth-child(11) > ul.pokemon_list > li:nth-child(1) > a"))
print(soup2.select_one("#contents > div:nth-child(11) > ul.pokemon_list > li:nth-child(1) > a").text)
print(soup2.select_one("#contents > div:nth-child(11) > ul.pokemon_list > li:nth-child(1) > a").get('href'))
sc_a = soup2.select_one("#contents > div:nth-child(11) > ul.pokemon_list > li:nth-child(3) > a").get('href')

ttt="#contents > div:nth-child(11) > ul.pokemon_list > li:nth-child(3) > span"
print(soup2.select_one(ttt).text)
print(type(title_tag),type(title),type(sc_a))

#poke_url = pokemon_tettei_kouryaku_url + sc_a[1:]+"/"
#print(poke_url)
#html3 = urllib.request.urlopen(poke_url)
#soup3 = BeautifulSoup(html3, "html.parser")
#hp=soup3.select_one("#stats_anchor > table > tr:nth-child(2) > td.left").text
#hp=soup3.select_one("#stats_anchor > table > tr:nth-child(2) > td.left").text[1:]
#print(len(hp),hp[0],",",hp[1],",",hp[2])
#hp2=hp[1:]
#print(poke_name," hp=",hp)
#print("hp3",hp3)

#print(soup3.find_all(class_="left",colspan="5"))

#stats_anchor > table > tbody > tr:nth-child(2) > td.left
#base_anchor > table > tbody > tr:nth-child(8) > td:nth-child(2) > ul > li > a > img
#base_anchor > table > tbody > tr:nth-child(8) > td:nth-child(2) > ul > li:nth-child(2) > a > img
#base_anchor > table > tbody > tr:nth-child(8) > td:nth-child(2) > ul > li:nth-child(1) > a > img

#contents > div:nth-child(11) > ul.pokemon_list > li:nth-child(344) > span

f= open('all_poke_data.csv', 'w')
writer = csv.writer(f,  lineterminator='\n')
for i in range(425):
    poke_number = i+1
    css_selecter_poke_num = "#contents > div:nth-child(11) > ul.pokemon_list > li:nth-child(" + str(poke_number) + ") > a"
    poke_name = soup2.select_one(css_selecter_poke_num).text
    poke_url_0 = soup2.select_one(css_selecter_poke_num).get('href')
    poke_url = pokemon_tettei_kouryaku_url + poke_url_0[1:]+"/"
    html_poke = urllib.request.urlopen(poke_url)
    soup_poke = BeautifulSoup(html_poke, "html.parser")
    hp = soup_poke.select_one("#stats_anchor > table > tr:nth-child(2) > td.left").text[1:]
    a = soup_poke.select_one("#stats_anchor > table > tr:nth-child(3) > td.left").text[1:]
    print(len(a))
    if len(a)>3:
        a = a[:3]
    b = soup_poke.select_one("#stats_anchor > table > tr:nth-child(4) > td.left").text[1:]
    print(len(b))
    if len(b)>3:
        b = b[:3]
    c = soup_poke.select_one("#stats_anchor > table > tr:nth-child(5) > td.left").text[1:]
    if len(c)>3:
        c = c[:3]
    d = soup_poke.select_one("#stats_anchor > table > tr:nth-child(6) > td.left").text[1:]
    if len(d)>3:
        d = d[:3]
    s = soup_poke.select_one("#stats_anchor > table > tr:nth-child(7) > td.left").text[1:]
    type1 = soup_poke.select_one("#base_anchor > table > tr:nth-child(8) > td:nth-child(2) > ul > li > a > img").get('alt')
    if soup_poke.select_one("#base_anchor > table > tr:nth-child(8) > td:nth-child(2) > ul > li:nth-child(2) > a > img") ==None:
        type2 = "None"
    else:
        type2 = soup_poke.select_one("#base_anchor > table > tr:nth-child(8) > td:nth-child(2) > ul > li:nth-child(2) > a > img").get('alt')
    print(poke_number,poke_name,hp,a,b,c,d,s,type1,type2)

    writer.writerow([poke_name,hp,a,b,c,d,s,type1,type2])

    sleep(1)
