from opencage.geocoder import OpenCageGeocode 
from phonenumbers import geocoder
import phonenumbers as pn
key = 'f80bebba838942ffb8c57ea58337f82d'

myNumber = pn.parse('+8801714008696', 'bd')

location = geocoder.description_for_number(myNumber,'en')

print(location)






geocoder = OpenCageGeocode(key)

query = location
result = geocoder.geocode(query)

print(result)