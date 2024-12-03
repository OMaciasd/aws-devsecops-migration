import boto3
import json

# Initialize AWS SDK clients
codepipeline_client = boto3.client('codepipeline')
iam_client = boto3.client('iam')

# Define the source Jenkins job and the target CodePipeline
jenkins_job_name = "example-jenkins-job"
codepipeline_name = "example-codepipeline"
codepipeline_stage_name = "BuildStage"
codepipeline_action_name = "JenkinsBuildAction"

# Function to create a CodePipeline


def create_codepipeline():
    try:
        print(f"Creating CodePipeline: {codepipeline_name}")

        # Create IAM Role for CodePipeline
        role = iam_client.create_role(
            RoleName="CodePipelineServiceRole",
            AssumeRolePolicyDocument=json.dumps({
                "Version": "2012-10-17",
                "Statement": [{
                    "Effect": "Allow",
                    "Principal": {"Service": "codepipeline.amazonaws.com"},
                    "Action": "sts:AssumeRole"
                }]
            })
        )
        role_arn = role['Role']['Arn']
        print(f"Created IAM role for CodePipeline: {role_arn}")

        # Create the pipeline
        response = codepipeline_client.create_pipeline(
            pipeline={
                'name': codepipeline_name,
                'roleArn': role_arn,
                'artifactStore': {
                    'type': 'S3',
                    'location': 'your-s3-bucket-name'
                },
                'stages': [
                    {
                        'name': codepipeline_stage_name,
                        'actions': [
                            {
                                'name': codepipeline_action_name,
                                'actionTypeId': {
                                    'category': 'Build',
                                    'owner': 'AWS',
                                    'provider': 'CodeBuild',
                                    'version': '1'
                                },
                                'outputArtifacts': [{'name': 'BuildOutput'}],
                                'inputArtifacts': [{'name': 'SourceOutput'}],
                                'configuration': {
                                    'ProjectName': 'your-codebuild-project'
                                }
                            }
                        ]
                    }
                ]
            }
        )
        print(f"Created CodePipeline: {response}")
    except Exception as e:
        print(f"Error creating CodePipeline: {str(e)}")

# Function to migrate Jenkins job to CodePipeline


def migrate_jenkins_job():
    print(f"Migrating Jenkins job {jenkins_job_name} to CodePipeline...")
    create_codepipeline()
    # Add migration logic as needed (e.g., job configuration mapping, etc.)
    print(
        f"Migrated Jenkins job {jenkins_job_name}"
        f"to CodePipeline {codepipeline_name}"
    )


if __name__ == "__main__":
    migrate_jenkins_job()
