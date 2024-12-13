import boto3
import time

# Simula solicitudes repetidas a una API para rastreo
client = boto3.client('xray')
for i in range(100):
    response = client.put_trace_segments(
        TraceSegmentDocuments=['{"trace": "test-segment"}']
    )
    time.sleep(0.1)
