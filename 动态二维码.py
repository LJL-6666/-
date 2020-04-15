import os
from MyQR import myqr

#gif存储的位置
save_name = 'G:/尝试/嘉玲.gif'
myqr.run(
    words='https://mp.weixin.qq.com/s?__biz=MzU2Mzc0NTgxMA==&mid=2247483885&idx=1&sn=0a07c190c1502cc69c5dc0e4d69b8f1c&chksm=fc54c490cb234d86678a5412e27e4455a5adf692e73403bc776a0951b069c3fa3bd9be15a648&scene=0&xtrack=1&sharer_openid=oEnJq1IXHGUVd0M9CB6rBRBzY2zg&sharer_sharetime=1584584519&srcid=0319swjMV3DAgN2YZaHSafAD&appmsg_type=9&vid=wxv_1234236330243178496&key=7d42e6f9dbc0e891b7439c2c5f2158346539bb0e25260ea46bc54320c4aba408337f9f6312022b78bbb66905842bae0900d37a70fab77d85a9191922d6b31b563a23ff788e90bc7158085ce0d9fee43f&ascene=1&uin=MzQ0NDY5NzEyNw%3D%3D&devicetype=Windows+10&version=62080079&lang=zh_CN&exportkey=AxrOfWWRAbcU%2FdLH3ArOPm4%3D&pass_ticket=5Mokhx1WgkLsvR4r2xmAERJwuxRfeu2Hoz82DgJL4GndgoOYwoD2iuJFKbxVMOiC',#扫描二维码后跳转的链接
    version=5,  #容错率
    level='H',  #纠错水平，范围是L、M、Q、H，从左到右依次升高
    colorized=True,#False为黑白
    contrast=1.0,  # 用以调节图片的对比度，1.0 表示原始图片。
    brightness=1.0,  # 用来调节图片的亮度。
    save_name=save_name,#存储的文件名
    picture='C:/Users/hp/OneDrive/图片/嘉玲.gif'#背景图片的路径
    )
