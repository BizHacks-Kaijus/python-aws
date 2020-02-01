import boto3

import json

comprehend = boto3.client('comprehend', region_name='us-east-1')

text = "The Lenovo T420 is a high performance business class notebook with a second gen Intel i5 processor, 4GB of Ram and a 320 GB HDD. This high quality, refurbished notebook is perfect for any computing environment, including at home for personal use or small and medium sized businesses looking to expand their fleet at a reasonable price point. The Lenovo T420 is built with high quality tier 1 components and has been professionally refurbished to ensure you?re getting a unit in Grade A condition. This desktop includes a 1 year warranty and is fully loaded with a Windows 10 Pro operating system."
print('Detecting key phrases')

print(json.dumps(comprehend.detect_key_phrases(Text=text, LanguageCode='en'), sort_keys=True, indent=4))

print('End of DetectKeyPhrases\n')