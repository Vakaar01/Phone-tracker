import phonenumbers
from phonenumbers import timezone, geocoder, carrier

number = input ("enter your number  +91 :•  ")
phone=phonenumbers.parse(number)
t = timezone.time_zones_for_number(phone)
c = carrier.name_for_number(phone,"en")
r = geocoder.description_for_number(phone, "en")

print(t)
print(c)
print(r)