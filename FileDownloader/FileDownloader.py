from bs4 import BeautifulSoup
import sys
import requests
from urllib.parse import urlparse

def is_valid_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False
    

def get_links(url):
    if not is_valid_url(url):
        print("Please double check if you have put in the correct url.")
        return "Incorrect input. Exit program."
    else:
        r = requests.get(url)
        contents = r.content

        soup = BeautifulSoup(contents, features="html.parser")
        links = soup.findAll('a')

        # From all links check for pdf link and
        # if present download file
        i = 0
        for link in links:
            if ('.ppt' or '.pdf' in link.get('href', [])):
                i += 1
                filename = link.get('href')
                print("Downloading file " + str(i) + ": " + filename)

                # Get response object for link
                filePath = url + filename
                response = requests.get(filePath)
        
                # Write content in ppt file
                ppt = open(filename, 'wb')
                ppt.write(response.content)
                ppt.close()
                print("File " + filename + " downloaded")
        
        if i == 0:
            return "Sorry, no files found in this webpage. Exit program."
        
        return "Hooray!! All " + str(i) + " files have been downloaded!"
    


if __name__ == "__main__":
    url = input("Welcome to file downloader (～￣▽￣)～ \nPlease paste your destination url here: ")
    # url = "https://www.softwarearchitecturebook.com/svn/main/slides/ppt/"
    print(get_links(url))
    sys.exit()