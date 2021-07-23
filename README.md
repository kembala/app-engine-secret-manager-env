## Pre-requisites

Get your account credentials from `IAM & Admin > Service Accounts` and save in this directory as google_application_credentials.json.
Install Secret Manager SDK `pip install google-cloud-secret-manager`

## Usage

Run `GOOGLE_APPLICATION_CREDENTIALS=google_application_credentials.json python3 get-google-secrets.py <project-id> > /.env.temp`
Load environment variables with `set -o allexport; source .env.temp; set +o allexport`

## Resources

Documentation for python gcloud secretmanager: https://googleapis.dev/python/secretmanager/latest/secretmanager_v1/services.html#
