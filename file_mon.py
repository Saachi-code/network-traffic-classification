from base64 import decode
from logging import exception
import pandas as pd
import time
import matplotlib.pyplot as plt
try:
    filePath = 'req.txt'
    explicit=['porn','sex','fuck', 'adult']
    games=['zapak','game','play','pubg','cricket','football','ludo']
    ott=['netflix','nflx','sony','primevideo.com','hotstar','youtube.com']
    edu=['edu','ac.in','coursera','udemy','edx']
    news=['sakshi','times','hindu','eenadu','andhrajyothi','deccanchronicle']

    exp=0
    gam=0
    ott1=0
    edu1=0
    news1=0
    gen=0
    def check(i):
        global exp,gam,ott1,edu1,news1,gen
        for j in explicit:
            if(j in i):
                exp=exp+1
                print(i+" is explicit")
                return
        for j in games:
            if(j in i):
                gam=gam+1
                print(i+" is games")
                return
        for j in ott:
            if(j in i):
                ott1=ott1+1
                print(i+" is ott")
                return
        for j in edu:
            if(j in i):
                edu1=edu1+1
                print(i+" is Educational")
                return
        for j in news:
            if(j in i):
                news1=news1+1
                print(i+" is News")
                return
        gen=gen+1
        print(i+" is General")
    strt=0
    while(True):
        with open(filePath, 'r', encoding="utf8") as file:
            data = file.read()
        strings = data.split("\n")
        data=[]
        for i in range(strt, len(strings)):
            try:
                check(strings[i].split(" ")[8].split("\"")[1].replace("b","").replace("'",""))
                # pd.DataFrame([exp,gam,ott1,edu1,news1,gen],columns=['explicit','games','ott','edu','news','general']).to_csv("G:/Python/packet_classification/stats.csv")
            except BaseException as ex:
                # print(ex)
                k=1
        strt=len(strings)
        time.sleep(1)
except KeyboardInterrupt:
    plt.bar(['explicit','games','ott','education','news','general'],[exp,gam,ott1,edu1,news1,gen])
    plt.show()
    # print([exp,gam,ott1,edu1,news1,gen])






