# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azure.cli.core.commands import \
    (register_cli_argument, register_extra_cli_argument, CliArgumentType)
import azure.cli.core.commands.arm  # pylint: disable=unused-import
from azure.cli.core.commands.validators import get_default_location_from_resource_group
from azure.cli.core.commands.parameters import (
    resource_group_name_type,
    location_type,
    tags_type,
    deployment_name_type,
    enum_choice_list,
    get_resource_name_completion_list
)
from azure.cli.core._profile import Profile
from azure.cli.core.util import get_json_object

from azure.cli.core.sdk.util import ParametersContext

# PARAMETER REGISTRATIONS

register_cli_argument('sf1 cluster list', 'resource_group_name', resource_group_name_type,
                      id_part=None, required=False, help='The resouce group name')

register_cli_argument('sf1', 'resource_group_name', resource_group_name_type,
                      id_part=None, required=True, help='The resouce group name')
register_cli_argument('sf1', 'cluster_name',options_list=('--name', '--cluster_name','-n'),
                      help='Specify the name of the cluster, if not given it will be same as resource group name')
register_cli_argument('sf1', 'location',
                      validator=get_default_location_from_resource_group)

register_cli_argument('sf1', 'secret_identifier',options_list=('--secret-identifier', '-si'),
                      help='The existing Azure key vault secret URL')
register_cli_argument('sf1', 'certificate_file',options_list=('--certificate-file', '-cf'),
                     help='The existing certificate file path for the primary cluster certificate.')
register_cli_argument('sf1', 'parameter_file',options_list=('--parameter-file', '-pf'),
                     help='The path to the template parameter file.')
register_cli_argument('sf1', 'template_file',options_list=('--template-file', '-tf'),
                     help='The path to the template file.')
register_cli_argument('sf1', 'vm_password',options_list=('--vm-password', '-vp'),
                      help='The password of the Vm')
register_cli_argument('sf1', 'certificate_output_folder',options_list=('--certificate-output-folder', '-cof'),
                      help='The folder of the new certificate file to be created.')
register_cli_argument('sf1', 'certificate_password',options_list=('--certificate-password', '-cp'),
                      help='The password of the certificate file.')
register_cli_argument('sf1', 'certificate_subject_name',options_list=('--certificate-subject-name', '-sn','-csn'),
                      help='The subject name of the certificate to be created.')
register_cli_argument('sf1', 'vault_resource_group_name',options_list=('--vault-resource-group', '-vg','-vrg'),
                      help='Azure key vault resource group name, it not given it will be defaulted to cluster resource group name')
register_cli_argument('sf1', 'vault_name',options_list=('--vault_name', '-vn'),
                      help='Azure key vault name, it not given it will be defaulted to the cluster resource group name')
register_cli_argument('sf1', 'cluster_size',options_list=('--cluster-size', '-size','-s'),
                      help='The number of nodes in the cluster. Default are 5 nodes')
register_cli_argument('sf1', 'vm_sku', options_list=('--vm-sku', '-sku'), help='The Vm Sku')
register_cli_argument('sf1', 'vm_user_name', options_list=('--vm-user-name', '-un'), help='The user name for logging to Vm. Default will be adminuser')
register_cli_argument('sf1', 'vm_os', default='WindowsServer2016Datacenter', options_list=('--vm-os', '-os'),
                      help='The Operating System of the VMs that make up the cluster.',
                     **enum_choice_list(['WindowsServer2012R2Datacenter', 'WindowsServer2016Datacenter', 'WindowsServer2016DatacenterwithContainers', 'UbuntuServer1604']))

register_cli_argument('sf1 client certificate', 'certificate_common_name',
                      help='Specify client certificate common name.')
register_cli_argument('sf1 client certificate', 'admin_client_thumbprints',
                      help='Specify list of client certificate thumbprint that only has admin permission.')
register_cli_argument('sf1 client certificate', 'certificate_issuer_thumbprint',
                      help='Specify client certificate issuer thumbprint.')
#TODO
register_cli_argument('sf1 client certificate', 'client_certificate_commonNames',
                      help='Specify client certificate issuer thumbprint.') 
register_cli_argument('sf1 client certificate', 'is-admin',
                      help='Client authentication type.')
register_cli_argument('sf1 client certificate', 'readonly_client_thumbprints',
                      help='Specify list of client certificate thumbprint that has read only permission.') 
register_cli_argument('sf1 client certificate', 'thumbprint',
                      help='Specify client certificate thumbprint.')
register_cli_argument('sf1 client certificate remove', 'thumbprints',
                      help='Specify list of client certificate thumbprints to be remove.')
register_cli_argument('sf1 cluster certificate remove', 'thumbprint',
                      help='Specify the cluster thumbprint which to be removed.')

register_cli_argument('sf1', 'node_type',
                      help='Specify the Node type name.')

register_cli_argument('sf1 cluster node', 'number_of_nodes_to_add',
                      help='Specify number of nodes to add.')
register_cli_argument('sf1 cluster node', 'number_of_nodes_to_remove',
                      help='Specify number of nodes to remove.')

register_cli_argument('sf1 cluster node-type', 'durability_level',
                      help='Specify durability level.')

register_cli_argument('sf1 cluster setting', 'parameter',
                      help='Specify parameter name')
register_cli_argument('sf1 cluster setting', 'section',
                      help='Specify section name')
register_cli_argument('sf1 cluster setting', 'value',
                      help='Specify the value')
#TODO
register_cli_argument('sf1 cluster setting', 'settings_section_description',
                      help='Specify the value')

register_cli_argument('sf1 cluster upgrade-type set', 'upgrade_mode',
                      help='Specify cluster upgrade mode')
register_cli_argument('sf1 cluster upgrade-type set', 'version',
                      help='Specify cluster code version')

with ParametersContext(command='sf1 cluster setting set') as c:
    c.register('settings_section_description', ('--settings-section-description',),
               type=get_json_object,
               help='JSON encoded parameters configuration. Use @{file} to load from a file.'
               """for example: [{"section": "NamingService","parameter": "MaxOperationTimeout","value": 1000},{"section": "MaxFileOperationTimeout","parameter": "Max2","value": 1000]""")

with ParametersContext(command='sf1 cluster setting remove') as c:
    c.register('settings_section_description', ('--settings-section-description',),
               type=get_json_object,
               help='JSON encoded parameters configuration. Use @{file} to load from a file.'
               """for example: [{"section": "NamingService","parameter": "MaxOperationTimeout"},{"section": "NamingService2","parameter": "MaxFileOperationTimeout"]""")