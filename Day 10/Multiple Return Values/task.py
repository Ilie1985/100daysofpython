def format_name(f_name, l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


print(format_name("romeo", "fantastik"))

def canBuyAlcohol(age):
    if age >= 18:
        return True
    else:
        return False
print(canBuyAlcohol(18))


def canBuyAlcohol(age):
    # If the data type of the age input is not an int, then exit.
    if type(age) != int:
        return

    if age >= 18:
        return True
    else:
        return False
print(canBuyAlcohol("two"))