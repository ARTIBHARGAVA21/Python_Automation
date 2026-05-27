import sys
import webbrowser


URLS ={ 
       "work" : ["www.slack.com", "www.google.com"],
       "personal": ["https://docs.python.org/3/library/webbrowser.html", "https://www.youtube.com/watch?v=w-X_EQ2Xva4&t=4051s", "https://open.spotify.com/"]}


def openwebpages(urls):
    for url in urls:
        print(url)
        webbrowser.open(url)
        
        
if __name__=="__main__":
    set_name=sys.argv[1]
    urls =URLS[set_name]
    openwebpages(urls)
    