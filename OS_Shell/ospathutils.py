#
# Example file for working with os.path module
#
import os
from os import path
import datetime
from datetime import date, time, timedelta
import time


def main():
  # Print the name of the OS
  print(os.name)


  # Check for item existence and type
  print("Item exists?: ", str(path.exists("textFile.txt")))
  print("Is item a file?: ", str(path.isfile("textFile.txt")))
  print("Is item a directory?: ", str(path.isdir("textFile.txt")))

  
  # Work with file paths
  print("Real path is: ", str(path.realpath("textFile.txt")))

  
  # Get the modification time
  t = time.ctime(path.getmtime("textfile.txt"))
  print (t)
  print (datetime.datetime.fromtimestamp(path.getmtime("textfile.txt")))
  
  # Calculate how long ago the item was modified
  td= datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime("textfile.txt"))
  print ("It has been " + str(td) + " since the file was modified")
  print ("Or, " + str(td.total_seconds()) + " seconds")
  
if __name__ == "__main__":
  main()
