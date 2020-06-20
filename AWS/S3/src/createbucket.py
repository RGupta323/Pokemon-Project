import boto3
import random
'''
This is a python file with functions to create a bucket in S3. 
The main function is called create_bucket()
The generate_str() function is to simply generate a random string of a given length, which is a helperfunction 
create_bucket can be called as: create_bucket() and if no bucket name is given then a bucket name will randomly 
generated. 
'''
#Script to create a bucket 
#function to generate bucket name
def generate_str(length):
    alpha="abcdefghijklmnopqrstuvxyz"
    alpha+="0123456789"
    newstr=""; 
    for i in range(length):
        r=random.randint(0,len(alpha)-1)
        newstr+=alpha[r]
    return newstr

'''
This function creates an S3 bucket on AWS

Inputs: 
    bucket_name is an optional param which is a string that signifies the name of a bucket 
    If nothing is given then a bucket_name will be generated. 

Logic: 
    create a bucket, print any errors. 

Output: 
    True if it works, no problem and a print message saying so. 
    False if there are any errors, printed out. 
'''
def create_bucket(bucket_name=None):
    try:
        s3 = boto3.resource('s3')
        #generate bucket name
        if (bucket_name == None):
            bucket_name = generate_str(length=10)
        print("bucket name: " + str(bucket_name))
        #create bucket
        s3.create_bucket(Bucket=bucket_name,
                         CreateBucketConfiguration={'LocationConstraint': 'us-east-2'})
        print("Successfully created an S3 Bucket!")
        return True;

    except Exception as e:
        print("ERROR")
        print(e);
        return False;

        
        
