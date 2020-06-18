import argparse
from datetime import datetime
import logging

from gensim.models import word2vec

formatter = '%(levelname)s : %(asctime)s : %(message)s'
logging.basicConfig(level=logging.INFO, filename='log/predict.log', format=formatter)
logger = logging.getLogger(__name__)

parser = argparse.ArgumentParser()
parser.add_argument('-p', '--positive', type=str, nargs='*', help='positive words')
parser.add_argument('-n', '--negative', type=str, nargs='*', help='negative words')

args = parser.parse_args()
positive = args.positive
negative = args.negative

model = word2vec.Word2Vec.load("model/jawiki.model")
logger.info('Loaded model')

result = model.most_similar(positive=positive, negative=negative)
logger.info('Predicted model')
print('positive words:', positive)
print('negative words:', negative)
print('result')
for r in result:
    print(r)