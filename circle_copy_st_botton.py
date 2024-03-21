# -*- coding: utf-8 -*-
# https://towardsdatascience.com/3-easy-ways-to-deploy-your-streamlit-web-app-online-7c88bb1024b1
#https://cold-eye.github.io/post/python-streamlit-heroku/


import pandas as pd
import matplotlib.pyplot as plt
import math
from matplotlib import image
from io import BytesIO
import numpy as np
import streamlit as st
from matplotlib.font_manager import FontProperties;
myfont = FontProperties(fname=r'taipei_sans_tc_beta.ttf')
from lunar_python import Lunar, Solar
import datetime

st.set_page_config(page_title="直接顯示",
    page_icon="hohologo.ico",)



jiazi60 =['60柱',
'01甲子','02乙丑','03丙寅','04丁卯','05戊辰','06己巳','07庚午','08辛未','09壬申','10癸酉',
'11甲戌','12乙亥','13丙子','14丁丑','15戊寅','16己卯','17庚辰','18辛巳','19壬午','20癸未',
'21甲申','22乙酉','23丙戌','24丁亥','25戊子','26己丑','27庚寅','28辛卯','29壬辰','30癸巳',
'31甲午','32乙未','33丙申','34丁酉','35戊戌','36己亥','37庚子','38辛丑','39壬寅','40癸卯',
'41甲辰','42乙巳','43丙午','44丁未','45戊申','46己酉','47庚戌','48辛亥','49壬子','50癸丑',
'51甲寅','52乙卯','53丙辰','54丁巳','55戊午','56己未','57庚申','58辛酉','59壬戌','60癸亥']


# Finding the index of the element
today = datetime.datetime.now()  + datetime.timedelta(hours=8)


col8, col9, col10 = st.columns(3)
with col8:
    user_name = st.text_input('您的名字', '笑禾禾')
    st.write('您的名字是：', user_name)
with col9:
    user_old = st.text_input('您的出生年月日時分', today.strftime('%Y%m%d%H%M'))
    st.write('您的出生年月日是：', user_old)

with col10:
    borg = st.selectbox('您的性別',['性別','男','女'],index=1)
    '您的性別：',borg

# 將字符串分割為年、月、日、時、分
year = int(user_old[0:4])
month = int(user_old[4:6])
day = int(user_old[6:8])
hour = int(user_old[8:10])
minute = int(user_old[10:12])

user_old = user_old[0:8]

# 使用分割後的值建立Solar物件
solar = Solar(year, month, day, hour, minute, 0)

lunar = solar.getLunar()
baZi = lunar.getEightChar()

a0 = next((i for i, item in enumerate(jiazi60) if baZi.getYear() in item), -1)
b0 = next((i for i, item in enumerate(jiazi60) if baZi.getMonth() in item), -1)
c0 = next((i for i, item in enumerate(jiazi60) if baZi.getDay() in item), -1)
d0 = next((i for i, item in enumerate(jiazi60) if baZi.getTime() in item), -1)



# 使用datetime.datetime獲取當前日期和時間


solar = Solar(int(today.year), int(today.month), int(today.day), int(today.hour), int(today.minute), 0)

lunar_today = solar.getLunar()
baZi_today = lunar_today.getEightChar()

thisYear = next((i for i, item in enumerate(jiazi60) if baZi_today.getYear() in item), -1)
thisMonth = next((i for i, item in enumerate(jiazi60) if baZi_today.getMonth() in item), -1)
thisDay= next((i for i, item in enumerate(jiazi60) if baZi_today.getDay() in item), -1)

jiazi60_num=range(61)

col5, col6, col7 = st.columns(3)
with col5:
    thisYear = st.selectbox('流年',jiazi60_num,index=thisYear)
    '流年：',jiazi60[thisYear]
with col6:
    thisMonth = st.selectbox('流月',jiazi60_num,index=thisMonth)
    '流月：',jiazi60[thisMonth]
with col7:
    thisDay = st.selectbox('流日',jiazi60_num,index=thisDay)
    '流日：',jiazi60[thisDay]

