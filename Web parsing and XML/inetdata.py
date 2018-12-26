# 
# Example file for retrieving data from the internet
#

import urllib.request
def main():
  url = urllib.request.urlopen("https://www.google.com")
  print("Url provided is: " + str(url.getcode())) #getcode() returns the status code 200 - OK, 404 - Not Found etc

  data = url.read() # read data from url
  print(data)

if __name__ == "__main__":
  main()
