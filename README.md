# Bulk Regex Comparison Tool
A Tool to compare bulk regex patterns against bulk data. 

The tool was built specifically to compare regex to be included as listners in Proxy or CDN against the actual urls which had to be redirected or routed as per the setup.

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

#### 1.Clone The Repository
```
git clone git@github.com:ananthkamath/BRCT.git && cd BRCT
```

#### 2.Input Patterns
Update the pattern_list.xlsx with all available patterns to be matched against

#### 3.Input Data
Update the url_list.xlsx with all test urls or test data

#### 4.Run The Script
```
python3 regexcomparescript.py
```
If any libraries are missing use `pip` Python package manager.
