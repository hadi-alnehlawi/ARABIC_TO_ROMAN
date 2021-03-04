decimal_places = {
    "1": "I",
    "2": "II",
    "3": "III",
    "4": "IV",
    "5": "V",
    "6": "VI",
    "7": "VII",
    "8": "VIII",
    "9": "IX",
    "10": "X",
    "20": "XX",
    "30": "XXX",
    "40": "XL",
    "50": "L",
    "60": "LX",
    "70": "LXX",
    "80": "LXXX",
    "90": "XC",
    "100": "C",
    "200": "CC",
    "300": "CCC",
    "400": "CD",
    "500": "D",
    "600": "DC",
    "700": "DCC",
    "800": "DCCC",
    "900": "CM",
    "1000": "M",
    "2000": "MM",
    "3000": "MMM"
}


# helper function to validate the user input
def validity(num):
    '''
    Input: arabic number as a string from the user input
    Output: a dictionary which contains of validation bool flag along with an int value of the arabic string input
    '''
    try:
        num_int = int(num)
        if num_int > 0 and num_int < 4000:
            # validation is True and return the int valud of input
            return {"success": True, "value": num_int}
        else:
            return {
                # validation is False and the input is out of accepted range for roman convertion
                "success": False,
                "message": "The Number Must Be Between 1 && 3999"
            }
    except ValueError:
        return {
            #  validation is False and is not valid arabic number
            "success": False,
            "message": "Not A Valid Arabic Integer"
        }


# convertion function
def arabic_to_roman(arabic_num):
    '''
    Input:  * the arabic number to be converted into roman numberal using the standard form.
            * it must be between 1 && 3999.
    Output: * if input is valid, its roman numberal is returned.
            * Otherwise, return a message with the error description.
    '''
    validity_result = validity(arabic_num)
    if validity_result["success"]:
        weight = 1
        positions = []
        num = validity_result["value"]
        # get its several decimal digits from highest to lowest
        while num != 0:
            x = num % 10
            if x != 0:
                positions.append(x * weight)
            num = num // 10
            weight = weight * 10
        roman = ""
        # map each item into its equavalent roman numberal
        for item in reversed(positions):
            roman += decimal_places[str(item)]
        # success
        return roman
    else:
        # failed
        return validity_result["message"]

# app implementation
if __name__ == "__main__":
    # input of the arabic number 
    num = input("Enter Number: ")
    # call the function and print the result
    print(arabic_to_roman(num))
