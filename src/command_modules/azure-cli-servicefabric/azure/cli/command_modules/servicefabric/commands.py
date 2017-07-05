# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# pylint: disable=line-too-long


from azure.cli.core.commands import cli_command
from azure.cli.core.util import empty_on_404

from ._client_factory import servicefabric_client_factory

custom_path = 'azure.cli.command_modules.servicefabric.custom#{}'
mgmt_path = 'azure.mgmt.servicefabric.operations.clusters_operations#{}'

factory = lambda args: servicefabric_client_factory(**args).clusters

cli_command(__name__, 'sf1 cluster show', mgmt_path.format('ClustersOperations.get'), factory, exception_handler=empty_on_404)

cli_command(__name__, 'sf1 cluster list', custom_path.format('list_cluster'), factory)

cli_command(__name__, 'sf1 cluster new', custom_path.format('new_cluster'), factory, no_wait_param=False)

cli_command(__name__, 'sf1 cluster certificate add', custom_path.format('add_cluster_cert'), factory, no_wait_param=False)

cli_command(__name__, 'sf1 cluster certificate remove', custom_path.format('remove_cluster_cert'), factory, no_wait_param=False)

cli_command(__name__, 'sf1 cluster client certificate add', custom_path.format('add_client_cert'), factory, no_wait_param=False)

cli_command(__name__, 'sf1 cluster client certificate remove', custom_path.format('remove_client_cert'), factory, no_wait_param=False)

cli_command(__name__, 'sf1 cluster setting set', custom_path.format('set_cluster_setting'), factory, no_wait_param=False)

cli_command(__name__, 'sf1 cluster setting remove', custom_path.format('remove_cluster_setting'), factory, no_wait_param=False)

cli_command(__name__, 'sf1 cluster reliability-level update', custom_path.format('update_cluster_reliability_level'), factory, no_wait_param=False)

cli_command(__name__, 'sf1 cluster node-type durability set', custom_path.format('update_cluster_durability'), factory, no_wait_param=False)

cli_command(__name__, 'sf1 cluster node-type add', custom_path.format('add_cluster_node_type'), factory, no_wait_param=False)

cli_command(__name__, 'sf1 cluster node-type node add', custom_path.format('add_cluster_node'), factory, no_wait_param=False)

cli_command(__name__, 'sf1 cluster node-type node remove', custom_path.format('remove_cluster_node'), factory, no_wait_param=False)

cli_command(__name__, 'sf1 cluster upgrade-type set', custom_path.format('update_cluster_upgrade_type'), factory, no_wait_param=False)

cli_command(__name__, 'sf1 application certificate add', custom_path.format('add_app_cert'), factory, no_wait_param=False)