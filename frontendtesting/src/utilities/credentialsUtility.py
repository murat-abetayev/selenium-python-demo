from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
import os


class CredentialsUtility(object):

    def __init__(self):
        pass

    def get_demo_customer_credentials(self):

        key_vault_url = "https://qa-demo.vault.azure.net/"

        azure_creds = DefaultAzureCredential()

