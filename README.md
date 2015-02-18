# pandas2arff
- Create an ARFF string from an existing pandas dataframe

- Imports column names straight from the pandas dataframe

- 'Object' dtype in pandas is treated as 'nominal'

- If your dataframe has a column called "Class" / "class" / "CLASS", then this code automatically makes it a nominal value

usage:

```
pandas2arff(df, filename = 'outputFile.arff',name = "mypandasdata")
```

where,

df: your pandas dataframe,

filename: your ARFF format output file

name: the stuff which goes after "@relation"
