import boto3
#function to delete an S3 bucket given the bucket_name
def delete_bucket(bucket_name):
    try:
        s3=boto3.resource('s3')
        s3.Bucket(bucket_name).delete()

    except TypeError as t:
        if(type(bucket_name)!=str):
            s3.Bucket(bucket_name).delete()
        else:
            print("Type ERROR")

    except Exception as e:
        print("deletebucket.py delete_bucket() function, lines5-6")
        print(e)
        return False

#function to delete all S3 buckets
def delete_all():
    s3 = boto3.resource('s3')
    buckets = [bucket for bucket in s3.buckets.all()]
    for bucket in buckets:
        try:
            delete_bucket(bucket_name=bucket)
        except TypeError as t:
            delete_bucket(bucket_name=bucket.name)
        except:
            assert(False)
    assert(True)
