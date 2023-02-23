import phonenumbers
from Locate_Text import number, Ink
from phonenumbers import geocoder
ch_num1 = phonenumbers.parse(number, "CH")   # C country, H history
ch_num2 = phonenumbers.parse(Ink, "CH")   # C country, H history

from phonenumbers import carrier
service_num1 = phonenumbers.parse(number, "RO")
print("Phone number1: ", geocoder.description_for_number(ch_num1, "en"))    # en Language English
print("Service provider1: ", carrier.name_for_number(service_num1, "en"))
print("\b")

service_num2 = phonenumbers.parse(Ink, "RO")
print("Phone number2: ", geocoder.description_for_number(ch_num2, "en"))    # en Language English
print("Service provider2: ", carrier.name_for_number(service_num2, "en"))
