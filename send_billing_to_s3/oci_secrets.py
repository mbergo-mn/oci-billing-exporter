from oci.secrets import SecretsClient
from oci.config import from_file as oci_config_from_file

def get_secret_content(oci_config, secret_ocid):
    # Initialize the Secrets Client with the OCI config
    secrets_client = SecretsClient(oci_config)
    
    # Get the secret's content
    secret_content_response = secrets_client.get_secret_bundle(secret_ocid)
    
    # Extract the secret content from the response
    secret_content = secret_content_response.data.secret_bundle_content.content.decode('utf-8')
    
    return secret_content

# Inside your handler function
oci_config = oci_config_from_file()  # Assumes default location for config file
aws_access_key_id_secret_ocid = ctx.Config()["AWS_ACCESS_KEY_ID_SECRET_OCID"]
aws_secret_access_key_secret_ocid = ctx.Config()["AWS_SECRET_ACCESS_KEY_SECRET_OCID"]

aws_access_key_id = get_secret_content(oci_config, aws_access_key_id_secret_ocid)
aws_secret_access_key = get_secret_content(oci_config, aws_secret_access_key_secret_ocid)

