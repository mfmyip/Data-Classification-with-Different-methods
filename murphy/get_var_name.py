import pandas as pd

SECTION_BREAK = "------------------------------------------------------------------------------------------\n"

sum = 0
vars = []
descs = []
with open("../data/codebook.txt", 'r') as codebook:
    line = codebook.readline()
    isTab = True
    while(line):
        line = codebook.readline()
        if (line == SECTION_BREAK):
            var = codebook.readline()
            varName = var[0:14].rstrip()
            varDesc = var[15:].strip().replace(" ", "_")
            vars.append(varName)
            descs.append(varDesc)
            # dump 2 lines
            codebook.readline() # -----...
            codebook.readline() # empty ln

df = pd.DataFrame({
    'vars': vars, 'desc': descs
})

df.to_csv("variables.csv", index=False)    

