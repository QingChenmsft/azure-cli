# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azure.cli.core.help_files import helps #pylint: disable=unused-import

#pylint: disable=line-too-long

helps["sf1"] = """
    type: group
    short-summary: Manage and administer Service Fabric cluster resource
"""

helps["sf1 cluster"] = """
    type: group
    short-summary: TODO
"""

helps["sf1 application"] = """
    type: group
    short-summary: TODO
"""

helps["sf1 client"] = """
    type: group
    short-summary: TODO
"""

helps["sf1 cluster list"] = """
    type: command
    short-summary: List all the cluster resource in the same subscription
"""

helps["sf1 cluster new"] = """
    type: command
    short-summary: Create a new Service Fabric cluster
    long-summary: >
        This command uses certificates that you provide or system generated self-signed certificates to set up a new service fabric cluster. 
        It can use a default template or a custom template that you provide.
        You have the option of specifying a folder to export the self-signed certificates to or fetching them later from the key vault.
    examples:
        - name: Specify only the cluster size, the cert subject name, and the OS to deploy a cluster
          text: >
            az sf1 cluster new -g group-name -n cluster1 -l westus -size 4 --vm-password Password#1234 --certificate-output-folder c:\Mycertificates
        - name: Specify an existing Certificate resource in a key vault and a custom template to deploy a cluster
          text: >
            az sf1 cluster new -g group-name -n cluster1 -l westus --template-file c:\\template.json --parameter-file c:\\parameter.json 
            --secret-identifier https://chackokv1.vault.azure.net:443/secrets/chackdantestcertificate4/56ec774dc61a462bbc645ffc9b4b225f

"""