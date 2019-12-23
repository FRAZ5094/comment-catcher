#Comment Catcher
#By Christopher Di-Nozzi

#This script uses regex to look for html, css and js style comments within a webpage.
#I made this for ease in CTF type challenges and to practice python a little.

def commentCatcher(url):
    #a url needs atleast http to work with urllib2, so this checks if http:// or https:// are at the start on the string
    #if they aren't, http:// is appended to the front
    if url[0:7]!="http://" and url[0:8]!="https://":
        url = "http://" + url
        print "[*]http:// appended to front of URL."
        print "[*]New URL: ",url


    print "[*]Searching ",url,"..."
    try:
        response = urllib2.urlopen(url)
    except urllib2.HTTPError as err:
        print "[-]", err
        return None
    except urllib2.URLError as err:
        print "[-]", err
        return None

    content = response.read()
    
    result = re.findall("<!--.*-->",content) + re.findall("//.*$",content) + re.findall("/\*.*\*/",content)

    if len(result)==0:
        print "[-]No comments found."
    else:
        print "[+]",len(result)," comment(s) found."
        for x in result:
            print "[+]",x

def fileHandle(fileName):
    file = open(filename,"r")
    fileline = file.readlines()
    for x in fileline:
        commentCatcher(x)

def help():
    ascii_banner = pyfiglet.figlet_format("Comment Catcher")
    print ascii_banner
    print "By Christopher Di-Nozzi"
    print "Version:", version
    print ""
    print "This script searches a webpage for html,css and js style comments. It can take a URL or .txt file with URLs in it as an arg."
    print ""
    print "Usage:"
    print "\tcommentcatcher.py -u URL"
    print "\tcommentcatcher.py -f FILE"
    print ""
    print "Example:"
    print "\tcommentcatcher.py -u http://google.com"
    print "\tcommentcatcher.py -f urls.txt"

    sys.exit()

import urllib2,re,getopt,sys

import pyfiglet

version = 0.2

#handle command line arguments
options, remainder = getopt.getopt(sys.argv[1:], 'u:f:h')

for opt, arg in options:
    if opt in ('-u', '--url'):
        commentCatcher(arg)
    elif opt in('-f','--file'):
        filename = arg
        fileHandle(filename)
    elif opt in ('-h', '--help'):
        help()

sys.exit()