#!/usr/bin/python
# Copyright (c) 2020, 2023 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.
# GENERATED FILE - DO NOT EDIT - MANUAL CHANGES WILL BE OVERWRITTEN


from __future__ import absolute_import, division, print_function

__metaclass__ = type

ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = """
---
module: oci_logging_unified_agent_configuration_facts
short_description: Fetches details about one or multiple UnifiedAgentConfiguration resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple UnifiedAgentConfiguration resources in Oracle Cloud Infrastructure
    - Lists all unified agent configurations in the specified compartment.
    - If I(unified_agent_configuration_id) is specified, the details of a single UnifiedAgentConfiguration will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    unified_agent_configuration_id:
        description:
            - The OCID of the Unified Agent configuration.
            - Required to get a specific unified_agent_configuration.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - Compartment OCID to list resources in. See compartmentIdInSubtree
                   for nested compartments traversal.
            - Required to list multiple unified_agent_configurations.
        type: str
    log_id:
        description:
            - Custom log OCID to list resources with the log as destination.
        type: str
    is_compartment_id_in_subtree:
        description:
            - Specifies whether or not nested compartments should be traversed. Defaults to false.
        type: bool
    group_id:
        description:
            - The OCID of a group or a dynamic group.
        type: str
    display_name:
        description:
            - Resource name.
        type: str
        aliases: ["name"]
    lifecycle_state:
        description:
            - Lifecycle state of the log object
        type: str
        choices:
            - "CREATING"
            - "ACTIVE"
            - "UPDATING"
            - "INACTIVE"
            - "DELETING"
            - "FAILED"
    sort_by:
        description:
            - The field to sort by (one column only). Default sort order is
              ascending exception of `timeCreated` and `timeLastModified` columns (descending).
        type: str
        choices:
            - "timeCreated"
            - "displayName"
    sort_order:
        description:
            - The sort order to use, whether 'asc' or 'desc'.
        type: str
        choices:
            - "ASC"
            - "DESC"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific unified_agent_configuration
  oci_logging_unified_agent_configuration_facts:
    # required
    unified_agent_configuration_id: "ocid1.unifiedagentconfiguration.oc1..xxxxxxEXAMPLExxxxxx"

- name: List unified_agent_configurations
  oci_logging_unified_agent_configuration_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    log_id: "ocid1.log.oc1..xxxxxxEXAMPLExxxxxx"
    is_compartment_id_in_subtree: true
    group_id: "ocid1.group.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    lifecycle_state: CREATING
    sort_by: timeCreated
    sort_order: ASC

"""

