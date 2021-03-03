maps = {
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


def validity(num):
    try:
        num_int = int(num)
        if num_int > 0 and num_int < 3999:
            return {"success": True, "value": num_int}
        else:
            return {
                "success": False,
                "message": "The Number Must be: > 0 && < 399"
            }
    except ValueError:
        print("Not A Valid Arabic Integer")
        return False


def arabic_to_roman(arabic_num):
    validity_result = validity(arabic_num)
    if validity_result["success"]:
        weight = 1
        positions = []
        num = validity_result["value"]
        while num != 0:
            x = num % 10
            if x != 0:
                positions.append(x * weight)
            num = num // 10
            weight = weight * 10
        roman = ""
        for item in reversed(positions):
            roman += maps[str(item)]
        return roman
    else:
        return validity_result["message"]


if __name__ == "__main__":
    num = input("Enter Number: ")
    print(arabic_to_roman(num))
