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
module: oci_identity_user_facts
short_description: Fetches details about one or multiple User resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple User resources in Oracle Cloud Infrastructure
    - Lists the users in your tenancy. You must specify your tenancy's OCID as the value for the
      compartment ID (remember that the tenancy is simply the root compartment).
      See L(Where to Get the Tenancy's OCID and User's OCID,https://docs.cloud.oracle.com/Content/API/Concepts/apisigningkey.htm#five).
    - If I(user_id) is specified, the details of a single User will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    user_id:
        description:
            - The OCID of the user.
            - Required to get a specific user.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The OCID of the compartment (remember that the tenancy is simply the root compartment).
            - Required to list multiple users.
        type: str
    identity_provider_id:
        description:
            - The id of the identity provider.
        type: str
    external_identifier:
        description:
            - The id of a user in the identity provider.
        type: str
    name:
        description:
            - A filter to only return resources that match the given name exactly.
        type: str
    sort_by:
        description:
            - The field to sort by. You can provide one sort order (`sortOrder`). Default order for
              TIMECREATED is descending. Default order for NAME is ascending. The NAME
              sort order is case sensitive.
            - "**Note:** In general, some \\"List\\" operations (for example, `ListInstances`) let you
              optionally filter by Availability Domain if the scope of the resource type is within a
              single Availability Domain. If you call one of these \\"List\\" operations without specifying
              an Availability Domain, the resources are grouped by Availability Domain, then sorted."
        type: str
        choices:
            - "TIMECREATED"
            - "NAME"
    sort_order:
        description:
            - The sort order to use, either ascending (`ASC`) or descending (`DESC`). The NAME sort order
              is case sensitive.
        type: str
        choices:
            - "ASC"
            - "DESC"
    lifecycle_state:
        description:
            - A filter to only return resources that match the given lifecycle state.  The state value is case-insensitive.
        type: str
        choices:
            - "CREATING"
            - "ACTIVE"
            - "INACTIVE"
            - "DELETING"
            - "DELETED"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific user
  oci_identity_user_facts:
    # required
    user_id: "ocid1.user.oc1..xxxxxxEXAMPLExxxxxx"

- name: List users
  oci_identity_user_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    identity_provider_id: "ocid1.identityprovider.oc1..xxxxxxEXAMPLExxxxxx"
    external_identifier: external_identifier_example
    name: name_example
    sort_by: TIMECREATED
    sort_order: ASC
    lifecycle_state: CREATING

"""

RETURN = """
users:
    description:
        - List of User resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The OCID of the user.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The OCID of the tenancy containing the user.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        name:
            description:
                - The name you assign to the user during creation. This is the user's login for the Console.
                  The name must be unique across all users in the tenancy and cannot be changed.
            returned: on success
            type: str
            sample: name_example
        description:
            description:
                - The description you assign to the user. Does not have to be unique, and it's changeable.
                - (For tenancies that support identity domains) You can have an empty description.
            returned: on success
            type: str
            sample: description_example
        email:
            description:
                - The email address you assign to the user.
                  The email address must be unique across all users in the tenancy.
                - (For tenancies that support identity domains) The email address is required unless the requirement is disabled at the tenancy level.
            returned: on success
            type: str
            sample: email_example
        email_verified:
            description:
                - Whether the email address has been validated.
            returned: on success
            type: bool
            sample: true
        db_user_name:
            description:
                - DB username of the DB credential. Has to be unique across the tenancy.
            returned: on success
            type: str
            sample: db_user_name_example
        identity_provider_id:
            description:
                - The OCID of the `IdentityProvider` this user belongs to.
            returned: on success
            type: str
            sample: "ocid1.identityprovider.oc1..xxxxxxEXAMPLExxxxxx"
        external_identifier:
            description:
                - Identifier of the user in the identity provider
            returned: on success
            type: str
            sample: external_identifier_example
        time_created:
            description:
                - Date and time the user was created, in the format defined by RFC3339.
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The user's current state. After creating a user, make sure its `lifecycleState` changes from CREATING to
                  ACTIVE before using it.
            returned: on success
            type: str
            sample: CREATING
        inactive_status:
            description:
                - "Returned only if the user's `lifecycleState` is INACTIVE. A 16-bit value showing the reason why the user
                  is inactive:"
                - "- bit 0: SUSPENDED (reserved for future use)
                  - bit 1: DISABLED (reserved for future use)
                  - bit 2: BLOCKED (the user has exceeded the maximum number of failed login attempts for the Console)"
            returned: on success
            type: int
            sample: 56
        freeform_tags:
            description:
                - Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        capabilities:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                can_use_console_password:
                    description:
                        - Indicates if the user can log in to the console.
                    returned: on success
                    type: bool
                    sample: true
                can_use_api_keys:
                    description:
                        - Indicates if the user can use API keys.
                    returned: on success
                    type: bool
                    sample: true
                can_use_auth_tokens:
                    description:
                        - Indicates if the user can use SWIFT passwords / auth tokens.
                    returned: on success
                    type: bool
                    sample: true
                can_use_smtp_credentials:
                    description:
                        - Indicates if the user can use SMTP passwords.
                    returned: on success
                    type: bool
                    sample: true
                can_use_db_credentials:
                    description:
                        - Indicates if the user can use DB passwords.
                    returned: on success
                    type: bool
                    sample: true
                can_use_customer_secret_keys:
                    description:
                        - Indicates if the user can use SigV4 symmetric keys.
                    returned: on success
                    type: bool
                    sample: true
        is_mfa_activated:
            description:
                - Flag indicates if MFA has been activated for the user.
            returned: on success
            type: bool
            sample: true
        last_successful_login_time:
            description:
                - The date and time of when the user most recently logged in the
                  format defined by RFC3339 (ex. `2016-08-25T21:10:29.600Z`).
                  If there is no login history, this field is null.
                - For illustrative purposes, suppose we have a user who has logged in
                  at July 1st, 2020 at 1200 PST and logged out 30 minutes later.
                  They then login again on July 2nd, 2020 at 1500 PST.
                - Their previousSuccessfulLoginTime would be `2020-07-01:19:00.000Z`.
                - Their lastSuccessfulLoginTime would be `2020-07-02:22:00.000Z`.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        previous_successful_login_time:
            description:
                - The date and time of when the user most recently logged in the
                  format defined by RFC3339 (ex. `2016-08-25T21:10:29.600Z`).
                  If there is no login history, this field is null.
                - For illustrative purposes, suppose we have a user who has logged in
                  at July 1st, 2020 at 1200 PST and logged out 30 minutes later.
                  They then login again on July 2nd, 2020 at 1500 PST.
                - Their previousSuccessfulLoginTime would be `2020-07-01:19:00.000Z`.
                - Their lastSuccessfulLoginTime would be `2020-07-02:22:00.000Z`.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "name": "name_example",
        "description": "description_example",
        "email": "email_example",
        "email_verified": true,
        "db_user_name": "db_user_name_example",
        "identity_provider_id": "ocid1.identityprovider.oc1..xxxxxxEXAMPLExxxxxx",
        "external_identifier": "external_identifier_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "inactive_status": 56,
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "capabilities": {
            "can_use_console_password": true,
            "can_use_api_keys": true,
            "can_use_auth_tokens": true,
            "can_use_smtp_credentials": true,
            "can_use_db_credentials": true,
            "can_use_customer_secret_keys": true
        },
        "is_mfa_activated": true,
        "last_successful_login_time": "2013-10-20T19:20:30+01:00",
        "previous_successful_login_time": "2013-10-20T19:20:30+01:00"
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.identity import IdentityClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class UserFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "user_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_user, user_id=self.module.params.get("user_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "identity_provider_id",
            "external_identifier",
            "name",
            "sort_by",
            "sort_order",
            "lifecycle_state",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_users,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


UserFactsHelperCustom = get_custom_class("UserFactsHelperCustom")


class ResourceFactsHelper(UserFactsHelperCustom, UserFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            user_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            identity_provider_id=dict(type="str"),
            external_identifier=dict(type="str"),
            name=dict(type="str"),
            sort_by=dict(type="str", choices=["TIMECREATED", "NAME"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            lifecycle_state=dict(
                type="str",
                choices=["CREATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED"],
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="user",
        service_client_class=IdentityClient,
        namespace="identity",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(users=result)


if __name__ == "__main__":
    main()
