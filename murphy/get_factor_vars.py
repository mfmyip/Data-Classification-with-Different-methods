import pandas as pd
import sys 

SECTION_BREAK = "------------------------------------------------------------------------------------------\n"

sum = 0
vars = []
descs = []

df_ret = pd.DataFrame(columns=['var_code', 'var_desc', 'isTabulated'])

with open("data/codebook.txt", 'r') as codebook:
    line = codebook.readline()
    isTab = True
    while(line):
        if (isTab): line = codebook.readline()
        if (line == SECTION_BREAK):
            var = codebook.readline()
            df_temp = pd.DataFrame(
                [[var[0:14].rstrip(), var[15:].strip().replace(" ", "_"), False]],
                columns=['var_code', 'var_desc', 'isTabulated'])
            df_ret = pd.concat([df_ret, df_temp], axis = 0, ignore_index = True)
            # dump 2 lines
            codebook.readline() # -----...
            codebook.readline() # empty ln
            # find "Tabulation"
            varLine = codebook.readline()
            while(varLine):
                varLine = codebook.readline()
                if varLine == SECTION_BREAK:
                    isTab = False
                    break
                if "Tabulation:" in varLine:
                    sum += 1
                    isTab = True
                    df_ret.iloc[-1, 2] = isTab
                    break

df_ret.to_csv("data/variables.csv", index = False)


