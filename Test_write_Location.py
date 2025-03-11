from Final.ios.JsonFileFactory import JsonFileFactory
from Final.Models.Location import Location
locate = []
locate.append(Location("123 Street, HCM", "HCM"))
locate.append(Location("456 Road, HN", "HN"))
jff = JsonFileFactory()
filename="../Dataset/Location.json"
jff.write_data(locate,filename)
