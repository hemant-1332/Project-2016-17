import urllib

def read_text():
    quotes= open("quote.txt")
    contents=quotes.read()
    #print(contents)
    quotes.close()
    check_profanity(contents)

def check_profanity(text):
    connection = urllib.urlopen("http://www.wdyl.com/profanity?q=" + text)
    output = connection.read()
    connection.close()

    if "true" in output:
        print ("profane word found")
    elif "false" in output:
        print ("No curse word!!")
    else :
        print ("could not scan")

read_text()
