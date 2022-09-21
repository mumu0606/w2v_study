import numpy as np
from modules import get_poke_vector
import json

type2Group = {
    "ノーマル": "1",
    "ほのお": "2",
    "みず": "3",
    "でんき": "4",
    "くさ": "5",
    "こおり": "6",
    "かくとう": "7",
    "どく": "8",
    "じめん": "9",
    "ひこう": "10",
    "エスパー": "11",
    "むし": "12",
    "いわ": "13",
    "ゴースト": "14",
    "ドラゴン": "15" 
}

# cos類似度を計算
def cos_sim(v1, v2):
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))


# ポケモン名を与えたら、d3で描画できるようなデータ形式で各ポケモンとの類似度を計算する
# @param name String
# @return
"""
{
    nodes: [
            {
                "id": "フシギダネ",
                "group": 1
            },
            {
                "id": "フシギソウ",
                "group": 1
            },
            {
                "id": "フシギバナ",
                "group": 1
            },
    ],
    linkes: [
            {
                "source": "フシギダネ",
                "target": "フシギソウ",
                "value": 43.58393298762299
            },
            {
                "source": "フシギダネ",
                "target": "フシギバナ",
                "value": 28.26313119009859
            },
    ]
}

"""
def get_similars(name, pokeVectorDic):
    print('____name____')
    print(name)
    print(pokeVectorDic)
    targetVec = pokeVectorDic[name]['vector']
    result = {
        "nodes": [],
        "links": []
    }
    for comparisonName, comparisonData in pokeVectorDic.items():
        result['nodes'].append({"id": comparisonName, "group": 1})
        # ターゲットポケモンのときはなにもしない
        if name == comparisonName:
            continue
        result["links"].append({"source": comparisonName, "target": name, "value": pow((1 - cos_sim(targetVec, comparisonData['vector'])), 1) * 100})
    return result


def get_similars_with_type(name, pokeVectorDic):
    print('____name____')
    print(name)
    targetVec = pokeVectorDic[name]['vector']
    result = {
        "nodes": [],
        "links": []
    }
    for comparisonName, comparisonData in pokeVectorDic.items():
        # タイプごとにグループきる
        result['nodes'].append({"id": comparisonName, "group": type2Group[comparisonData['type']]})
        # ターゲットポケモンのときはなにもしない
        if name == comparisonName:
            continue
        result["links"].append({"source": comparisonName, "target": name, "value": pow((1 - cos_sim(targetVec, comparisonData['vector'])), 1) * 100})
    return result