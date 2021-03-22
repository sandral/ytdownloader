from html.parser import HTMLParser
from urllib.parse import urlparse, urlencode
from urllib.request import urlopen, Request
from urllib.error import HTTPError
from pytube import YouTube
link = input("videon osoite: ")
yt = YouTube(link)
#Title of video
print("Title: ", yt.title)
#Number of views
print("Number of views: ", yt.views)
#Length of video
print("Length of video : ", yt.length, "seconds")
#Description of video
print("Description: ", yt.description)
#Ratings
print("Ratings: ", yt.rating)
#print streams
print(yt.streams.filter(progressive=True))
ys = yt.streams.get_highest_resolution()

print("Ladataan...")
ys.download('/home/sandra/ytdownloads')
print("Lataus valmis")