# 將選擇的性別轉換為數字
borg_selection = 1 if  borg== '男' else 0

# 使用轉換後的數字調用getYun方法
yun = baZi.getYun( borg_selection)

  
    
#[[癸癸~癸壬],[甲癸~甲壬],...,[壬癸~壬壬]]
tengod=[
['比肩','傷官','食神','正財','偏財','正官','偏官','正印','偏印','劫財'],
['正印','比肩','劫財','食神','傷官','偏財','正財','偏官','正官','偏印'],
['偏印','劫財','比肩','傷官','食神','正財','偏財','正官','偏官','正印'],
['正官','偏印','正印','比肩','劫財','食神','傷官','偏財','正財','偏官'],
['偏官','正印','偏印','劫財','比肩','傷官','食神','正財','偏財','正官'],
['正財','偏官','正官','偏印','正印','比肩','劫財','食神','傷官','偏財'],
['偏財','正官','偏官','正印','偏印','劫財','比肩','傷官','食神','正財'],
['傷官','偏財','正財','偏官','正官','偏印','正印','比肩','劫財','食神'],
['食神','正財','偏財','正官','偏官','正印','偏印','劫財','比肩','傷官'],
['劫財','食神','傷官','偏財','正財','偏官','正官','偏印','正印','比肩']]

thistime = [thisYear, thisMonth,  thisDay]

jiazi60hohocard =['60甲子',
'01甲子 向上逆轉','02乙丑 關係溝通','03丙寅 關係溝通','04丁卯 向上逆轉','05戊辰 行動執行','06己巳 行動執行','07庚午 生活空間','08辛未 投資財富','09壬申 目標管理','10癸酉 才華學習',
'11甲戌 才華學習','12乙亥 生活空間','13丙子 愛情婚姻','14丁丑 投資財富','15戊寅 感恩祝福','16己卯 貴人桃花','17庚辰 情緒覺察','18辛巳 生活空間','19壬午 感恩祝福','20癸未 關係溝通',
'21甲申 關係溝通','22乙酉 愛情婚姻','23丙戌 目標管理','24丁亥 事業組織','25戊子 行動執行','26己丑 事業組織','27庚寅 生活空間','28辛卯 愛情婚姻','29壬辰 向上逆轉','30癸巳 向上逆轉',
'31甲午 情緒覺察','32乙未 情緒覺察','33丙申 事業組織','34丁酉 貴人桃花','35戊戌 感恩祝福','36己亥 愛情婚姻','37庚子 貴人桃花','38辛丑 投資財富','39壬寅 事業組織','40癸卯 貴人桃花',
'41甲辰 生活空間','42乙巳 行動執行','43丙午 情緒覺察','44丁未 向上逆轉','45戊申 目標管理','46己酉 感恩祝福','47庚戌 感恩祝福','48辛亥 才華學習','49壬子 愛情婚姻','50癸丑 關係溝通',
'51甲寅 行動執行','52乙卯 貴人桃花','53丙辰 事業組織','54丁巳 情緒覺察','55戊午 目標管理','56己未 投資財富','57庚申 目標管理','58辛酉 才華學習','59壬戌 投資財富','60癸亥 才華學習']


fivetype=['五行','木','火','土','金','水']

if a0%10==1 or a0%10==2:
    a0tengan=fivetype[1]
elif a0%10==3 or a0%10==4:
    a0tengan=fivetype[2]
elif a0%10==5 or a0%10==6:
    a0tengan=fivetype[3]
elif a0%10==7 or a0%10==8:
    a0tengan=fivetype[4]
else:
    a0tengan=fivetype[5]
if b0%10==1 or b0%10==2:
    b0tengan=fivetype[1]
elif b0%10==3 or b0%10==4:
    b0tengan=fivetype[2]
elif b0%10==5 or b0%10==6:
    b0tengan=fivetype[3]
elif b0%10==7 or b0%10==8:
    b0tengan=fivetype[4]
else:
    b0tengan=fivetype[5]
