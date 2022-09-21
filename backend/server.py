import uvicorn
from fastapi import FastAPI
from modules import get_poke_vector
import modules.get_similar as get_similar
import pprint
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
pokeVectorDic = get_poke_vector.get_poke_vector()

@app.get('/similar') # URI / にGETリクエストが来たときの処理
def getSimilarJson(name: str):
    pprint.pprint(name)
    similarDic = get_similar.get_similars(name, pokeVectorDic)
    print(similarDic)
    return similarDic

@app.get('/similar_with_type')
def getSimilarWithTypeJson(name: str):
    pprint.pprint(name)
    similarDic = get_similar.get_similars_with_type(name, pokeVectorDic)
    print(similarDic)
    return similarDic

if __name__ == '__main__': #コンストラクタ
    uvicorn.run(app)