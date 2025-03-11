from Final.Models.User import User

class PersonalTrainer(User):
    def __init__(self, ID=None, First_Name=None, Last_Name=None, Gender=None, Username=None, Password=None, Experience=None, TypeofPt=None, Branch=None):
        super().__init__(ID, First_Name, Last_Name, Gender, Username, Password)
        self.Experience = Experience
        self.TypeofPT = TypeofPt
        self.Branch = Branch

    def __str__(self):
        return f"{super().__str__()}\t{self.Experience}\t{self.TypeofPT}\t{self.Branch}"
