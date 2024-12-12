import boto3
import yaml
import os

# Convertir Jenkinsfile a YAML para CloudFormation
def jenkinsfile_to_yaml():
    # Simulación del contenido YAML
    pipeline_yaml = {
        "Resources": {
            "CodePipeline": {
                "Type": "AWS::CodePipeline::Pipeline",
                "Properties": {
                    "RoleArn": "arn:aws:iam::123456789012:role/CodePipelineRole",
                    "ArtifactStore": {
                        "Type": "S3",
                        "Location": "my-codepipeline-bucket"
                    },
                    "Stages": [
                        {
                            "Name": "Source",
                            "Actions": [
                                {
                                    "Name": "SourceAction",
                                    "ActionTypeId": {
                                        "Category": "Source",
                                        "Owner": "AWS",
                                        "Provider": "S3",
                                        "Version": "1"
                                    },
                                    "Configuration": {
                                        "S3Bucket": "my-codepipeline-bucket",
                                        "S3ObjectKey": "source.zip"
                                    },
                                    "OutputArtifacts": [{"Name": "SourceArtifact"}]
                                }
                            ]
                        },
                        {
                            "Name": "Build",
                            "Actions": [
                                {
                                    "Name": "BuildAction",
                                    "ActionTypeId": {
                                        "Category": "Build",
                                        "Owner": "AWS",
                                        "Provider": "CodeBuild",
                                        "Version": "1"
                                    },
                                    "Configuration": {
                                        "ProjectName": "MyCodeBuildProject"
                                    },
                                    "InputArtifacts": [{"Name": "SourceArtifact"}],
                                    "OutputArtifacts": [{"Name": "BuildArtifact"}]
                                }
                            ]
                        },
                        {
                            "Name": "Deploy",
                            "Actions": [
                                {
                                    "Name": "DeployAction",
                                    "ActionTypeId": {
                                        "Category": "Deploy",
                                        "Owner": "AWS",
                                        "Provider": "CodeDeploy",
                                        "Version": "1"
                                    },
                                    "Configuration": {
                                        "ApplicationName": "MyApplication",
                                        "DeploymentGroupName": "MyDeploymentGroup"
                                    },
                                    "InputArtifacts": [{"Name": "BuildArtifact"}]
                                }
                            ]
                        }
                    ]
                }
            }
        }
    }
    return pipeline_yaml


# Crear un bucket S3
def create_s3_bucket(bucket_name):
    s3 = boto3.client('s3')
    s3.create_bucket(Bucket=bucket_name)
    print(f"Bucket {bucket_name} creado.")

# Subir YAML a S3
def upload_to_s3(bucket_name, file_name, data):
    s3 = boto3.client('s3')
    with open(file_name, 'w') as f:
        yaml.dump(data, f)
    s3.upload_file(file_name, bucket_name, file_name)
    print(f"Archivo {file_name} subido a S3.")


# Crear el pipeline con CloudFormation
def deploy_cloudformation_stack(stack_name, template_file):
    cf = boto3.client('cloudformation')
    with open(template_file, 'r') as f:
        template_body = f.read()
    cf.create_stack(
        StackName=stack_name,
        TemplateBody=template_body,
        Capabilities=['CAPABILITY_NAMED_IAM']
    )
    print(f"Stack {stack_name} creado.")

# Configuración inicial
bucket_name = "my-codepipeline-bucket"
yaml_file = "codepipeline_template.yaml"
stack_name = "MyCodePipelineStack"

# Pasos principales
if __name__ == "__main__":
    # Convertir Jenkinsfile a YAML
    yaml_data = jenkinsfile_to_yaml()

    # Crear un bucket S3
    create_s3_bucket(bucket_name)

    # Subir el archivo YAML a S3
    upload_to_s3(bucket_name, yaml_file, yaml_data)

    # Crear el pipeline desde CloudFormation
    deploy_cloudformation_stack(stack_name, yaml_file)