if c0%10==1 or c0%10==2:
    c0tengan=fivetype[1]
elif c0%10==3 or c0%10==4:
    c0tengan=fivetype[2]
elif c0%10==5 or c0%10==6:
    c0tengan=fivetype[3]
elif c0%10==7 or c0%10==8:
    c0tengan=fivetype[4]
else:
    c0tengan=fivetype[5]
if d0%10==1 or d0%10==2:
    d0tengan=fivetype[1]
elif d0%10==3 or d0%10==4:
    d0tengan=fivetype[2]
elif d0%10==5 or d0%10==6:
    d0tengan=fivetype[3]
elif d0%10==7 or d0%10==8:
    d0tengan=fivetype[4]
else:
    d0tengan=fivetype[5]

strong = 0
if fivetype.index(c0tengan)-fivetype.index(a0tengan)==0 or fivetype.index(c0tengan)-fivetype.index(a0tengan)==1 or fivetype.index(c0tengan)-fivetype.index(a0tengan)== -4:
    strong = strong+1
if fivetype.index(c0tengan)-fivetype.index(b0tengan)==0 or fivetype.index(c0tengan)-fivetype.index(b0tengan)==1 or fivetype.index(c0tengan)-fivetype.index(b0tengan)== -4:
    strong = strong+1
if fivetype.index(c0tengan)-fivetype.index(d0tengan)==0 or fivetype.index(c0tengan)-fivetype.index(d0tengan)==1 or fivetype.index(c0tengan)-fivetype.index(d0tengan)== -4:
    strong = strong+1

if strong>=2:
    strong1='身強'
else:
    strong1='身弱'
	
if a0%12==3 or a0%12==4:
    a0deZhi=fivetype[1]
elif a0%12==6 or a0%12==7:
    a0deZhi=fivetype[2]
elif a0%12==0 or a0%12==1:
    a0deZhi=fivetype[5]
elif a0%12==9 or a0%12==10:
    a0deZhi=fivetype[4]
else:
    a0deZhi=fivetype[3]
if b0%12==3 or b0%12==4:
    b0deZhi=fivetype[1]
elif b0%12==6 or b0%12==7:
    b0deZhi=fivetype[2]
elif b0%12==0 or b0%12==1:
    b0deZhi=fivetype[5]
elif b0%12==9 or b0%12==10:
    b0deZhi=fivetype[4]
else:
    b0deZhi=fivetype[3]
if c0%12==3 or c0%12==4:
    c0deZhi=fivetype[1]
elif c0%12==6 or c0%12==7:
    c0deZhi=fivetype[2]
elif c0%12==0 or c0%12==1:
    c0deZhi=fivetype[5]
elif c0%12==9 or c0%12==10:
    c0deZhi=fivetype[4]
else:
    c0deZhi=fivetype[3]
if d0%12==3 or d0%12==4:
    d0deZhi=fivetype[1]
elif d0%12==6 or d0%12==7:
    d0deZhi=fivetype[2]
elif d0%12==0 or d0%12==1:
    d0deZhi=fivetype[5]
elif d0%12==9 or d0%12==10:
    d0deZhi=fivetype[4]
else:
    d0deZhi=fivetype[3]

strong = 1
if fivetype.index(c0tengan)-fivetype.index(a0tengan)==0 or fivetype.index(c0tengan)-fivetype.index(a0tengan)==1 or fivetype.index(c0tengan)-fivetype.index(a0tengan)== -4:
    strong = strong+1
if fivetype.index(c0tengan)-fivetype.index(b0tengan)==0 or fivetype.index(c0tengan)-fivetype.index(b0tengan)==1 or fivetype.index(c0tengan)-fivetype.index(b0tengan)== -4:
    strong = strong+1
if fivetype.index(c0tengan)-fivetype.index(d0tengan)==0 or fivetype.index(c0tengan)-fivetype.index(d0tengan)==1 or fivetype.index(c0tengan)-fivetype.index(d0tengan)== -4:
    strong = strong+1
