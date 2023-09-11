import json
import os
import boto3
import botocore
import pytesseract
from PIL import Image

#static variables
s3 = boto3.resource('s3')
BUCKET_NAME = 'image-upload-test-via-apigw' # replace with your bucket name
KEY = 'jpn-text-img.png' #replace with your key name
img_dir = '/tmp/my_local_image.jpg'
def lambda_handler(event, context):
    #download img from S3 and place image in /tmp as my_local_image.jpg
    try:
        s3.Bucket(BUCKET_NAME).download_file(KEY, img_dir)
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "404":
            print("The object does not exist.")
        else:
            raise

    #pytesseract image to String
    text = pytesseract.image_to_string(Image.open(img_dir), lang='jpn') #change lang to 'eng', 'due', 'jpn' as desired. If you need other Languages, make sure to add them in the Dockerfile. (language packs can be seen between line 28-32 in the Dockerfile)
    print(text)
    
    response = {
        "statusCode": 200,
        "body": json.dumps("Hello")
    }

    return response