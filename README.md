# pandas2arff
- Create an ARFF string from an existing pandas dataframe

- Imports column names straight from the pandas dataframe

- 'Object' dtype in pandas is treated as 'nominal'

- If your dataframe has a column called "Class" / "class" / "CLASS", then this code automatically makes it a nominal value

usage:

```
f = open("outputFile.arff","w")
f.writelines(pandas2arff(df, name = "mypandasdata"))
f.close()
```

where
    df: your pandas dataframe

    name: the stuff which goes after "@relation"
