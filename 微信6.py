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
