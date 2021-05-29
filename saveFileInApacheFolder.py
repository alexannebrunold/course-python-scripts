import os

name_of_file = input("Name of file: ")
completeNameOfFile = '/var/log/apache2' + name_of_file + ".txt"
file1 = open(completeNameOfFile , "w")
toFile = input("Write what you want here")
file1.write(toFile)
file1.close()