#
# Read and write files using the built-in Python file methods
#

# No need to import anything for files

def main():  
  # Open a file for writing and create it if it doesn't exist
  # w means with write access and + means create file if not existing
  # other modes: a - append, r - read
  f = open("textFile.txt", "w+")

  # Open the file for appending text to the end


  # write some lines of data to the file
  for i in range(1, 11):
    f.write("This is line no " + str(i) + "\r\n")

  
  # close the file when done
  f.close()

  
  # Open the file back up and read the contents
  f = open("textfile.txt","r")
  
  # read all contents of file at once
  if(f.mode == "r"):
    # content = f.read()
    # print("Reading all content")
    # print(content)

  # read content line by line (in case of large file)
    fl = f.readlines()
    print("Reading line by line content")
    for content in fl:
      print(content)
  

    
if __name__ == "__main__":
  main()
