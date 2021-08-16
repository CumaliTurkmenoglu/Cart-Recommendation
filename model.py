from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
import re
import math
import numpy as np
from scipy import sparse

class RecommendationModel(object):

    def __init__(self):
        """Attributes:
            clusteringAlgorithm: sklearn kmeans
            vectorizor: Count vectorizer
        """
        self.clusteringModel = KMeans()
        self.vectorizer = CountVectorizer(ngram_range=(1,2),min_df=3, max_df=0.02)
        self.df_meta=pd.DataFrame()
        self.productid_index=pd.DataFrame()
        self.cooccurence=pd.DataFrame()
     # Get all item id'sin the same cluster with  the item requested
    def getCluster(self, index):
        cluster_map = pd.DataFrame()
        cluster_map['productid'] = self.df_meta['productid']
        cluster_map['cluster'] = self.clusteringModel.labels_
        return cluster_map[cluster_map['cluster']==index]
    def predict(self, id):
        """Returns the top recommendation for each product id
        """
        #print(self.df_meta[self.df_meta['productid']==id]['name'], "*************************************************")
        #vectorize the current item with its product name+" "+category+""+subcategory
        y = self.vectorizer.transform(self.df_meta[self.df_meta['productid']==id]['name']+' '+self.df_meta[self.df_meta['productid']==id]['category']+''+ self.df_meta[self.df_meta['productid']==id]['subcategory'])
        #predict the cluster of the vectorized item
        prediction = self.clusteringModel.predict(y)
        #self.productid_index includes the item-item pivot table indexes and productids , self.cooccurence includes item-item cooccurence numbers
        #get the sorted cooccured items for current productid
        sorted_indexes_cooccurence=np.argsort(-1*self.cooccurence[self.productid_index[self.productid_index['productid']==id]['index']].todense())
        sorted_values_cooccurence=-1*np.sort(-1*self.cooccurence[self.productid_index[self.productid_index['productid']==id]['index']].todense())
        #sort productid_index based on current porduct id and its cooccurance items        
        sorted_productid_index=self.productid_index.loc[sorted_indexes_cooccurence.tolist()[0]]
        sorted_productid_index["cooccurence"] = sorted_values_cooccurence.tolist()[0]
        #add a value eg:2 for each item that fell in the same cluster with the current product. By this approach we guaranttee that 
        #there will be related items(within same cluster) recommended when there is no enough cooccurence for the current product
        # The most effective metric is the cooccurence of products withing cart history. On the other hand my approach gives more importance to items that fell in the same cluster  and help them to appear in reccommendation
        sorted_productid_index["cooccurence"] = np.where(sorted_productid_index["productid"].isin(self.getCluster(prediction[0])['productid'].tolist()),sorted_productid_index["cooccurence"]+1,sorted_productid_index["cooccurence"])
        #sort whole dataset based on cooccurance values with current product 
        df_merged=pd.merge(self.df_meta,sorted_productid_index.set_index('index'),on='productid',how="left").loc[sorted_productid_index[sorted_productid_index['productid'].isin(self.df_meta['productid'])]['index']]
        df_merged['item_name_recommended_for']=self.df_meta[self.df_meta['productid']==id]['name'].values[0]
        df_merged=df_merged[df_merged['productid']!=id]
        df_merged['item_id_recommended_for']=id
        df=df_merged.sort_values('cooccurence', ascending=False).reset_index(drop=True)
        return df.head(10)
