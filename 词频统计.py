# 第一题
def getText():
    txt=open('哈姆雷特.txt','r', encoding='UTF-8').read()
    txt=txt.lower()
    for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_‘{|}~':
        txt =txt.replace(ch," ")
    return txt

哈姆雷特Txt=getText()
words=哈姆雷特Txt.split()
counts={}
for word in words:
    counts[word]=counts.get(word,0)+1

items=list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
for i in range (10):
    word,count=items[i]
    print("{0:<10}{1:>5}".format(word,count))


# 第二题
print('《三国演义》人物出场统计（上）')

import jieba
txt = open('三国演义.txt', "r", encoding='utf-8').read()
words  = jieba.lcut(txt)
counts = {}
for word in words:
    if len(word) == 1:
        continue
    else:
        counts[word] = counts.get(word,0) + 1
items = list(counts.items())
items.sort(key=lambda x:x[1], reverse=True)

for i in range(15):
    word, count = items[i]
    print ("{0:<10}{1:>5}".format(word, count))

print('《三国演义》人物出场统计（下）')
txt = open("三国演义.txt", "r", encoding='utf-8').read()
excludes={"将军","却说","荆州","二人","不可","不能","如此"}
words  = jieba.lcut(txt)
counts = {}
for word in words:
    if len(word) == 1:
        continue
    elif word=="诸葛亮" or word=="孔明曰":
        rword="孔明"
    elif word=="关公" or word=="云长":
         rword="关羽"
    elif word=="玄德" or word=="玄德曰":
        rword="刘备"
    elif word=="孟德" or word=="丞相":
         rword="曹操"
    else:
        rword=word
        counts[rword] = counts.get(rword,0) + 1

for word in excludes:
    del counts[word]

items = list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
for i in range(10):
    word, count = items[i]
    print ("{0:<10}{1:>5}".format(word, count))


print('《三国演义》人物出场统计（精确）')
words = jieba.lcut(txt)
excludes = ['将军','却说','二人','不可','荆州','不能','如此','商议','如何'
            ,'军士','左右','天下','次日','大喜','引兵','军马','东吴','于是'
            ,'今日','不敢','魏兵','陛下','一人','人马','汉中','不知','只见',
            '众将','蜀兵','上马','大叫']
counts = {}
for word in words:
    if len(word) == 1:
        continue
    elif word == '诸葛亮'or word == '孔明曰':
        rword = '孔明'
    elif word == '玄德'or word == '玄德曰' or word == '主公':
        rword = '刘备'
    elif word == '孟德'or word == '丞相':
        rword = '曹操'
    elif word == '关公'or word == '云长':
        rword = '关羽'
    elif word == '都督':
        rword = '周瑜'
    elif word == '后主':
        rword = '刘禅'
    elif word == '太守':
        rword = '刘度'
    else:
        rword = word
    counts[rword] = counts.get(rword,0) + 1

for word in excludes:
    del counts[word]
items = list(counts.items())
items.sort(key = lambda x:x[1],reverse=True)
for i in range(15):
    word,count = items[i]
    print("{0:<10}{1:>5}".format(word,count))
