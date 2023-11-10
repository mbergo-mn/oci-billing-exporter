import io
import json
import logging
import oci
import boto3
from fdk import response

def handler(ctx, data: io.BytesIO=None):
    try:
        # Parse input data if available
        body = json.loads(data.getvalue()) if data.getvalue() else {}

        # Initialize the OCI client
        oci_config = oci.config.from_file("/function/oci_config")  # Path to your OCI config file
        oci_identity = oci.identity.IdentityClient(oci_config)

        # Get the tenancy ID from OCI config
        tenancy_id = oci_config['tenancy']
        
        # Retrieve the billing information from OCI
        # This is a placeholder, replace with actual method to retrieve billing info
        billing_info = oci_identity.get_cost_and_usage(tenancy_id)

        # Format the billing information
        # This needs to be replaced with the actual format logic
        formatted_billing_info = json.dumps(billing_info.data, default=str)

        # Initialize the AWS S3 client
        aws_access_key_id = ctx.Config()["AWS_ACCESS_KEY_ID"]
        aws_secret_access_key = ctx.Config()["AWS_SECRET_ACCESS_KEY"]
        s3_client = boto3.client(
            's3',
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key
        )

        # Name of the S3 bucket
        s3_bucket_name = ctx.Config()["S3_BUCKET_NAME"]

        # Upload the billing info to S3 bucket
        s3_client.put_object(
            Bucket=s3_bucket_name,
            Key=f"billing_info.json",
            Body=formatted_billing_info
        )

        return response.Response(
            ctx, response_data=json.dumps(
                {"message": "Successfully uploaded billing info to S3"}),
            headers={"Content-Type": "application/json"}
        )
    except Exception as ex:
        logging.getLogger().info('Error occurred: ' + str(ex))

        return response.Response(
            ctx, response_data=json.dumps(
                {"message": "An error occurred"}),
            headers={"Content-Type": "application/json"}
        )
