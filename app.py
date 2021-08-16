import pickle5 as pickle
import pandas as pd
import numpy as np
import re
from model import RecommendationModel
from scipy import sparse
from flask import Flask

app = Flask(__name__)
model = RecommendationModel()
#load kmeans clustering model, co-occurence matrix, pivot_productId for cooccurence matrix, preprocessed data, count vectorizer
model.clusteringModel = pd.read_pickle("models/kmeansmodel.pkl")
model.cooccurence = sparse.load_npz("models/cooccurence.npz")
model.productid_index = pd.read_pickle("models/productid_index.pkl")
model.df_meta = pd.read_pickle("models/df_meta_lemma.pkl")
model.vectorizer=pd.read_pickle("models/count_vectorizer.pkl")

#@app.route('/recomendations', defaults={'ids' :'HBV00000AX6LR-HBV00000JUHBA-HBV00000NE0UQ-HBV00000P7W3K'})
@app.route("/api/v1.0/recommendations/<string:ids>", methods=["GET"])
def get_recomendations(ids):
    ids = re.sub(r'-', ' ',ids).split()
    print(ids,"-------------------------------------------")
    df=pd.DataFrame();
    #make recommendations. tries to recommend circa 10 items which uniformly distributed for each item in the cart. If there is 5 items in the cart then each of them will have 2 recommended items
    # If there are 4 items in the cart then each of them will have 2.5~3 recommended items 
    for id in ids:
         df= pd.concat([df, model.predict(id).head(10//len(ids))])
    df.reset_index(drop=True, inplace=True)
    #df=df.drop('cooccurance',axis=1)
    print(df)
    return df.to_json(orient="table")

if __name__ == "__main__":
    app.run(debug=True)
    
