import unittest

import boto3
from AWS.S3.src.createbucket import *
from AWS.S3.src.writebucket import *
'''
This is a file that contains test cases for other random tests, just to mess around. 
Not seriously testing functions.                                                  
'''

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

    def test_test1(self):
        s3=boto3.resource('s3')
        bucket_name=generate_str(10)
        #create a bucket
        self.assertTrue(create_bucket(bucket_name))
        bucket_name=[bucket for bucket in s3.buckets.all()][0]
        #now upload a file
        baseurl_downloads = "C:\\Users\gupta\\AWSPractice\\AWSPractice\\S3Bucket\\filesdownloaded\\"
        baseurl_uploads = "C:\\Users\\gupta\\AWSPractice\\AWSPractice\\S3Bucket\\Samplehtmlfiles\\"
        fileName,content=generate_str(10),generate_content(10)
        #upload_file= f = create_file(baseurl_uploads + fileName+".txt", content)
        self.assertEqual(write_bucket(bucket_name=bucket_name, file=baseurl_uploads+"sample.html", file_name="sample.html"),True)
        self.assertEqual(write_bucket(bucket_name=bucket_name, file=baseurl_uploads+"sampleerror.html", file_name="sampleerror.html"),True)
        #now download these files
        self.assertEqual(read_bucket(bucket_name=bucket_name.name, file=baseurl_downloads+"sample.html", file_name="sample.html"),True)
        self.assertEqual(read_bucket(bucket_name=bucket_name.name, file=baseurl_downloads+"sampleerror.html", file_name="sampleerror.html"),True)
    def test_test2(self):
        s3=boto3.resource('s3')
        bucket_name = [bucket for bucket in s3.buckets.all()][0]
        print(bucket_name.name)
        baseurl_downloads = "C:\\Users\gupta\\AWSPractice\\AWSPractice\\S3Bucket\\filesdownloaded\\"
        baseurl_uploads = "C:\\Users\\gupta\\AWSPractice\\AWSPractice\\S3Bucket\\Samplehtmlfiles\\"
        self.assertEqual(
            read_bucket(bucket_name=bucket_name.name, file=baseurl_downloads + "sample.html", file_name="sample.html"), True)
        self.assertEqual(read_bucket(bucket_name=bucket_name.name, file=baseurl_downloads + "sampleerror.html",
                                     file_name="sampleerror.html"), True)



if __name__ == '__main__':
    unittest.main()
