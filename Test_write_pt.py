from Final.ios.JsonFileFactory import JsonFileFactory
from Final.Models.PersonalTrainer import PersonalTrainer

pts=[]
pts.append(PersonalTrainer("E1","Tèo","Nguyễn","Male","nguyenteo","111","10 Years","Gym","HCM"))
pts.append(PersonalTrainer("E2","Tý","Nguyễn","Male","nguyenteo","111","5 Years","Gym","HCM"))
pts.append(PersonalTrainer("E3","Bin","Trần","Male","nguyenteo","111","3 Years","Gym","HCM"))
pts.append(PersonalTrainer("E4","Bo","Trần","Male","nguyenteo","111","2 Years","Gym","HCM"))
pts.append(PersonalTrainer("E5","Bủn","Lê","Female","nguyenteo","111","1 Years","Yoga","HN"))
pts.append(PersonalTrainer("E6","Rủn","Lê","Female","nguyenteo","111","5 Years","Yoga","HN"))
jff=JsonFileFactory()
filename="../Dataset/PersonalTrainer.json"
jff.write_data(pts,filename)