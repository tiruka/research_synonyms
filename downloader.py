import logging
import os

import requests

logger = logging.getLogger(__name__)

class DownloadError(Exception):
    pass

def download(url, fn, dir_path, logger):
    fp = os.path.join(dir_path, fn)
    logger.info("Donwloding to {} from {}".format(fp, url))
    res = requests.get(url, stream=True)
    if res.status_code != 200:
        raise DownloadError
    with open(fp, 'wb') as f:
        for chunk in res.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
    return fp


if __name__ == "__main__":
    JA_WIKIPEDIA_DATA_URL = "https://dumps.wikimedia.org/jawiki/latest/jawiki-latest-pages-articles.xml.bz2"
    file_name = "jawiki-latest-pages-articles.xml.bz2"
    dir_path = "data"
    download(JA_WIKIPEDIA_DATA_URL, file_name, dir_path, logger)