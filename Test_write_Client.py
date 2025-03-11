from Final.ios.JsonFileFactory import JsonFileFactory
from Final.Models.Client import Client

clients=[]
clients.append(Client("E1","Tèo","Nguyễn","Male","nguyenteo","111","Newbie","HCM"))
clients.append(Client("E2","Tý","Nguyễn","Male","nguyenteo","111","Newbie","HCM"))
clients.append(Client("E3","Bin","Trần","Male","nguyenteo","111","Newbie","HCM"))
clients.append(Client("E4","Bo","Trần","Male","nguyenteo","111","Newbie","HN"))
clients.append(Client("E5","Bủn","Lê","Female","nguyenteo","111","Newbie","HN"))
clients.append(Client("E6","Rủn","Lê","Female","nguyenteo","111","Newbie","HCM"))
jff=JsonFileFactory()
filename="../Dataset/Client.json"
jff.write_data(clients,filename)