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
    banter = {'to': 'gjclaridge@gmail.com', 'link': landmarkURL,'image':landmarkImage, 'landmark':landmark}
    r = requests.post("http://jrbradley.co.uk:8002/", data=banter)

#an example email
# sendEmail("poo@poo.com","Cabbages",
# "http://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Cabbage_and_cross_section_on_white.jpg/300px-Cabbage_and_cross_section_on_white.jpg",
# "http://en.wikipedia.org/wiki/Cabbage")

"""Gets a random wikipedia page and emails the user details about it
@Params:
        email(string): email address of the user
"""
def sendRandomEmail(email):
    r = requests.get("http://en.wikipedia.org/wiki/Special:Random")


    link = r.text.split('<link rel="canonical" href="')
    link = link[1].split('"')
    print link[0]

    image = r.text.split('<img')
    image = image[1].split('/>')
    image = image[0].split('src="')
    #print image[1],"\n"
    image = image[1].split('"')
    #print image[0],"\n"
    image = image[0].split("//")
    #print image[1],"\n"
    image = image[1]
    #print image


    title = r.text.split('"wgTitle":"')
    title = title[1].split('","')
    #print title[0]

    sendEmail(email,title[0],image,link[0])
