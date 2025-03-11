from Final.ios.JsonFileFactory import JsonFileFactory
from Final.Models.Client import Client

jff=JsonFileFactory()
filename="../Dataset/Client.json"
clients=jff.read_data(filename,Client)
print("List of Client")
for a in clients:
    print(a)