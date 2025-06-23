import pyshorteners
import pyshorteners.shorteners

def short_url(long_url):

    shortner = pyshorteners.Shortener()
    return shortner.tinyurl.short(long_url)

url = input("Enter a long url: ")
print(short_url(url))