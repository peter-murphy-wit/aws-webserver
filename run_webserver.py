
"""
Create, Monitor and Launch a public-facing web server in the Amazon Cloud
Automated Cloud Services CA1
"""
import boto3
import sys

ec2 = boto3.resource('ec2')
ec2_client = boto3.client('ec2')

def create_instance():
    instance = ec2.create_instances(
        ImageId='ami-079d9017cb651564d',
        MinCount=1,
        MaxCount=1,
        InstanceType='t2.micro',
        #SecurityGroup='launch-wizard-2'
        )
    print (instance[0].id)

def create_security_group():
    response = ec2_client.create_security_group(
    Description='ACS CA1 Secuirty Group',
    GroupName='acs-ca1-sg',
    VpcId='vpc-34c7234d',
    TagSpecifications=[
        {
            'ResourceType': 'security-group',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'ACS CA1 Secuirty Group'
                },
            ]
        },
    ],
    DryRun=False
    )
    print(response)

def create_bucket():
    for bucket_name in sys.argv[1:]:
        try:
            response = s3.create_bucket(Bucket=bucket_name,
    CreateBucketConfiguration={'LocationConstraint': 'eu-west-1'})
            print (response)
        except Exception as error:
            print (error)

def put_bucket():
    bucket_name = sys.argv[1]
    object_name = sys.argv[2]

    try:
        response = s3.Object(bucket_name,
    object_name).put(Body=open(object_name, 'rb'))
        print (response)
    except Exception as error:
        print (error)

def main():
    create_security_group()

if __name__ == "__main__":
    main()
