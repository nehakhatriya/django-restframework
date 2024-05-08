from algoliasearch_django import algolia_engine

def get_client():
    return algolia_engine.client
def get_index(index_name="Product"):
    client=get_client()
    index=client.init_index(index_name)
    return index

def perform_search(query,**kwargs):
    index=get_index()
    params={}
    index_filters=[f'{k}:{v}' for k,v in kwargs.items() if v]
    print(index_filters)
    if len(index_filters)!=0:
        params['facetFilters']=index_filters
    return index.search(query,params)

