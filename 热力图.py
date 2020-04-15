import numpy as np
import pandas as pd
import folium
from folium.plugins import HeatMap
posi=pd.read_excel("data.xlsx")
num = 113240
lat = np.array(posi["lat"][0:num])                        # 获取维度之维度值
lon = np.array(posi["lon"][0:num])                        # 获取经度值
data1 = [[lat[i],lon[i]] for i in range(num)]    #将数据制作成[lats,lons,weights]的形式
map_osm = folium.Map(location=[1,2],zoom_start=1)    #绘制Map，开始缩放程度是5倍
HeatMap(data1).add_to(map_osm)  # 将热力图添加到前面建立的map里
file_path = r"C:\Users\admin\Desktop\热力图.html"
map_osm.save(file_path)     # 保存为html文件
#webbrowser.open(file_path)  # 默认浏览器打开
