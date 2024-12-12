import boto3
cloudwatch = boto3.client('cloudwatch')

for _ in range(1000):  # Publica muchas métricas en poco tiempo
    cloudwatch.put_metric_data(
        Namespace='TestMetrics',
        MetricData=[{
            'MetricName': 'HighLoad',
            'Value': 100
        }]
    )
