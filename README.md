
```markdown
# OCI Function for Billing to S3

## Overview

We've created an Oracle Cloud Infrastructure (OCI) Function that retrieves billing information from an OCI account and uploads it to an AWS S3 bucket. This document guides you through the installation of the Fn CLI, setting up your local development environment, deploying the function to OCI, and configuring your function with the necessary credentials.

## Prerequisites

Before we begin, ensure you have the following prerequisites met:

- An Oracle Cloud Infrastructure (OCI) account
- An AWS account with access to S3
- Access to OCI Vault for storing secrets
- Docker installed on your local machine
- Fn CLI installed on your local machine

## Installation

### Install Fn CLI on Ubuntu

To install the Fn CLI, we execute the following commands in our terminal:

```sh
curl -LSs https://raw.githubusercontent.com/fnproject/cli/master/install | sh

```


After the installation is complete, we verify it with:

```sh
fn --version
```

### Set Up OCI Vault

We securely store our AWS credentials in the OCI Vault:

1. Create a Vault and Key in OCI.
2. Add AWS Access Key and Secret Access Key as Secrets.

### Configure Dynamic Group and Policies

We configure a Dynamic Group and Policies to allow our function to access secrets:

1. Create a Dynamic Group and include our function.
2. Write policies to allow the group to read secrets.

## Function Deployment

### Local Development

Here's how we set up our local development environment:

1. Create a new directory and initialize a function using the Fn CLI:

```sh
fn init --runtime python --trigger http my-python-function
```

2. Write our function logic in `func.py`.
3. Define dependencies in `requirements.txt`.

### Create Dockerfile

We create a `Dockerfile` in our function directory with the necessary environment for our function to run.

### Deploying the Function

To deploy our function to OCI, we run:

```sh
fn -v deploy --app myapp
```

## Configuration

We configure our function with the necessary environment variables using the Fn CLI or the OCI console:

- `AWS_ACCESS_KEY_ID_SECRET_OCID`: The OCID of the secret containing the AWS Access Key ID.
- `AWS_SECRET_ACCESS_KEY_SECRET_OCID`: The OCID of the secret containing the AWS Secret Access Key.
- `S3_BUCKET_NAME`: The name of the S3 bucket where billing information will be uploaded.

## Testing

We test our function locally using:

```sh
fn invoke myapp my-python-function
```

## Monitoring

After deploying, we monitor our function executions and logs through the OCI Console.

## Security

We adhere to OCI best practices for security, ensuring that all sensitive information is stored in OCI Vault and only accessed by our function at runtime.

## Support

For any queries or support, please open an issue in the repository, and we'll get back to you promptly.

## Contributing

We welcome contributions! If you'd like to contribute, please fork the repository and submit a pull request.

---

We hope this README helps you in setting up and deploying your OCI Function seamlessly. Happy coding!
```

Be sure to fill in any placeholders (like `my-python-function` and `myapp`) with the actual names used in your project. You might also need to expand upon certain sections with more detailed instructions specific to your setup or environment.

thk @mbergo