# coding: UTF-8
import urllib.request
from bs4 import BeautifulSoup
from time import sleep
import csv

pokemon_tettei_kouryaku_url = "https://yakkun.com/"
url2 = "https://yakkun.com/swsh/zukan/"
html2 = urllib.request.urlopen(url2)
soup2 = BeautifulSoup(html2, "html.parser")
print(soup2.select_one("#contents > div:nth-child(11) > ul.pokemon_list > li:nth-child(1) > a"))
print(soup2.select_one("#contents > div:nth-child(11) > ul.pokemon_list > li:nth-child(1) > a").text)
print(soup2.select_one("#contents > div:nth-child(11) > ul.pokemon_list > li:nth-child(1) > a").get('href'))

#move_list
for i in range(425):
    poke_number = i+1
    file_name = "./data/poke_waza/poke_" + '{:03}'.format(poke_number) + "_waza_data.csv"
    print(file_name)
    f= open(file_name, 'w')
    writer = csv.writer(f,  lineterminator='\n')
    writer.writerow(["技名","タイプ","分類","威力","ダイ","命中","PP","直","説明"])
    css_selecter_poke_num = "#contents > div:nth-child(11) > ul.pokemon_list > li:nth-child(" + str(poke_number) + ") > a"
    poke_name = soup2.select_one(css_selecter_poke_num).text
    poke_url_0 = soup2.select_one(css_selecter_poke_num).get('href')
    poke_url = pokemon_tettei_kouryaku_url + poke_url_0[1:]+"/"
    html_poke = urllib.request.urlopen(poke_url)
    soup_poke = BeautifulSoup(html_poke, "html.parser")
    waza_name_list = soup_poke.select(".move_main_row")
    waza_detail = soup_poke.select(".move_detail_row")
    #print(waza_name_list,len(waza_name_list))
    for i in range(len(waza_name_list)):
        name = waza_name_list[i]
        detail = waza_detail[i]
        waza_name = name.select_one(".move_name_cell a").text
        waza_type = detail.select_one(".type").text
        waza_bunnrui = detail.select_one("td:nth-child(2)").text
        waza_iryoku = detail.select_one("td:nth-child(3)").text
        waza_daimax = detail.select_one("td:nth-child(4)").text
        waza_meityuu = detail.select_one("td:nth-child(5)").text
        waza_pp = detail.select_one("td:nth-child(6)").text
        waza_tyoku = detail.select_one("td:nth-child(7)").text
        waza_ex = detail.select_one(".move_ex_cell").text
        writer.writerow([waza_name,waza_type,waza_bunnrui,waza_iryoku,waza_daimax,waza_meityuu,waza_pp,waza_tyoku,waza_ex])


        #move_list > tbody > tr:nth-child(4) > td:nth-child(3)
    sleep(1)
