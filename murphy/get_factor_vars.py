SECTION_BREAK = "------------------------------------------------------------------------------------------\n"

sum = 0
vars = []
descs = []
with open("../data/codebook.txt", 'r') as codebook:
    line = codebook.readline()
    isTab = True
    while(line):
        if (isTab): line = codebook.readline()
        if (line == SECTION_BREAK):
            var = codebook.readline()
            varName = var[0:14].rstrip()
            varDesc = var[15:].strip().replace(" ", "_")
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
                    vars.append(varName)
                    descs.append(varDesc)
                    isTab = True
                    break
        
with open("factor.txt", "w") as f:
    print("\n".join(vars), file = f)


