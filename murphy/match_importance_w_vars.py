import pandas as pd
import sys 

def debugger_is_active() -> bool:
    """Return if the debugger is currently active"""
    gettrace = getattr(sys, 'gettrace', lambda : None) 
    return gettrace() is not None

# debugger has directory from KAGGLE PROJECT folder
HOMEPATH = "./murphy/" if debugger_is_active() else ""

imp = pd.read_csv(HOMEPATH + "randomforest/importance.csv")
vars = pd.read_csv(HOMEPATH + "variables.csv")

merged = pd.merge(imp, vars, left_on='vars', right_on='vars', how = 'left')
merged.to_csv(HOMEPATH + "randomforest/importance_w_desc.csv", index=False)