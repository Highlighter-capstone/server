from config import config
import boto3

class S3Connector:
    aws_config = config.aws_config
    client = boto3.client('s3',
                          aws_access_key_id=aws_config["aws_access_key_id"],
                          aws_secret_access_key=aws_config["aws_secret_access_key"],
                          region_name=aws_config["aws_default_region"])
    def get_client(self):
        return self.client

    def get_bucket(self):
        return self.aws_config["bucket"]