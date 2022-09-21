import MeCab
from gensim.models import KeyedVectors
import numpy as np
import json

mt = MeCab.Tagger('')
mt.parse('')
wv = KeyedVectors.load_word2vec_format('./wiki.vec.pt', binary=True)

# テキストのベクトルを計算
def get_vector(text):
    sum_vec = np.zeros(200)
    word_count = 0
    node = mt.parseToNode(text)
    while node:
        fields = node.feature.split(",")
        # 名詞、動詞、形容詞に限定
        if fields[0] == '名詞' or fields[0] == '動詞' or fields[0] == '形容詞':
            # 作ったモデルに単語がない場合もある
            if node.surface in wv:
                sum_vec += wv[node.surface]
            word_count += 1
        node = node.next

    return sum_vec / word_count


def get_poke_vector():
    pokeVectorDic = {}
    with open('./modules/picture_book.json') as f:
        pictureBook = json.load(f)

    
    for name, data in pictureBook.items():
        pokeVector = get_vector(data['comment'])
        pokeVectorDic[name] = {
            "vector": pokeVector,
            "type": data['type']
        }
    
    return pokeVectorDic