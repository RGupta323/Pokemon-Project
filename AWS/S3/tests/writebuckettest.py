import unittest
from AWS.S3.src.writebucket import *;
'''
A file that contains junit tests to test the functions in writebucket.py 
To be honest, it mainly tests the write_bucket() function and read_bucket() functions. 
'''
class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)
    def test_writebucket(self):
        s3 = boto3.resource('s3')
        numLines = random.randint(1, 10)
        # generating random file name and random string to put into file
        fileName, content = generate_str(length=10), generate_content(numLines)
        print("fileName: "+str(fileName))
        # creating a file
        baseurl = "C:\\Users\\gupta\\AWSPractice\\AWSPractice\\S3Bucket\\txtfiles"
        f = create_file(baseurl + "\\"+fileName+".txt", content)
        bucket_name = generate_str(10)
        # checking to see if there are any s3 buckets created
        print([bucket for bucket in s3.buckets.all()])
        if (len([bucket for bucket in s3.buckets.all()]) == 0):
            print("going to create a bucket")
            bucket_name = create_bucket()
        # if there exists a bucket then upload to an existing bucket
        else:
            buckets = [bucket for bucket in s3.buckets.all()]
            bucket_name = buckets[random.randint(0, len(buckets) - 1)]
        print(str(bucket_name.name))
        #self.assertEqual(type(bucket_name),str)
        #bucket_name=str(bucket_name)
        # writing bucket
        self.assertEqual(write_bucket(bucket_name=bucket_name.name, file=baseurl+"\\"+fileName + ".txt", file_name=fileName+".txt"), True)
    #test to test function read_bucket(), to download files from a bucket
    def test_readbucket(self):
        pass;
if __name__ == '__main__':
    unittest.main()
