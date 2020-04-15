from pyecharts import wordcloud
name = ['刘嘉玲'] # 词条
value = [10000] # 权重
wordcloud = wordcloud(width=1300, height=620)
wordcloud.add(" ", name, value, word_size_range=[20, 100])
wordcloud.render()

