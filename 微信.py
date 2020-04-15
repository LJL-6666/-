from wxpy import*
bot = Bot()
bot.self.send('Hello World!')
bot.file_helper.send('Hello World!')
my_friend = bot.friends().search(u'Streetcar')[0]
my_friend.send('Hello, WeChat!')
my_friend.send_image('my_picture.png')
my_friend.send_video('my_video.mov')
my_friend.send_file('my_file.zip')
my_friend.send('@img@my_picture.png')
my_friends = bot.friends(update=False)
my_friends.pop(0) # 除去列表中第一个元素（自己）
for i in range(120):
   friend = my_friends[i]
   friend.send('早上好')
# 获取所有好友[返回列表包含Chats物件(你的所有好友，包括自己)]
t0 = bot.friends(update=False)
# 查看自己好友数(除自己)
print("我的好友数："+str(len(t0)-1))
# 获取所有微信群[返回列表包含Groups物件]
t1 = bot.groups(update=False)
# 查看微信群数(活跃的)
print("我的微信群聊数："+str(len(t1)))
# 获取所有关注的微信公众号[返回列表包含Chats物件]
t2 = bot.mps(update=False)
# 查看关注的微信公众号数
print("我关注的微信公众号数："+str(len(t2)))
# 找到群
group = ensure_one(bot.groups().search('要找的群名称'))
# 更新群成员详细信息
group.update_group(True)
female_members = group.members.search(sex=FEMALE)
local_female_members = group.members.search(sex=FEMALE, city='重庆')
local_female_members.add_all(interval=3, verify_content='认识一下吧？')
bot = Bot() 
tuling = Tuling(api_key='图灵api')
print('图灵机器人已上线')
my_friednd = bot.friends().search('Streetcar')[0]
# 如果想对所有好友实现机器人回覆把引数my_friend改成chats = [Friend]



        
