from Final.Models.User import User

class Client(User):
    def __init__(self, ID=None, First_Name=None, Last_Name=None, Gender=None, Username=None, Password=None, TypeofPt=None, Branch=None, Schedule=None):
        super().__init__(ID, First_Name, Last_Name, Gender, Username, Password)
        self.TypeofPt = TypeofPt
        self.Branch = Branch
        self.Schedule = Schedule

    def __str__(self):
        return f"{super().__str__()}\t{self.TypeofPt}\t{self.Branch}\t{self.Schedule}"
