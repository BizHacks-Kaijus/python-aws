import boto3;
import json;

s3 = boto3.client('s3')
max_labels = 10
min_confidence = 90
rekog = boto3.client('rekognition', region_name='us-east-1')

# analyze(path-to-image, description-of-product)
def analyze(img, desc): 
	upload(img)
	for label in detect_labels(img):
		print("{Name} - {Confidence}%".format(**label))
	comprehend = boto3.client('comprehend', region_name='us-east-1')

	#text = "The Lenovo T420 is a high performance business class notebook with a second gen Intel i5 processor, 4GB of Ram and a 320 GB HDD. This high quality, refurbished notebook is perfect for any computing environment, including at home for personal use or small and medium sized businesses looking to expand their fleet at a reasonable price point. The Lenovo T420 is built with high quality tier 1 components and has been professionally refurbished to ensure you?re getting a unit in Grade A condition. This desktop includes a 1 year warranty and is fully loaded with a Windows 10 Pro operating system."
	text = desc
	print('Detecting key phrases')

	print(json.dumps(comprehend.detect_key_phrases(Text=text, LanguageCode='en'), sort_keys=True, indent=4))

	print('End of DetectKeyPhrases\n')

def upload(img):
    documentKey = img
    #docName = documentKey
    bucketName = "bizhacks2020"
    outputName = documentKey
    s3.upload_file(documentKey, bucketName, outputName)

def detect_labels(img):
    response = rekog.detect_labels(
        Image = {
            "S3Object": {
                "Bucket": "bizhacks2020",
                "Name": img
            }
        }
    )
    MaxLabels = max_labels
    MinConfidence=min_confidence
    return response['Labels']
