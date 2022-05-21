import phonenumbers
from phonenumbers import timezone, geocoder, carrier

number = input('Enter the phone number 📱 >>> ')
phonenumber = phonenumbers.parse(number)

timezone = timezone.time_zones_for_number(phonenumber)

carrier = carrier.name_for_number(phonenumber, 'en')

COUNTRY = geocoder.description_for_number(phonenumber, 'en')


if __name__ == "__main__":
    print(phonenumber)
    print("Time Zone : " + str(timezone))
    print("COUNTRY : " + COUNTRY)
    print("Issued by SIM : " + carrier)
    print("\U0001F92B" + "N" + u'\u2620' + "I" + u'\u2620' + "P" + u'\u2620' + "U" + u'\u2620' + "N" + u'\u2620' + "A")
