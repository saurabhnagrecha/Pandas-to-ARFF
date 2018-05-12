# pandas2arff

A quick and dirty script to transform a pandas dataframe into a [Weka](https://www.cs.waikato.ac.nz/ml/weka/)-friendly ARFF file. While Weka has limited capabilities for practical use, it is a good first foray into data mining and can be effective as a teaching tool.


## Features

- Create an ARFF dump file from an existing pandas dataframe
- Imports column names straight from the pandas dataframe
- 'Object' dtype in pandas is treated as 'nominal'
- If your dataframe has a column called "Class" / "class" / "CLASS", then this code automatically makes it a nominal value
- Cleans up NaNs, dirty strings, etc.

## Usage

```python
pandas2arff(df, filename, wekaname="pandasdata", cleanstringdata=True, cleannan=True)
```

where,

- `df`: dataframe in pandas format (flattened, no groupings)
- `filename`: the filename you want the Weka compatible file to be in
- `wekaname`: the name you want to give to the Weka dataset (this will be visible to you when you open it in Weka)
- `cleanstringdata`: clean up data which may have spaces and replace with `"_"`, special characters, etc. which seem to annoy Weka. To suppress this, set this to `False`.
- `cleannan`: replaces all `NaN` values with `"?"`, which is Weka's standard for missing values. To suppress this, set this to `False`.

## Quick Example

Using the sample files,

```python
# import pandas as pd
df = pd.read_csv("foo.txt", na_values="NA")
pandas2arff(df, "foo.arff")
```

Literally just these two lines!

## What's not supported (yet)

- dates as variables
- any other popular use-cases you might suggest!

## License
MIT License

Copyright (c) [2015] [Saurabh Nagrecha]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
