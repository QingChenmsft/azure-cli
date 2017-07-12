# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# pylint: disable=line-too-long


from azure.cli.core.commands import cli_command
from azure.cli.core.util import empty_on_404

from ._client_factory import keyvault_client_factory,keyvault_client_vaults_factory


data_client_path = 'azure.keyvault.key_vault_client#{}'

custom_path = 'azure.cli.command_modules.servicefabric.custom#{}'

# cli_command(__name__, 'sbzrm load', custom_path.format('load'), keyvault_client_vaults_factory)

# cli_command(__name__, 'sbzrm load', custom_path.format('load'), keyvault_client_vaults_factory)

cli_command(__name__, 'sbz application get', custom_path.format('get'), keyvault_client_vaults_factory)

cli_command(__name__, 'sbz application create', custom_path.format('put'), keyvault_client_vaults_factory)

cli_command(__name__, 'sbz application update', custom_path.format('post'), keyvault_client_vaults_factory)

cli_command(__name__, 'sbz application delete', custom_path.format('delete'), keyvault_client_vaults_factory)