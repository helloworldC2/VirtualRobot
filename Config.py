"""File used to load in config info to be used in the program
"""


"""Variables to be saved and loaded
"""
config = {"email":"",
        "receiveEmail":"",
        "difficulty":"",
        "numAI":"",
        "name":"",
        
}

"""Loads the config file and stores the data in config(dict)
@Params:
        None
@Return:
        config(dict)
"""
def loadConfig():
    file = open("config",'r')
    data = file.read()
    data = data.split("\n")
    for d in data:
        d = d.split(": ")
        try:
            try:
                config[d[0]] = int(d[1])#load as int
            except ValueError:
                if d[1]=="True" or d[1]=="False":
                    if d[1]=="True":config[d[0]]=True
                    if d[1]=="False":config[d[0]]=False#load as boolean
                else:
                    config[d[0]] = d[1]#load as string
        except IndexError:
            pass

    return config

"""Saves config(dict) to config file
@Params:
        None
@Return:
        None
"""
def saveConfig():
    f = open('config','w')
    for key, value in config.iteritems():
        f.write(key+": "+str(value)+'\n')
        print key+": "+str(value)
    f.close()
