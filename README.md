# cdi_cardinality

Prints the cardinality of each column of a csv file.

## Installation

```
sudo pip3 isntall https://github.com/plainas/cdi_cardinality/zipball/master
```

This package is not listed in python package index (pypy). I do **not** intend to submit it. This code is shared as is. If you would like to have this available on pypi or if you would like a certain feature, you are encouraged to fork this project.

## usage

```
cdi_cardinality [-h] [-m MAX] [-n] [-v] filename
```

Examples:

```
> cdi_cardinality towed-vehicles.csv
Tow_Date 91
Make 76
Style 33
Model 69
Color 26
Plate 4025
State 39
Towed_to_Address 5
Tow_Facility_Phone 7
Inventory_Number 4816
```

Column names will have spaces replaced by underscores for easier integration with other command line tools such as awk, sed, grep, etc.

For readability by humans, the `-v` or `--valign` switch can be helpful.

```
> cdi_cardinality -v towed-vehicles.csv
Tow_Date           91
Make               76
Style              33
Model              69
Color              26
Plate              4025
State              39
Towed_to_Address   5
Tow_Facility_Phone 7
Inventory_Number   4816
```

Memory usage is a linear function of column cardinality. If you are working with very large files you can mitigate this problem by setting an upper limit for cardinality which will prevent filling up the memory with new values once the given limit is reached for each colum.

This is achieved by passing a `-m` or `--max` parameter. 

```
>cdi_cardinality -v -m 100  towed-vehicles.csv
Tow_Date           91
Make               76
Style              33
Model              69
Color              26
Plate              100
State              39
Towed_to_Address   5
Tow_Facility_Phone 7
Inventory_Number   100
```

Notice that the columns `Plate` and `Inventory_Number` display the specified maximum rather than their actual cardinality.


## Command arguments

```
positional arguments:
  filename

optional arguments:
  -h, --help         show this help message and exit
  -m MAX, --max MAX  Specify maximum count value.
  -n, --no-header    Read values from the first line of the input. Use this is
                     the input has no header.
  -v, --valign       Vertically align columns on the output for beter human
                     readability
```

