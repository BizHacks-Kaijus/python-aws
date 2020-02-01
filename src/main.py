import boto3; 

s3 = boto3.client('s3')

def main(): 
    upload()

def upload():
    documentKey = input()
    bucketName = "bizhacks2020"
    outputName = documentKey
    s3.upload_file(documentKey, bucketName, outputName)

main()