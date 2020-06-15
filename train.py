from gensim.models import word2vec

data = word2vec.Text8Corpus('data/jawiki_wakachi.txt')

model = word2vec.Word2Vec(data, size=100)

model.save('model/jawiki.model')