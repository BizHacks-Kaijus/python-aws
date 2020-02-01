import boto3

rekog = boto3.client('rekognition')

docName = "1.png"
max_labels = 10
min_confidence = 90

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

for label in detect_labels():
    print("{Name} - {Confidence}%".format(**label))