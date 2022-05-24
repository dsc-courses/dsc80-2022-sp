# Note to students – you shouldn't change this file at all,
# it is just meant to help the autogradertest your code

from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer


def get_transformers(pl, translist=()):
    
    translist = []
    
    is_coltrans = False
    if isinstance(pl, Pipeline):
        trans = pl.named_steps.values()
    elif isinstance(pl, ColumnTransformer):
        is_coltrans = True
        trans = pl.named_transformers_.values()
    else:
        return [pl]
    
    for tr in trans:
        translist.append(get_transformers(tr))
    if is_coltrans:
        translist.append([pl])
        
    return sum(translist, [])
