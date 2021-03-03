# Arabic To Roman Function

## Introduction

This function is an implementation of a code problem to convert Arabic number to Roman Numeral using the "standard" subtraction notation (https://en.wikipedia.org/wiki/Roman_numerals).

The numerals are positive and don’t exceed 3999 in absolute value:

arabic_number: [0..399]

## Implementation

The algorithm for this funciton is decmposing the arabic number into its several decimal digits from highest to lowest.

This is implemented by storing the decimal digits into a list. Then the list items mapped to its Roman equivalent numerals for each.

## Run

### Docker

As a requisite a docker must be installed:

```
$ docker --version
```

The docker will create a persisted image of which might be tagged with a name **arabic_to_roman**.
Running the container as below would be automatically purged after closing

```
$ cd ./ARABIC_TO_ROMAN
$ docker build --tag arabic_to_roman .
$ docker run --rm -ti arabic_to_roman
```

### Manually

As a perquisite virtualenv package might be installed

`$ virtualenv --version`

If not, please visit this [pypi](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/) tutorial for more clarification. Follow the below commands in sequence:

```
$ cd ./ARABIC_TO_ROMAN

$ virtualenv venv

$ source venv/bin/activate

$ python app.py

```

It will prompt to input the arabic number which is required to be converted to Roman numberals. If the input was not valid the function will return the message with an error description.

## Test

In order to run the test script, please execute the following:

```
$ cd ./ARABIC_TO_ROMAN
$ pytest
```
