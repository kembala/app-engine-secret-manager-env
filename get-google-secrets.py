#!/usr/bin/python

import sys

def access_secret_version(project_id, secret_id, version_id):
    """
    Access the payload for the given secret version if one exists. The version
    can be a version number as a string (e.g. "5") or an alias (e.g. "latest").
    """

    # Import the Secret Manager client library.
    from google.cloud import secretmanager

    # Create the Secret Manager client.
    client = secretmanager.SecretManagerServiceClient()

    # Build the resource name of the secret version.
    name = f"projects/{project_id}/secrets/{secret_id}/versions/{version_id}"

    # Access the secret version.
    response = client.access_secret_version(request={"name": name})

    # Print the secret payload.
    #
    # WARNING: Do not print the secret in a production environment - this
    # snippet is showing how to access the secret material.
    payload = response.payload.data.decode("UTF-8")
    return format(payload)

def list_secrets(project_id):
    """
    List all secrets in the given project.
    """

    # Import the Secret Manager client library.
    from google.cloud import secretmanager

    # Create the Secret Manager client.
    client = secretmanager.SecretManagerServiceClient()

    # Build the resource name of the parent project.
    parent = f"projects/{project_id}"

    secrets = []

    # Return all secrets.
    for secret in client.list_secrets(request={"parent": parent}):
        secrets.append(secret.name.split('/')[-1])

    return secrets

projectId = sys.argv[1]
secrets = list_secrets(projectId)

for secret in secrets:
    value = access_secret_version(projectId,secret,1)
    print(f'{secret}={value}')