# research_synonyms

Researching synonyms using natural language processing (NLP)

Creating corpas based on Wikipedia Data ans utlizing Word2Vec to predict new synonyms.

## Setup

1. Download Wikipedia data from `https://dumps.wikimedia.org`. If you will use Japanese and the latest one, you can use `donwloader.py` and store it in `data` the directory. The size is over 2GB.
2. Insall ruby and execute `gem install wp2txt` in order to convert wikipedia data into text data. If your computer is mac, you can skip this step and make it sure it is installed by `ruby -v` to see the installed ruby version. If necesssary, please add `sudo` to deal with permission errors.
3. Donwload Mecab from `https://drive.google.com/uc?export=download&id=0B4y35FiV1wh7cENtOXlicTFaRUE` and IPA dictionary from `https://drive.google.com/uc?export=download&id=0B4y35FiV1wh7MWVlSDBCSXZMTXM`. If you can donwload it in any ways (cURL, wget, using browser) and put it on `mecab` directory of this project. Those are linked from `https://taku910.github.io/mecab/`.
4. Build and install mecab as the below. If you already installed it using other tools such as brew, you can skip the step of insalling mecab, but should execute commands for ipa dictionary.

```.sh
tar zxfv mecab-X.X.tar.gz
cd mecab-X.X
./configure
make
make check
sudo make install

tar zxfv mecab-ipadic-2.7.0-XXXX.tar.gz
cd mecab-ipadic-2.7.0-XXXX
./configure --with-charset=utf8
make
make check
sudo make install
```

5. If you are interested in new word(neologism), you can add NEologd from `https://github.com/neologd/mecab-ipadic-neologd`. Execute the below commands in `mecab` dir. You can see details at README of the github.

```.sh
git clone --depth 1 https://github.com/neologd/mecab-ipadic-neologd.git
./mecab-ipadic-neologd/bin/install-mecab-ipadic-neologd -n
# Please enter yes for [install-mecab-ipadic-NEologd] : Do you want to install mecab-ipadic-NEologd? Type yes or no
```

6. Unarchive wikipedia data like the below with `bunzip2` (taking you a long time).

```.sh
bunzip2 jawiki-latest-pages-articles.xml.bz2
```

7. Execute `wp2txt` by the below command.

```.sh
wp2txt --input-file jawiki-latest-pages-articles.xml
```

8. Concatenate all jawiki-latest-pages-articles-*.txt into one file and make wakachi file(txt).

```.sh
cat jawiki-latest-pages-articles-*.txt >> all_jawiki-latest-pages-articles.txt
mecab -b 100000 -O wakati all_jawiki-latest-pages-articles.txt -o jawiki_wakachi.txt
```

9. Train and save the wrod2vec model by running the below command.

```.sh
python train.py
```

10.  You can predict and fetch similar words with commands like `python predict.py -p ラーメン 甘い -n 辛い`.
If the word does not exist in vocabulary, the program returns KeyError.
