#!/usr/bin/env python
import sys

BUCKET = sys.argv[1]

import boto3

s3 = boto3.resource('s3')
bucket = s3.Bucket(BUCKET)
bucket.object_versions.delete()