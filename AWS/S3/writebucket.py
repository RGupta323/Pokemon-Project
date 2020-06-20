#Script to create text files and write random strings on a text file
#then to give write that into a bucket
import boto3
from AWS.S3.createbucket import *
import os
'''
This is a script that has functions to upload files to a bucket (write_bucket()) and download files from a given bucket 
(read_bucket()). 

For testing purposes, it has helping functions to create a random txt file with a randomly generated name (create_file()) 
and generates a random string to put on that file (generate_content()). 

Main functions: 
    write_bucket() is a function to upload files to an S3 bucket 
    read_bucket() is a function to download a file from an S3 bucket 

main() is a function used for testing purposes. 
'''
#this is giong to be where the txt fiels are stored, this is mine.

#function to create a file from scratch.
'''
Function to create a file and writes a given string into it. 
rtInputs (Params): 
    fileName is a string that specifies the name of the file. 
    the extension must be included (ie .txt must be included to create a file called 
    test.txt) 
    content is a string that specifies the string (with new line characters!) to be written in the text file
    
Logic: 
    Pretty simple, open the file, write teh content, close it. 
    Catch any errors and print them out. 
    
Output: 
    Return True if everything worked! 
    Return false if any errors. 
'''
def create_file(fileName,content):
    try: 
        f=open(fileName, 'w')
        f.write(content)
        f.close()
        print("Successfully Create File!")
        return True
    except Exception as e:
        print("Error writing and create txt file. create_file() function")
        print(e);
        return False


#function to write bucket given a name and a file.
#this is to upload a file into a bucket
'''
Function to upload a file to a S3 bucket. 

Inputs (params): 
    bucket_name which is a string that specifies the bucket_name (remember this must be unique!) 
    file is a string that specifies the absolute path of where the file is located locally 
    file_name is a string that specifies the name of the file (the file extension must be included!) 
        ie file_name="test.txt" 

Logic: 
     Call the upload file() function from s3 
     print out any errors, and return false 
     return true if there are no problems. 

Outputs: 
    True if there are no errors. 
    False if there are, print any error messages. 
'''
def write_bucket(bucket_name,file,file_name):
    s3=boto3.client('s3')
    try:
        s3.upload_file(file,bucket_name,Key=file_name);
        print("Successfully written bucket!")
        return True;
    except TypeError as t:
        print(t);
        if(type(file)!=str):
            print("file variable type: "+str(type(file)))
            return False;
        if(type(bucket_name)!=str):
            print("bucket_name type: "+str(type(bucket_name)))
            return False;
        print("All inputs look good")
    except Exception as e:
        print("ERROR. write_bucket() function")
        print(e);
        return False;

#function to download a file from a bucket
'''
Inputs(params): 
    file is a string that specifies the absolute path of a file (where it should be place once its downlaoded! 
    bucket_name is a string htat specifies the bucket_name 
    file_name is a string that specifies the name of the file (the file extension must be included!) 
    
Logic: 
    Yeah its not rocket science, I called the download_file() function on using boto3 
    
Output: 
    True if there are no errors 
    False if there are, error messages and exception messages will be printed. 
'''
def read_bucket(bucket_name,file, file_name):
    try:
        s3=boto3.client('s3',aws_access_key_id = "AKIA3NCGCBMDCRU2ZI75",aws_secret_access_key = "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")
        print("Downloading file")
        s3.download_file(bucket_name,file, file_name);
    except TypeError as t:
        print(t);
        if(type(file)!=str):
            print("file variable type: "+str(type(file)))
            return False;
        if(type(bucket_name)!=str):
            print("bucket_name type: "+str(type(bucket_name)))
            return False;
        if(type(file_name)!=str):
            print("file_name type: "+str(type(file_name)))
            return False;
        print("All inputs look good")
    except Exception as e:
        print(e);
        print("ERROR: writebucket.py, read_bucket() function, lines 58-60")
        return False;

#function to generate random string to put on a file
'''
Function to generate a random string to write to a file

Inputs: 
    numLines is an integer that specifies the numbe rof lines that string needs to be. 
    
Logic: 
    generates a random string to write into a txt file. 
    
Output: 
    returns a string
'''
def generate_content(numLines):
    newstr=""
    for i in range(numLines):
        choice=random.randint(0,1)
        if(choice==0):
            newstr+=generate_str(random.randint(1,20))
        else:
            newstr+="\n"
    return newstr

#default method to test write_bucket()
#generates a random txt file with random text in it, and makes a bucket and tries to upload that file into the bucket
def main():
    s3=boto3.resource('s3')
    while(True): 
        try: 
            numLines=random.randint(1,10)
            #generating random file name and random string to put into file
            fileName,content=generate_str(length=10),generate_content(numLines)
            #creating a file
            f=create_file(baseurl+fileName,content)
            bucket_name=generate_str(10)
            #checking to see if there are any s3 buckets created
            if(len([bucket for bucket in s3.buckets.all()])==0):
                print("going to create a bucket")
                bucket_name=create_bucket()
            else:
                buckets=[bucket for bucket in s3.buckets.all()]
                bucket_name=buckets[random.randint(0,len(buckets)-1)]
            #writing bucket
            return write_bucket(bucket_name=bucket_name,file=baseurl+"\\"+fileName+".txt")
        except Exception as e:
            print("ERROR WITH main()")
            print(e)
             


    