if fivetype.index(c0tengan)-fivetype.index(a0deZhi)==0 or fivetype.index(c0tengan)-fivetype.index(a0deZhi)==1 or fivetype.index(c0tengan)-fivetype.index(a0deZhi)== -4:
    strong = strong+1
if fivetype.index(c0tengan)-fivetype.index(b0deZhi)==0 or fivetype.index(c0tengan)-fivetype.index(b0deZhi)==1 or fivetype.index(c0tengan)-fivetype.index(b0deZhi)== -4:
    strong = strong+1
if fivetype.index(c0tengan)-fivetype.index(c0deZhi)==0 or fivetype.index(c0tengan)-fivetype.index(c0deZhi)==1 or fivetype.index(c0tengan)-fivetype.index(c0deZhi)== -4:
    strong = strong+1	
if fivetype.index(c0tengan)-fivetype.index(d0deZhi)==0 or fivetype.index(c0tengan)-fivetype.index(d0deZhi)==1 or fivetype.index(c0tengan)-fivetype.index(d0deZhi)== -4:
    strong = strong+1

if strong>=4:
    strong2='身弱'
else:
    strong2='身強'

strong=0	
if b0%12==3 or b0%12==4 or b0%12==5:
    b0deZhi=fivetype[1]
elif b0%12==6  or b0%12==7 or b0%12==8:
    b0deZhi=fivetype[2]
elif b0%12==9 or b0%12==10 or b0%12==11:
    b0deZhi=fivetype[4]
else:
    b0deZhi=fivetype[5]
	
if fivetype.index(c0tengan)-fivetype.index(b0deZhi)==0 or fivetype.index(c0tengan)-fivetype.index(b0deZhi)==1 or fivetype.index(c0tengan)-fivetype.index(b0deZhi)== -4:
    strong = strong+1	

if strong>=1:
    strong3='身強'
else:
    strong3='身弱'
	

		
hidegod=[['甲','','壬'],['','癸',''],['辛','癸','己'],['戊','丙','甲'],['','乙',''],['癸','乙','戊'],['庚','戊','丙'],['己','','丁'],['丁','乙','己'],['戊','壬','庚'],['','辛',''],['丁','辛','戊']]
hidegodnum=[[1,9],[0],[8,0,6],[5,3,1],[2],[0,2,5],[7,5,3],[6,4],[4,2,6],[5,9,7],[8],[4,8,5]]

d0hide=''
for i in range(len(hidegodnum[d0%12])):
    d0hide=d0hide+tengod[c0%10][hidegodnum[d0%12][i]]
c0hide=''
for i in range(len(hidegodnum[c0%12])):
    c0hide=c0hide+tengod[c0%10][hidegodnum[c0%12][i]]
b0hide=''
for i in range(len(hidegodnum[b0%12])):
    b0hide=b0hide+tengod[c0%10][hidegodnum[b0%12][i]]
a0hide=''
for i in range(len(hidegodnum[a0%12])):
    a0hide=a0hide+tengod[c0%10][hidegodnum[a0%12][i]]

d0hidegen=''
for i in range(len(hidegod[d0%12])):
    d0hidegen=d0hidegen+str(hidegod[d0%12][i])
c0hidegen=''
for i in range(len(hidegod[c0%12])):
    c0hidegen=c0hidegen+str(hidegod[c0%12][i])
b0hidegen=''
for i in range(len(hidegod[b0%12])):
    b0hidegen=b0hidegen+str(hidegod[b0%12][i])
a0hidegen=''
for i in range(len(hidegod[a0%12])):
    a0hidegen=a0hidegen+str(hidegod[a0%12][i])
	
data = [[tengod[c0%10][d0%10],'日主',tengod[c0%10][b0%10],tengod[c0%10][a0%10],'十神'],[jiazi60[d0][2],jiazi60[c0][2],jiazi60[b0][2],jiazi60[a0][2],'天干'],[jiazi60[d0][3],jiazi60[c0][3],jiazi60[b0][3],jiazi60[a0][3],'地支'],[d0hidegen,c0hidegen,b0hidegen,a0hidegen,'藏干'],[d0hide,c0hide,b0hide,a0hide,'藏神']]

