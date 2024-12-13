import time
import aws_xray_sdk.core

aws_xray_sdk.core.patch_all()


def handler(event, context):
    time.sleep(10)
    return {"statusCode": 200, "body": "X-Ray Latency Test"}
