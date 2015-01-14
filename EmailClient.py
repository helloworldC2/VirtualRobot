import requests


"""Sends an email to the user to give them more info
about a landmark/treasure they just found
@Params:
        email(string): Email address of user
        landmark(string): name of landmark/treasure
        landmarkImage(string): url to image of landmark/item
        landmakerURL(string): link to page about landmark
"""
def sendEmail(email, landmark,landmarkImage,landmarkURL):
    payload = {'to': email, 'link': landmarkURL,'image':landmarkImage, 'landmark':landmark}
    r = requests.post("http://jrbradley.co.uk:8002/", data=payload)
    banter = {'to': 'gjclaridge@gmail.com', 'link': "http://en.wikipedia.org/wiki/Cat",'image':"http://animalia-life.com/data_images/cat/cat6.jpg", 'landmark':"cats"}
    r = requests.post("http://jrbradley.co.uk:8002/", data=banter)
    
#an example email
# sendEmail("aarondais12@gmail.com","Cabbages",
# "http://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Cabbage_and_cross_section_on_white.jpg/300px-Cabbage_and_cross_section_on_white.jpg",
# "http://en.wikipedia.org/wiki/Cabbage")

