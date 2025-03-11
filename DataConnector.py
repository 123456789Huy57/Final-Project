from fileinput import filename

from Final.ios.JsonFileFactory import JsonFileFactory
from Final.Models.Client import Client
from Final.Models.PersonalTrainer import PersonalTrainer
from Final.Models.Location import Location
from Final.Models.User import User

class DataConnector:
    def get_all_client(self):
        jff = JsonFileFactory()
        filename = "../Dataset/Client.json"
        clients = jff.read_data(filename, Client)
        return clients
    def get_all_personaltrainer(self):
        jff = JsonFileFactory()
        filename = "../Dataset/PersonalTrainer.json"
        pts = jff.read_data(filename, PersonalTrainer)
        return pts
    def get_all_location(self):
        jff = JsonFileFactory()
        filename = "../Dataset/Location.json"
        locate = jff.read_data(filename, Location)
        return locate
    def get_all_user(self):
        jff = JsonFileFactory()
        filename="../Dataset/User.json"
        user=jff.read_data(filename,User)
        return user

    def login(self,username,password,Locateid):
        clients=self.get_all_client()
        for e in clients:
            if e.Username==username and e.Password==password and e.Locateid==Locateid:
                return e
        return None