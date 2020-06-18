from datetime import datetime
import glob
import os
import shutil
import logging

from gensim.models import word2vec

formatter = '%(levelname)s : %(asctime)s : %(message)s'
logging.basicConfig(level=logging.INFO, filename='log/train.log', format=formatter)
logger = logging.getLogger(__name__)


def pre_process():
    logger.info('Preprocess to move trained files')
    model_files = glob.glob(os.path.join('model', '*'))
    past_model_files = glob.glob(os.path.join('past_model', '*'))
    if not model_files:
        logger.info('No files exist in model directory')
        return
    d = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    dir_path = os.path.join('past_model', d)
    os.makedirs(dir_path, exist_ok=False)
    for file in model_files:
        if os.path.exists(file):
            shutil.move(file, dir_path)
    logger.info('Preprocess done')

def create_model():
    logger.info('Training started')
    data = word2vec.Text8Corpus('data/jawiki_wakachi.txt')
    model = word2vec.Word2Vec(data, sg=1, size=100, min_count=1, window=5)
    model.save('model/jawiki.model')
    logger.info('Training ended')

def main():
    pre_process()
    create_model()

if __name__ == "__main__":
    main()