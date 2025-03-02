import re

class InvalidPhoneNumberError(Exception):
    pass

def check(pnumber):
    pattern = r'\b7[(]?\d{3}[)]?\d{3}[-]?\d{2}[-]?\d{2}\b'
    if re.match(pattern, pnumber):
        return pnumber
    else:
        return InvalidPhoneNumberError("Некорректный номер телефона.")
    
#7(841)717-25-45
#78417172545
#7(841)7172545
pnumber = input("Введите номер: ")
try:
    valid_number = check(pnumber)
    print(f"Корректный номер: {valid_number}")
except InvalidPhoneNumberError as e:
    print(e)