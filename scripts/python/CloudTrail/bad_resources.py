import boto3

# Simular errores para monitoreo
client = boto3.client('ec2')
try:
    # Crear una instancia con parámetros inválidos
    response = client.run_instances(
        ImageId='ami-invalid',
        InstanceType='t2.micro',
        MinCount=1,
        MaxCount=1
    )
except Exception as e:
    print(f"Error esperado: {e}")
