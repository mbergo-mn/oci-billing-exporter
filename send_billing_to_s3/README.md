# OCI Function: send_billing_to_s3

## Overview

We've developed an Oracle Cloud Infrastructure (OCI) Function named `send_billing_to_s3` that retrieves billing information from an OCI account and uploads it to an AWS S3 bucket. This README outlines the entire process from setting up the Fn CLI to deploying the function in OCI, and it's written from our collective experience.

## Prerequisites

Before we start, make sure the following prerequisites are met:

- An active Oracle Cloud Infrastructure (OCI) account.
- An active AWS account with access to S3.
- OCI Vault is set up for storing secrets.
- Docker is installed on your local machine.
- The Fn CLI is installed on your local development machine.

## Installation

### Install Fn CLI on Ubuntu

To install the Fn CLI, we run the following commands:

```sh
curl -LSs https://raw.githubusercontent.com/fnproject/cli/master/install | sh
fn --version
```

This confirms that the Fn CLI is installed successfully.

### Set Up OCI Vault

We store our AWS credentials securely in the OCI Vault:

1. Create a Vault and Key in OCI.
2. Add the AWS Access Key and Secret Access Key as Secrets.

### Configure Dynamic Group and Policies

We give our function access to read secrets:

1. Create a Dynamic Group and include our function.
2. Write policies that allow the group to read secrets from the Vault.

## Function Deployment

### Local Development Setup

We set up our local development environment like this:

1. We create a new directory for our function.
2. We initialize a new function with the Fn CLI:

```sh
fn init --runtime python --trigger http send_billing_to_s3
```

3. We write our function logic in `func.py`.
4. We list our dependencies in `requirements.txt`.

### Dockerfile

We also create a `Dockerfile` tailored to our function's runtime environment.

### Deploying the Function

We deploy our function to OCI with this command:

```sh
fn -v deploy --app myapp
```

Replace `myapp` with your actual OCI Functions application name.

## Configuration

We set the following configuration variables for our function:

- `AWS_ACCESS_KEY_ID_SECRET_OCID`
- `AWS_SECRET_ACCESS_KEY_SECRET_OCID`
- `S3_BUCKET_NAME`

These are set through the Fn CLI or the OCI console.

## Testing

We test our function locally using:

```sh
fn invoke myapp send_billing_to_s3
```

## Monitoring

After deployment, we monitor our function's executions and logs through the OCI Console.

## Security

We handle security with OCI best practices, ensuring all sensitive information is securely stored in OCI Vault.

## Support

Should you have any queries or require support, please open an issue in the repository, and we'll address it as soon as possible.

## Contributing

Contributions are welcome! Fork the repository and submit a pull request to contribute.

## Automated Tasks

We have created a Makefile to automate common tasks:

- `make install` for installing dependencies.
- `make test` for running unit tests.
- `make run-local` for running the function locally.
- `make deploy` for deploying the function to OCI.
- `make all` to execute all the above tasks in order.

To run any of these tasks, simply execute `make <task-name>` in your terminal.

---

We trust this README provides you with a clear guide to setting up and managing the `send_billing_to_s3` function. We're proud of what we've built and we hope you find it both useful and easy to use.
---

Make sure to replace any placeholder text with actual values that are specific to your setup and environment. This `README.md` is now tailored to the `send_billing_to_s3` function and should be included at the root of your project directory.