RETURN = """
unified_agent_configurations:
    description:
        - List of UnifiedAgentConfiguration resources
    returned: on success
    type: complex
    contains:
        service_configuration:
            description:
                - ""
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                configuration_type:
                    description:
                        - Type of Unified Agent service configuration.
                    returned: on success
                    type: str
                    sample: LOGGING
                sources:
                    description:
                        - Logging source object.
                    returned: on success
                    type: complex
                    contains:
                        paths:
                            description:
                                - Absolute paths for log source files. Wildcard can be used.
                            returned: on success
                            type: list
                            sample: []
                        parser:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                is_merge_cri_fields:
                                    description:
                                        - If you don't need stream/logtag fields, set this to false.
                                    returned: on success
                                    type: bool
                                    sample: true
                                nested_parser:
                                    description:
                                        - Optional nested JSON Parser for CRI Parser. Supported fields are fieldTimeKey, timeFormat, and isKeepTimeKey.
                                    returned: on success
                                    type: complex
                                    contains:
                                        parser_type:
                                            description:
                                                - Type of fluent parser.
                                            returned: on success
                                            type: str
                                            sample: AUDITD
                                        field_time_key:
                                            description:
                                                - Specify time field for the event time. If the event doesn't have this field, the current time is used.
                                            returned: on success
                                            type: str
                                            sample: field_time_key_example
                                        types:
                                            description:
                                                - "Specify types for converting a field into another type.
                                                  For example,
                                                    With this configuration:
                                                        <parse>
                                                          @type csv
                                                          keys time,host,req_id,user
                                                          time_key time
                                                        </parse>"
                                                - " This incoming event:
                                                      \\"2013/02/28 12:00:00,192.168.0.1,111,-\\""
                                                - " is parsed as:
                                                      1362020400 (2013/02/28/ 12:00:00)"
                                                - |
                                                  "   record:
                                                      {
                                                        \\"host\\"   : \\"192.168.0.1\\",
                                                        \\"req_id\\" : \\"111\\",
                                                        \\"user\\"   : \\"-\\"
                                                      }"
                                            returned: on success
                                            type: dict
                                            sample: {}
                                        null_value_pattern:
                                            description:
                                                - Specify the null value pattern.
                                            returned: on success
                                            type: str
                                            sample: null_value_pattern_example
                                        is_null_empty_string:
                                            description:
                                                - If true, an empty string field is replaced with nil.
                                            returned: on success
                                            type: bool
                                            sample: true
                                        is_estimate_current_event:
                                            description:
                                                - If true, use Fluent::EventTime.now(current time) as a timestamp when time_key is specified.
                                            returned: on success
                                            type: bool
                                            sample: true
                                        is_keep_time_key:
                                            description:
                                                - If true, keep time field in the record.
                                            returned: on success
                                            type: bool
                                            sample: true
                                        timeout_in_milliseconds:
                                            description:
                                                - Specify the timeout for parse processing. This is mainly for detecting an incorrect regexp pattern.
                                            returned: on success
                                            type: int
                                            sample: 56
                                        time_type:
                                            description:
                                                - Time type of JSON parser.
                                            returned: on success
                                            type: str
                                            sample: FLOAT
                                        time_format:
                                            description:
                                                - Process time value using the specified format.
                                            returned: on success
                                            type: str
                                            sample: time_format_example
                                time_type:
                                    description:
                                        - Time type of JSON parser.
                                    returned: on success
                                    type: str
                                    sample: FLOAT
                                format_firstline:
                                    description:
                                        - First line pattern format.
                                    returned: on success
                                    type: str
                                    sample: format_firstline_example
                                format:
                                    description:
                                        - Mutiline pattern format.
                                    returned: on success
                                    type: list
                                    sample: []
                                grok_name_key:
                                    description:
                                        - grok name key.
                                    returned: on success
                                    type: str
                                    sample: grok_name_key_example
                                grok_failure_key:
                                    description:
                                        - grok failure key.
                                    returned: on success
                                    type: str
                                    sample: grok_failure_key_example
                                multi_line_start_regexp:
                                    description:
                                        - Multiline start regexp pattern.
                                    returned: on success
                                    type: str
                                    sample: multi_line_start_regexp_example
                                patterns:
                                    description:
                                        - grok pattern object.
                                    returned: on success
                                    type: complex
                                    contains:
                                        pattern:
                                            description:
                                                - The grok pattern.
                                            returned: on success
                                            type: str
                                            sample: pattern_example
                                        name:
                                            description:
                                                - The name key to tag this grok pattern.
                                            returned: on success
                                            type: str
                                            sample: name_example
                                        field_time_key:
                                            description:
                                                - Specify the time field for the event time. If the event doesn't have this field, the current time is used.
                                            returned: on success
                                            type: str
                                            sample: field_time_key_example
                                        field_time_format:
                                            description:
                                                - Process value using the specified format. This is available only when time_type is a string.
                                            returned: on success
                                            type: str
                                            sample: field_time_format_example
                                        field_time_zone:
                                            description:
                                                - Use the specified time zone. The time value can be parsed or formatted in the specified time zone.
                                            returned: on success
                                            type: str
                                            sample: field_time_zone_example
                                message_key:
                                    description:
                                        - Specifies the field name to contain logs.
                                    returned: on success
                                    type: str
                                    sample: message_key_example
                                expression:
                                    description:
                                        - Regex pattern.
                                    returned: on success
                                    type: str
                                    sample: expression_example
                                time_format:
                                    description:
                                        - Process time value using the specified format.
                                    returned: on success
                                    type: str
                                    sample: time_format_example
                                rfc5424_time_format:
                                    description:
                                        - rfc5424 time format.
                                    returned: on success
                                    type: str
                                    sample: rfc5424_time_format_example
                                message_format:
                                    description:
                                        - Message format of syslog.
                                    returned: on success
                                    type: str
                                    sample: RFC3164
                                is_with_priority:
                                    description:
                                        - With priority or not.
                                    returned: on success
                                    type: bool
                                    sample: true
                                is_support_colonless_ident:
                                    description:
                                        - Support colonless ident or not.
                                    returned: on success
                                    type: bool
                                    sample: true
                                syslog_parser_type:
                                    description:
                                        - Syslog parser type.
                                    returned: on success
                                    type: str
                                    sample: STRING
                                parser_type:
                                    description:
                                        - Type of fluent parser.
                                    returned: on success
                                    type: str
                                    sample: AUDITD
                                field_time_key:
                                    description:
                                        - Specify time field for the event time. If the event doesn't have this field, the current time is used.
                                    returned: on success
                                    type: str
                                    sample: field_time_key_example
                                types:
                                    description:
                                        - "Specify types for converting a field into another type.
                                          For example,
                                            With this configuration:
                                                <parse>
                                                  @type csv
                                                  keys time,host,req_id,user
                                                  time_key time
                                                </parse>"
                                        - " This incoming event:
                                              \\"2013/02/28 12:00:00,192.168.0.1,111,-\\""
                                        - " is parsed as:
                                              1362020400 (2013/02/28/ 12:00:00)"
                                        - |
                                          "   record:
                                              {
                                                \\"host\\"   : \\"192.168.0.1\\",
                                                \\"req_id\\" : \\"111\\",
                                                \\"user\\"   : \\"-\\"
                                              }"
                                    returned: on success
                                    type: dict
                                    sample: {}
                                null_value_pattern:
                                    description:
                                        - Specify the null value pattern.
                                    returned: on success
                                    type: str
                                    sample: null_value_pattern_example
                                is_null_empty_string:
                                    description:
                                        - If true, an empty string field is replaced with nil.
                                    returned: on success
                                    type: bool
                                    sample: true
                                is_estimate_current_event:
                                    description:
                                        - If true, use Fluent::EventTime.now(current time) as a timestamp when time_key is specified.
                                    returned: on success
                                    type: bool
                                    sample: true
                                is_keep_time_key:
                                    description:
                                        - If true, keep time field in the record.
                                    returned: on success
                                    type: bool
                                    sample: true
                                timeout_in_milliseconds:
                                    description:
                                        - Specify the timeout for parse processing. This is mainly for detecting an incorrect regexp pattern.
                                    returned: on success
                                    type: int
                                    sample: 56
                                delimiter:
                                    description:
                                        - csv delimiter.
                                    returned: on success
                                    type: str
                                    sample: delimiter_example
                                keys:
                                    description:
                                        - csv keys.
                                    returned: on success
                                    type: list
                                    sample: []
                        name:
                            description:
                                - unique name for the source
                            returned: on success
                            type: str
                            sample: name_example
                        source_type:
                            description:
                                - Unified schema logging source type.
                            returned: on success
                            type: str
                            sample: LOG_TAIL
                        channels:
                            description:
                                - Windows event log channels.
                            returned: on success
                            type: list
                            sample: []
                destination:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        log_object_id:
                            description:
                                - The OCID of the resource.
                            returned: on success
                            type: str
                            sample: "ocid1.logobject.oc1..xxxxxxEXAMPLExxxxxx"
        group_association:
            description:
                - ""
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                group_list:
                    description:
                        - list of group/dynamic group ids associated with this configuration.
                    returned: on success
                    type: list
                    sample: []
        id:
            description:
                - The OCID of the resource.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The OCID of the compartment that the resource belongs to.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - The user-friendly display name. This must be unique within the enclosing resource,
                  and it's changeable. Avoid entering confidential information.
            returned: on success
            type: str
            sample: display_name_example
        description:
            description:
                - Description for this resource.
            returned: on success
            type: str
            sample: description_example
        defined_tags:
            description:
                - Defined tags for this resource. Each key is predefined and scoped to a
                  namespace. For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        freeform_tags:
            description:
                - "Free-form tags for this resource. Each tag is a simple key-value pair with no
                  predefined name, type, or namespace. For more information, see L(Resource
                  Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        time_created:
            description:
                - Time the resource was created.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_last_modified:
            description:
                - Time the resource was last modified.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The pipeline state.
            returned: on success
            type: str
            sample: CREATING
        is_enabled:
            description:
                - Whether or not this resource is currently enabled.
            returned: on success
            type: bool
            sample: true
        configuration_type:
            description:
                - Type of Unified Agent service configuration.
                - Returned for list operation
            returned: on success
            type: str
            sample: LOGGING
        configuration_state:
            description:
                - State of unified agent service configuration.
            returned: on success
            type: str
            sample: VALID
    sample: [{
        "service_configuration": {
            "configuration_type": "LOGGING",
            "sources": [{
                "paths": [],
                "parser": {
                    "is_merge_cri_fields": true,
                    "nested_parser": {
                        "parser_type": "AUDITD",
                        "field_time_key": "field_time_key_example",
                        "types": {},
                        "null_value_pattern": "null_value_pattern_example",
                        "is_null_empty_string": true,
                        "is_estimate_current_event": true,
                        "is_keep_time_key": true,
                        "timeout_in_milliseconds": 56,
                        "time_type": "FLOAT",
                        "time_format": "time_format_example"
                    },
                    "time_type": "FLOAT",
                    "format_firstline": "format_firstline_example",
                    "format": [],
                    "grok_name_key": "grok_name_key_example",
                    "grok_failure_key": "grok_failure_key_example",
                    "multi_line_start_regexp": "multi_line_start_regexp_example",
                    "patterns": [{
                        "pattern": "pattern_example",
                        "name": "name_example",
                        "field_time_key": "field_time_key_example",
                        "field_time_format": "field_time_format_example",
                        "field_time_zone": "field_time_zone_example"
                    }],
                    "message_key": "message_key_example",
                    "expression": "expression_example",
                    "time_format": "time_format_example",
                    "rfc5424_time_format": "rfc5424_time_format_example",
                    "message_format": "RFC3164",
                    "is_with_priority": true,
                    "is_support_colonless_ident": true,
                    "syslog_parser_type": "STRING",
                    "parser_type": "AUDITD",
                    "field_time_key": "field_time_key_example",
                    "types": {},
                    "null_value_pattern": "null_value_pattern_example",
                    "is_null_empty_string": true,
                    "is_estimate_current_event": true,
                    "is_keep_time_key": true,
                    "timeout_in_milliseconds": 56,
                    "delimiter": "delimiter_example",
                    "keys": []
                },
                "name": "name_example",
                "source_type": "LOG_TAIL",
                "channels": []
            }],
            "destination": {
                "log_object_id": "ocid1.logobject.oc1..xxxxxxEXAMPLExxxxxx"
            }
        },
        "group_association": {
            "group_list": []
        },
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "description": "description_example",
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "freeform_tags": {'Department': 'Finance'},
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_last_modified": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "is_enabled": true,
        "configuration_type": "LOGGING",
        "configuration_state": "VALID"
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.logging import LoggingManagementClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class UnifiedAgentConfigurationFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "unified_agent_configuration_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_unified_agent_configuration,
            unified_agent_configuration_id=self.module.params.get(
                "unified_agent_configuration_id"
            ),
        )

    def list_resources(self):
        optional_list_method_params = [
            "log_id",
            "is_compartment_id_in_subtree",
            "group_id",
            "display_name",
            "lifecycle_state",
            "sort_by",
            "sort_order",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_unified_agent_configurations,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


UnifiedAgentConfigurationFactsHelperCustom = get_custom_class(
    "UnifiedAgentConfigurationFactsHelperCustom"
)


class ResourceFactsHelper(
    UnifiedAgentConfigurationFactsHelperCustom, UnifiedAgentConfigurationFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            unified_agent_configuration_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            log_id=dict(type="str"),
            is_compartment_id_in_subtree=dict(type="bool"),
            group_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "CREATING",
                    "ACTIVE",
                    "UPDATING",
                    "INACTIVE",
                    "DELETING",
                    "FAILED",
                ],
            ),
            sort_by=dict(type="str", choices=["timeCreated", "displayName"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="unified_agent_configuration",
        service_client_class=LoggingManagementClient,
        namespace="logging",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(unified_agent_configurations=result)


if __name__ == "__main__":
    main()
