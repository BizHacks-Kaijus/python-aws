import boto3; 

s3 = boto3.client('s3')

def main(): 
    upload()

def upload():
    documentKey = input()
    docName = documentKey
    bucketName = "bizhacks2020"
    outputName = documentKey
    s3.upload_file(documentKey, bucketName, outputName)

rekog = boto3.client('rekognition', region_name='us-east-1')

docName = "2.jpg"
max_labels = 10
min_confidence = 60

def detect_labels():
    response = rekog.detect_labels(
        Image = {
            "S3Object": {
                "Bucket": "bizhacks2020",
                "Name": docName
            }
        }
    )
    MaxLabels = max_labels
    MinConfidence=min_confidence
    return response['Labels']

main()
for label in detect_labels():
    print("{Name} - {Confidence}%".format(**label))
