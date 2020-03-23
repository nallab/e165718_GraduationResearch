# -*- coding: utf-8 -*-
import MeCab
import glob
import csv


# get review paths
text_paths = glob.glob('./review/star1-/**.txt')
# print(text_paths)



# processing
def nlp(content):
    # make dictionary.
    tagger = MeCab.Tagger('-Owakati -d /usr/local/lib/mecab/dic/mecab-ipadic-neologd')

    # end of sentense.
    #EOS_DIC = ['。', '．',',','、','！','？','!?', '!', '?','…' ]

    tagger.parse('')
    node = tagger.parseToNode(content) # nodeにsurfaec(単語)feature(品詞情報)を持つ解析結果を代入． node.surface/node.featureでそれぞれにアクセス可能．
    keywords = []
    while node:
        if node.feature.split(',')[0] == u"名詞":
            keywords.append(node.surface)
        elif node.feature.split(',')[0] == u"形容詞":
            keywords.append(node.feature.split(',')[6])
        elif node.feature.split(',')[0] == u"動詞":
            keywords.append(node.feature.split(',')[6])
        elif node.feature.split(',')[0] == u"副詞":
            keywords.append(node.feature.split(',')[6])
        node = node.next
    # print(keywords)

        # with open('result_1.csv','a')as f:
        #     writer = csv.writer(f)
        #     writer.writerow([point,word_list[0]])
        # print(str(point)+' '+word_list[0])
    # print(keywords)
    return keywords


# count score
def score_counter(keywords,point,sum):
    point = point
    sum = sum
    # read dictionary
    dic = get_dic('./dic/dictionary.csv')
    for word in keywords:
        word_list = word.split(',')
        # print(word_list)
        if word_list[0] in dic:
            point = dic[word_list[0]]
        else:
            continue
        print(str(point)+' '+word_list[0])
        point = int(point)
        # print(type(point))
        sum += point
        # print(str(sum)+' = '+str(sum-point)+'+('+str(point)+')')
    return point, sum




# read dictionary
def get_dic(input_dic):
    negaPoji_dic = {}
    with open(input_dic) as f:
    # with open(input_dic,encoding = 'cp932') as f: # delite BOM by insert 'encoding'
        data = csv.reader(f)
        for i, x in enumerate(data):
            y = x[0].strip()
            z = x[1].strip()
            negaPoji_dic.setdefault(y, z) # add to dictionary
    # print(negaPoji_dic)
    # print(negaPoji_dic['気になる'])
    return negaPoji_dic



# read review
def get_review(input_file):
    texts = []
    count = 0
    for text_path in input_file:
        count += 1
        point = 0
        sum =0
        files = open(text_path, 'r').read()
        files = files.split('\n')
        print('\n')
        print(text_path)
        for text in files:
            texts.append(nlp(text))
            point, sum = score_counter(nlp(text),point,sum)
        # print('\n')
        print(sum)

        with open('./review/star5_comp.csv','a')as f:
            writer = csv.writer(f)
            writer.writerow(['レビュー'+str(count), sum])
        f.close()

    # print(texts)
    # print('\n')
    return texts



# run
def main():
    review_list = get_review(text_paths)

if __name__ == '__main__':
    main()






# chasen = MeCab.Tagger("-Ochasen -d /usr/local/lib/mecab/dic/mecab-ipadic-neologd")
# wakati = MeCab.Tagger("-Owakati -d /usr/local/lib/mecab/dic/mecab-ipadic-neologd")
# result_c = chasen.parse(text)
# result_w = wakati.parse(text)
# print(result_c)
# print(result_w)
