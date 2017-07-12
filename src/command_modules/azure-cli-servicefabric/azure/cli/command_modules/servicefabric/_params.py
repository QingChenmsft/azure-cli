
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


with ParametersContext(command='restcall put') as c:
    c.register('content', ('--content'),
               type=get_json_object,
               help='JSON encoded parameters configuration. Use @{file} to load from a file.')
            