df = pd.DataFrame(data)
df1 =  df.style.set_table_styles([dict(selector='th', props=[('text-align', 'center')])]).set_properties(**{'text-align': 'center'}).hide(axis='index').hide(axis='columns')
st.subheader('您的人生使用手冊：')
st.write(df1.to_html(), unsafe_allow_html=True)

st.write("")		
####################################################################################################################################################################################################################################################################
st.write("[諮詢對話總攬(hackmd)](https://hackmd.io/btGjT-E9QqqnC8_oJGGlZw)")
st.write("[EP進階班(hackmd)](https://hackmd.io/eZpWH_MkR96amxWWQwy5_A)")
st.write("[分數(hackmd)](https://hackmd.io/EZ4jx5ltSiGWf3ufXtsFlA)")
if st.button('產生結果'):

    fivetype=['五行','木','火','土','金','水']
    
    if a0%10==1 or a0%10==2:
        a0tengan=fivetype[1]
    elif a0%10==3 or a0%10==4:
        a0tengan=fivetype[2]
    elif a0%10==5 or a0%10==6:
        a0tengan=fivetype[3]
    elif a0%10==7 or a0%10==8:
        a0tengan=fivetype[4]
    else:
        a0tengan=fivetype[5]
    if b0%10==1 or b0%10==2:
        b0tengan=fivetype[1]
    elif b0%10==3 or b0%10==4:
        b0tengan=fivetype[2]
    elif b0%10==5 or b0%10==6:
        b0tengan=fivetype[3]
    elif b0%10==7 or b0%10==8:
        b0tengan=fivetype[4]
    else:
        b0tengan=fivetype[5]
    if c0%10==1 or c0%10==2:
        c0tengan=fivetype[1]
    elif c0%10==3 or c0%10==4:
        c0tengan=fivetype[2]
    elif c0%10==5 or c0%10==6:
        c0tengan=fivetype[3]
    elif c0%10==7 or c0%10==8:
        c0tengan=fivetype[4]
    else:
        c0tengan=fivetype[5]
    if d0%10==1 or d0%10==2:
        d0tengan=fivetype[1]
    elif d0%10==3 or d0%10==4:
        d0tengan=fivetype[2]
    elif d0%10==5 or d0%10==6:
        d0tengan=fivetype[3]
    elif d0%10==7 or d0%10==8:
        d0tengan=fivetype[4]
    else:
        d0tengan=fivetype[5]
    
    #st.write('身強：\n\
    #能夠去貫徹自己的想法、承擔責任，擁有度強，情緒度高\n\
    #獨立自主，不怕受傷，越挫越勇，屹立不搖，堅持到底\n\
    #凡事靠自己，先做後想，理性追逐。\n\
    #\n\
    #主觀意識強大，固執己見，不會體諒他人，自負缺圓融，無法溝通，\n\
    #聽不進勸，強勢，逼迫，主導，大男(女)人，永遠是他人的貴人，夠拗。')
    #st.write('')
    #st.write('身弱：\n\
    #意志力薄弱，三心二意，優柔寡斷，沒恆心，沒毅力，不堅定的感覺\n\
    #做事三分鐘熱度，常受到外來因素的影響，朝令夕改\n\
    #需有人協助瞻前顧後，先想後座，無限膽怯。\n\
    #\n\
    #給人舒服，軟性風格，腰軟嘴甜，貼心，令人憐惜，左右逢源，以退為進\n\
    #以和為貴，貴人提拔相助，關鍵重要人物，感性到手，送到門口。\n')
    
    st.title('身強身弱')
    strong = 0
    if fivetype.index(c0tengan)-fivetype.index(a0tengan)==0 or fivetype.index(c0tengan)-fivetype.index(a0tengan)==1 or fivetype.index(c0tengan)-fivetype.index(a0tengan)== -4:
        strong = strong+1
    if fivetype.index(c0tengan)-fivetype.index(b0tengan)==0 or fivetype.index(c0tengan)-fivetype.index(b0tengan)==1 or fivetype.index(c0tengan)-fivetype.index(b0tengan)== -4:
        strong = strong+1
    if fivetype.index(c0tengan)-fivetype.index(d0tengan)==0 or fivetype.index(c0tengan)-fivetype.index(d0tengan)==1 or fivetype.index(c0tengan)-fivetype.index(d0tengan)== -4:
        strong = strong+1
    
    if strong>=2:
        strong1='身強'
    else:
        strong1='身弱'
    
    st.write('得勢力藏於內的信念(得勢 電力 十神)：'+strong1)	
    if a0%12==3 or a0%12==4:
        a0deZhi=fivetype[1]
    elif a0%12==6 or a0%12==7:
        a0deZhi=fivetype[2]
    elif a0%12==0 or a0%12==1:
        a0deZhi=fivetype[5]
    elif a0%12==9 or a0%12==10:
        a0deZhi=fivetype[4]
    else:
        a0deZhi=fivetype[3]
        
    if b0%12==3 or b0%12==4:
        b0deZhi=fivetype[1]
    elif b0%12==6 or b0%12==7:
        b0deZhi=fivetype[2]
    elif b0%12==0 or b0%12==1:
        b0deZhi=fivetype[5]
    elif b0%12==9 or b0%12==10:
        b0deZhi=fivetype[4]
    else:
        b0deZhi=fivetype[3]
        
    if c0%12==3 or c0%12==4:
        c0deZhi=fivetype[1]
    elif c0%12==6 or c0%12==7:
        c0deZhi=fivetype[2]
    elif c0%12==0 or c0%12==1:
        c0deZhi=fivetype[5]
    elif c0%12==9 or c0%12==10:
        c0deZhi=fivetype[4]
    else:
        c0deZhi=fivetype[3]
    if d0%12==3 or d0%12==4:
        d0deZhi=fivetype[1]
    elif d0%12==6 or d0%12==7:
        d0deZhi=fivetype[2]
    elif d0%12==0 or d0%12==1:
        d0deZhi=fivetype[5]
    elif d0%12==9 or d0%12==10:
        d0deZhi=fivetype[4]
    else:
        d0deZhi=fivetype[3]
    
    strong = 1
    if fivetype.index(c0tengan)-fivetype.index(a0tengan)==0 or fivetype.index(c0tengan)-fivetype.index(a0tengan)==1 or fivetype.index(c0tengan)-fivetype.index(a0tengan)== -4:
        strong = strong+1
    if fivetype.index(c0tengan)-fivetype.index(b0tengan)==0 or fivetype.index(c0tengan)-fivetype.index(b0tengan)==1 or fivetype.index(c0tengan)-fivetype.index(b0tengan)== -4:
        strong = strong+1
    if fivetype.index(c0tengan)-fivetype.index(d0tengan)==0 or fivetype.index(c0tengan)-fivetype.index(d0tengan)==1 or fivetype.index(c0tengan)-fivetype.index(d0tengan)== -4:
        strong = strong+1
    if fivetype.index(c0tengan)-fivetype.index(a0deZhi)==0 or fivetype.index(c0tengan)-fivetype.index(a0deZhi)==1 or fivetype.index(c0tengan)-fivetype.index(a0deZhi)== -4:
        strong = strong+1
    if fivetype.index(c0tengan)-fivetype.index(b0deZhi)==0 or fivetype.index(c0tengan)-fivetype.index(b0deZhi)==1 or fivetype.index(c0tengan)-fivetype.index(b0deZhi)== -4:
        strong = strong+1
    if fivetype.index(c0tengan)-fivetype.index(c0deZhi)==0 or fivetype.index(c0tengan)-fivetype.index(c0deZhi)==1 or fivetype.index(c0tengan)-fivetype.index(c0deZhi)== -4:
        strong = strong+1	
    if fivetype.index(c0tengan)-fivetype.index(d0deZhi)==0 or fivetype.index(c0tengan)-fivetype.index(d0deZhi)==1 or fivetype.index(c0tengan)-fivetype.index(d0deZhi)== -4:
        strong = strong+1
    
    if strong>=4:
        strong2='身弱'
    else:
        strong2='身強'
    st.write('得分展現於外的氣場(得分 續航力 五行)  ：'+strong2)	
    strong=0	
    if b0%12==3 or b0%12==4 or b0%12==5:
        b0deZhi=fivetype[1]
    elif b0%12==6  or b0%12==7 or b0%12==8:
        b0deZhi=fivetype[2]
    elif b0%12==9 or b0%12==10 or b0%12==11:
        b0deZhi=fivetype[4]
    else:
        b0deZhi=fivetype[5]
    	
    if fivetype.index(c0tengan)-fivetype.index(b0deZhi)==0 or fivetype.index(c0tengan)-fivetype.index(b0deZhi)==1 or fivetype.index(c0tengan)-fivetype.index(b0deZhi)== -4:
        strong = strong+1	
    
    if strong>=1:
        strong3='身強'
    else:
        strong3='身弱'
    st.write('得時貫徹意志力的強度(得時 堅持力 季節)：'+strong3);
    timechin =['流年','流月','流日']
    
    # 初始化格子底色為白色
    colors = [['w', 'w', 'w', 'w'],  # 第一行的顏色
              ['w', 'w', 'w', 'w']]  # 第二行的顏色
    
    # 初始化格子的文字
    table_text = [['時干12'+d0tengan, '日主'+c0tengan, '月干12'+b0tengan, '年干8'+a0tengan],
                  ['時支12'+d0deZhi, '日支12'+c0deZhi, '月令40'+b0deZhi, '年支4'+a0deZhi]]
    
    # 設定格子底色和計算得分
    strong = 0
    c_b = ['w', 'c']  # 白色和彩色選項
    
    # 根據條件改變格子底色並計算得分
    if fivetype.index(c0tengan) - fivetype.index(a0tengan) in [0, 1, -4]:
        colors[0][3] = c_b[1]
        strong += 8
    
    if fivetype.index(c0tengan) - fivetype.index(b0tengan) in [0, 1, -4]:
        colors[0][2] = c_b[1]
        strong += 12
    
    if fivetype.index(c0tengan) - fivetype.index(d0tengan) in [0, 1, -4]:
        colors[0][0] = c_b[1]
        strong += 12
    
    if fivetype.index(c0tengan) - fivetype.index(a0deZhi) in [0, 1, -4]:
        colors[1][3] = c_b[1]
        strong += 4
    
    if fivetype.index(c0tengan) - fivetype.index(b0deZhi) in [0, 1, -4]:
        colors[1][2] = c_b[1]
        strong += 40
    
    if fivetype.index(c0tengan) - fivetype.index(c0deZhi) in [0, 1, -4]:
        colors[1][1] = c_b[1]
        strong += 12
    
    if fivetype.index(c0tengan) - fivetype.index(d0deZhi) in [0, 1, -4]:
        colors[1][0] = c_b[1]
        strong += 12
    
    # 绘制表格
    fig, ax = plt.subplots(figsize=(5, 1))  # figsize可以根据需要调整
    ax.axis('off')  # 关闭轴
    ax.axis('tight')  # 紧凑布局
    
    # 创建表格
    the_table = ax.table(cellText=table_text, cellColours=colors, loc='center', cellLoc='center')
    the_table.auto_set_font_size(False)
    the_table.set_fontsize(10)  # 可以根据需要调整字体大小
    the_table.scale(1, 1.5)  # 可以根据需要调整表格的列宽和行高
    for (row, col), cell in the_table.get_celld().items():
        cell.set_text_props(fontproperties=myfont)    
    
    # 移除图表周围的白边
    fig.patch.set_visible(False)
    ax.set_clip_on(False)
    ax.set_frame_on(False)

    
    # 使用 st.pyplot() 展示图形
    st.pyplot(fig)
    
    # 顯示得分
    st.write('身強身弱得分：', str(strong))


