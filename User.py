

class User:
    def __init__(self,ID=None,First_Name=None,Last_Name=None,Gender=None,Username=None,Password=None):
        self.ID=ID
        self.First_Name=First_Name
        self.Last_Name=Last_Name
        self.Gender=Gender
        self.Username=Username
        self.Password=Password
    def __str__(self):
        return f"{self.ID}\t{self.First_Name}\t{self.Last_Name}\t{self.Gender}\t{self.Username}\t{self.Password}"