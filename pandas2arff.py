def pandas2arff(df,name = "pandasdata",filename):
    f = open(filename,"w")
    arffList = []
    arffList.append("@relation " + name + "\n")
    #look at each column's dtype. If it's an "object", make it "nominal" under Weka for now (can be changed in source for dates.. etc)
    for i in range(df.shape[1]):
        if df.dtypes[i]=='O' or df.columns[i]=="Class" or df.columns[i]=="CLASS" or df.columns[i]=="class":
            _uniqueNominalVals = [str(_i) for _i in np.unique(df.iloc[:,i])]
            _uniqueNominalVals = ",".join(_uniqueNominalVals)
            _uniqueNominalVals = _uniqueNominalVals.replace("[","")
            _uniqueNominalVals = _uniqueNominalVals.replace("]","")
            _uniqueValuesString = "{" + _uniqueNominalVals +"}"
            arffList.append("@attribute " + df.columns[i] + _uniqueValuesString + "\n")
        else:
            arffList.append("@attribute " + df.columns[i] + " integer\n")
    arffList.append("@data\n")
    for i in range(df.shape[0]):#instances
        _instanceString = ""
        for j in range(df.shape[1]):#features
                if df.dtypes[j]=='O':
                    _instanceString+="\"" + (df.iloc[i,j]) + "\""
                else:
                    _instanceString+=str(df.iloc[i,j])
                if j!=df.shape[1]:#if it's not the last feature, add a comma
                    _instanceString+=","
        _instanceString+="\n"
        arffList.append(_instanceString)
    f.writelines(arffList)
    f.close()
    return True
