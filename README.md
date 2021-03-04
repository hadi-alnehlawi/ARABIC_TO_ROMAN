# Arabic To Roman Function

## Introduction

This function is an implementation of a code problem to convert Arabic numbers to Roman numerals using the "standard" subtraction notation (https://en.wikipedia.org/wiki/Roman_numerals).

The numerals are positive and don’t exceed 3999 in absolute value:

arabic_number: [1..3999]

## Implementation

The algorithm for this funciton is decmposing the arabic number into its several decimal digits from highest to lowest.

This is implemented by storing the decimal digits into a list, and for each list items is mapped to its Roman equivalent numeral.

## Run

### Docker

As a requisite a docker must be installed

The docker will create a persisted image of which might be tagged with a name **arabic_to_roman**.

```
$ docker --version
$ cd ./ARABIC_TO_ROMAN
$ docker build --tag arabic_to_roman .
```

Running the container as below would be automatically purged after closing

`$ docker run --rm -ti arabic_to_roman`

### Manually

As a perquisite virtualenv package might be installed

If not, please visit this [pypi](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/) tutorial for more clarification. Follow the below commands in sequence

```
$ virtualenv --version
$ cd ./ARABIC_TO_ROMAN
$ virtualenv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

Running the application will prompt to input the arabic number which is required to be converted to Roman numberals. If the input was not valid the function will return the message with an error description.

`$ python app.py`

## Test

In order to run the test script, please execute the following:

```
$ cd ./ARABIC_TO_ROMAN
$ pytest
```

## Note

The input must be number only without any dots or commas

- 2,410 must be entered 2410 without comma
- 151.00 must be entered 151 wihtout dot

Otherwise, comman and dot would be considered as strings and would return not a valid arabic number message
