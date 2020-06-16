import argparse

from gensim.models import word2vec

parser = argparse.ArgumentParser()
parser.add_argument('-p', '--positive', type=str, nargs='*', help='positive words')
parser.add_argument('-n', '--negative', type=str, nargs='*', help='negative words')

args = parser.parse_args()
positive = args.positive
negative = args.negative

model = word2vec.Word2Vec.load("model/jawiki.model")

result = model.most_similar(positive=positive, negative=negative)
print('positive words:', positive)
print('negative words:', negative)
print('result')
for r in result:
    print(r)