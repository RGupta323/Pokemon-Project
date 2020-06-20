import random
import unittest
import boto3

from S3Bucket.src.createbucket import create_bucket, generate_str
from S3Bucket.src.deletebucket import delete_bucket


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

    def test_deletebucket(self):
        s3=boto3.resource('s3')
        buckets=[bucket for bucket in s3.buckets.all()]
        if(len(buckets)==0):
            bucket_name=generate_str(10)
            create_bucket(bucket_name=bucket_name)
        else:
            bucket_name=buckets[random.randint(0,len(buckets)-1)].name

        delete_bucket(bucket_name=bucket_name)


if __name__ == '__main__':
    unittest.main()
