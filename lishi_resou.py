#!/usr/bin/env python
# coding: utf-8

# In[1]:


import json
import requests
import time
import pandas as pd


# In[18]:


# 设置 headers，cookie 
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36',
           'Cookie':'JSESSIONID=8117A258430ECD84241DD1528DC03BE2',
           'Referer':'https://www.enlightent.cn/research/rank/weiboSearchRank'
           }

#时间戳转换为年月日
def stampToTime(stamp): 
    datatime = time.strftime("%Y-%m-%d",time.localtime(float(str(stamp)[0:10])))
    return datatime


# 爬取逻辑
def main():
    # 创建一个 DataFrame 对象，用于保存数据
    resou = pd.DataFrame(columns=['datetime','title','searchCount'])
    # 从 20 年开始到现在共有 20 页
    for i in range(1,21):
        # 请求 url
        url= 'https://www.enlightent.cn/research/top/getWeiboRankSearch.do'
        # 表单参数
        data = {'keyword': '武汉',
                'from': i,
                't': '577803043',
                'accessToken': 'ZDu6fWxLQL0Syobd0BKjhvwtORWDFHxNg4h/77cOAW0U4GSh7B71nF1e8H6NUR733eqHW3GtV//IrWgW5v3t9Q==',
                'type': 'realTimeHotSearchList'
                }
        html = requests.post(url=url,headers=headers,data=data).content
        data = json.loads(html.decode('utf-8'))
        # 一页有 20 条数据
        for j in range(16): 
            resou = resou.append({'datetime':stampToTime(data['rows'][j]['updateTime']),
                    'title':data['rows'][j]['keywords'],'searchCount':data['rows'][j]['searchNums'],
                                  },ignore_index=True)
    resou.to_csv("resou.csv", index_label="index_label",encoding='utf-8-sig')
    

main()


# In[39]:


# 汇总每天有几条热搜
resou = pd.read_csv('resou.csv')
resou_dt = resou.groupby('datetime',as_index=False).agg({'searchCount':['count']})
resou_dt.columns = ['date','count']

temp = resou_dt[3:]
temp.to_csv("count.csv",encoding='utf-8-sig')
temp


# In[40]:


# 汇总每天热搜的搜索数
resou_df = resou.groupby('datetime',as_index=False).agg({'searchCount':['sum']})
resou_df.columns = ['date','sum']
resou_df


# In[43]:


# 绘制日历图
from pyecharts import options as opts
from pyecharts.charts import Calendar
data = [
        (resou_df['date'][i], resou_df['sum'][i])
        for i in range(resou_df.shape[0])
    ]

# 剔除去年的热搜
data = data[3:]


def calendar_base() -> Calendar:
    c = (
        Calendar()
        .add("", data, calendar_opts=opts.CalendarOpts(range_=['2020-01-01', '2020-02-15']))
        .set_global_opts(
            title_opts=opts.TitleOpts(title="20年1月至今热搜次数"),
            visualmap_opts=opts.VisualMapOpts(
                max_=7000000,
                min_=1,
                orient="horizontal",
                is_piecewise=False,
                pos_top="230px",
                pos_left="100px",
            ),
        )
    )
    return c


c = calendar_base()
c.render('热搜日历图.html')


# In[ ]:




