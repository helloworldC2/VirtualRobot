import random
names = ["Adam","Ben","Joel","Rikki","Aaron","George","Dave","Dickbutt","Pierre","Antonetta","Priscilla","Jarrod","Andree","Flo","Bart","Glayds","Abel","Alex","Jettie","Cherelle","Tami","Lindsey","Joannie","Natacha","Betty","Margarite","Sima","Charlott","Providencia","Zack","Corinne","Celinda","Jerome","Dovie","Valrie","Serena","Gwen","Christal","Terrell","Aldo","April","Else","Jarvis","Fanny","Takako","Fidel","Patty","Lorinda","Tomoko","Twyla","Kiana","Khadijah","Luz","Chantal","Latasha","Dania","Shameka","Ed"]

def getRandomName():
    return names[random.randint(0,len(names)-1)]
