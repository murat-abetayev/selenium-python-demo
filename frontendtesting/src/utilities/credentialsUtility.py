from azure.identity import ClientSecretCredential
from azure.keyvault.secrets import SecretClient
import os


class CredentialsUtility(object):

    def __init__(self):
        pass

    @staticmethod
    def get_demo_customer_credentials():

        vault_url = "https://qa-demo.vault.azure.net/"

        # Create the credential
        azure_creds = ClientSecretCredential(
            tenant_id=os.environ.get('TENANT_ID'),
            client_id=os.environ.get('CLIENT_ID'),
            client_secret=os.environ.get('CLIENT_SECRET')
        )

        # Create a SecretClient to interact with the Key Vault
        client = SecretClient(vault_url=vault_url, credential=azure_creds)

        demo_customer = client.get_secret("DEMO-CUST-USERNAME").value
        demo_cust_password = client.get_secret("DEMO-CUST-PASSWORD").value

        if not demo_customer or not demo_cust_password:
            raise Exception(f"The demo customer credentials 'DEMO-CUST-USERNAME' and 'DEMO-CUST-PASSWORD' "
                            f"must be set in Azure Key Vault")
        else:
            return {'demo_customer': demo_customer, 'demo_cust_password': demo_cust_password}
