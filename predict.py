from gensim.models import word2vec

model = word2vec.Word2Vec.load("model/jawiki.model")

r = model.most_similar(positive='Linux')
print(r)

r = model.most_similar(positive='Mac')
print(r)

r = model.most_similar(positive='ラーメン')
print(r)

r = model.most_similar(positive=['甘い', 'カレー'])
print(r)

r = model.most_similar(positive=['王様', '女性'], negative=['男性'])
print(r)