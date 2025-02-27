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
module: oci_identity_tag
short_description: Manage a Tag resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a Tag resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new tag in the specified tag namespace.
    - The tag requires either the OCID or the name of the tag namespace that will contain this
      tag definition.
    - "You must specify a *name* for the tag, which must be unique across all tags in the tag namespace
      and cannot be changed. The name can contain any ASCII character except the space (_) or period (.) characters.
      Names are case insensitive. That means, for example, \\"myTag\\" and \\"mytag\\" are not allowed in the same namespace.
      If you specify a name that's already in use in the tag namespace, a 409 error is returned."
    - "The tag must have a *description*. It does not have to be unique, and you can change it with
      L(UpdateTag,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/identity/latest/Tag/UpdateTag)."
    - The tag must have a value type, which is specified with a validator. Tags can use either a
      static value or a list of possible values. Static values are entered by a user applying the tag
      to a resource. Lists are created by you and the user must apply a value from the list. Lists
      are validiated.
    - "* If no `validator` is set, the user applying the tag to a resource can type in a static
      value or leave the tag value empty.
      * If a `validator` is set, the user applying the tag to a resource must select from a list
      of values that you supply with L(EnumTagDefinitionValidator,https://docs.cloud.oracle.com/en-
      us/iaas/api/#/en/identity/latest/datatypes/EnumTagDefinitionValidator)."
    - "This resource has the following action operations in the M(oracle.oci.oci_identity_tag_actions) module: bulk_delete, bulk_edit, import_standard_tags."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    description:
        description:
            - The description you assign to the tag during creation.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
    is_retired:
        description:
            - Whether the tag is retired.
              See L(Retiring Key Definitions and Namespace
              Definitions,https://docs.cloud.oracle.com/Content/Tagging/Tasks/managingtagsandtagnamespaces.htm#retiringkeys).
            - This parameter is updatable.
        type: bool
    freeform_tags:
        description:
            - Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
              For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
            - "Example: `{\\"Department\\": \\"Finance\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - Defined tags for this resource. Each key is predefined and scoped to a namespace.
              For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
            - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            - This parameter is updatable.
        type: dict
    is_cost_tracking:
        description:
            - Indicates whether the tag is enabled for cost tracking.
            - This parameter is updatable.
        type: bool
    validator:
        description:
            - ""
            - This parameter is updatable.
        type: dict
        suboptions:
            validator_type:
                description:
                    - "Specifies the type of validation: a static value (no validation) or a list."
                type: str
                choices:
                    - "DEFAULT"
                    - "ENUM"
                required: true
            values:
                description:
                    - The list of allowed values for a definedTag value.
                    - Applicable when validator_type is 'ENUM'
                type: list
                elements: str
    tag_namespace_id:
        description:
            - The OCID of the tag namespace.
        type: str
        required: true
    name:
        description:
            - The name you assign to the tag during creation. This is the tag key definition.
              The name must be unique within the tag namespace and cannot be changed.
        type: str
        required: true
    is_lock_override:
        description:
            - Whether to override locks (if any exist).
            - This parameter is updatable.
        type: bool
    state:
        description:
            - The state of the Tag.
            - Use I(state=present) to create or update a Tag.
            - Use I(state=absent) to delete a Tag.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create tag
  oci_identity_tag:
    # required
    description: description_example
    tag_namespace_id: "ocid1.tagnamespace.oc1..xxxxxxEXAMPLExxxxxx"
    name: name_example

    # optional
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    is_cost_tracking: true
    validator:
      # required
      validator_type: DEFAULT
    is_lock_override: true

- name: Update tag
  oci_identity_tag:
    # required
    tag_namespace_id: "ocid1.tagnamespace.oc1..xxxxxxEXAMPLExxxxxx"
    name: name_example

    # optional
    description: description_example
    is_retired: true
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    is_cost_tracking: true
    validator:
      # required
      validator_type: DEFAULT
    is_lock_override: true

- name: Delete tag
  oci_identity_tag:
    # required
    tag_namespace_id: "ocid1.tagnamespace.oc1..xxxxxxEXAMPLExxxxxx"
    name: name_example
    state: absent

    # optional
    is_lock_override: true

"""

RETURN = """
tag:
    description:
        - Details of the Tag resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        compartment_id:
            description:
                - The OCID of the compartment that contains the tag definition.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        tag_namespace_id:
            description:
                - The OCID of the namespace that contains the tag definition.
            returned: on success
            type: str
            sample: "ocid1.tagnamespace.oc1..xxxxxxEXAMPLExxxxxx"
        tag_namespace_name:
            description:
                - The name of the tag namespace that contains the tag definition.
            returned: on success
            type: str
            sample: tag_namespace_name_example
        id:
            description:
                - The OCID of the tag definition.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        name:
            description:
                - The name assigned to the tag during creation. This is the tag key definition.
                  The name must be unique within the tag namespace and cannot be changed.
            returned: on success
            type: str
            sample: name_example
        description:
            description:
                - The description you assign to the tag.
            returned: on success
            type: str
            sample: description_example
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
                - Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        is_retired:
            description:
                - Indicates whether the tag is retired.
                  See L(Retiring Key Definitions and Namespace
                  Definitions,https://docs.cloud.oracle.com/Content/Tagging/Tasks/managingtagsandtagnamespaces.htm#retiringkeys).
            returned: on success
            type: bool
            sample: true
        lifecycle_state:
            description:
                - The tag's current state. After creating a tag, make sure its `lifecycleState` is ACTIVE before using it. After retiring a tag, make sure its
                  `lifecycleState` is INACTIVE before using it. If you delete a tag, you cannot delete another tag until the deleted tag's `lifecycleState`
                  changes from DELETING to DELETED.
            returned: on success
            type: str
            sample: ACTIVE
        time_created:
            description:
                - Date and time the tag was created, in the format defined by RFC3339.
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        is_cost_tracking:
            description:
                - Indicates whether the tag is enabled for cost tracking.
            returned: on success
            type: bool
            sample: true
        validator:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                validator_type:
                    description:
                        - "Specifies the type of validation: a static value (no validation) or a list."
                    returned: on success
                    type: str
                    sample: ENUM
                values:
                    description:
                        - The list of allowed values for a definedTag value.
                    returned: on success
                    type: list
                    sample: []
    sample: {
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "tag_namespace_id": "ocid1.tagnamespace.oc1..xxxxxxEXAMPLExxxxxx",
        "tag_namespace_name": "tag_namespace_name_example",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "name": "name_example",
        "description": "description_example",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "is_retired": true,
        "lifecycle_state": "ACTIVE",
        "time_created": "2013-10-20T19:20:30+01:00",
        "is_cost_tracking": true,
        "validator": {
            "validator_type": "ENUM",
            "values": []
        }
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.identity import IdentityClient
    from oci.identity.models import CreateTagDetails
    from oci.identity.models import UpdateTagDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class TagHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(TagHelperGen, self).get_possible_entity_types() + [
            "tag",
            "tags",
            "identitytag",
            "identitytags",
            "tagresource",
            "tagsresource",
            "identity",
        ]

    def get_module_resource_id_param(self):
        return "name"

    def get_module_resource_id(self):
        return self.module.params.get("name")

    def get_get_fn(self):
        return self.client.get_tag

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_tag,
            tag_name=summary_model.name,
            tag_namespace_id=self.module.params.get("tag_namespace_id"),
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_tag,
            tag_namespace_id=self.module.params.get("tag_namespace_id"),
            tag_name=self.module.params.get("name"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "tag_namespace_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        return dict()

    def list_resources(self):

        required_kwargs = self.get_required_kwargs_for_list()
        optional_kwargs = self.get_optional_kwargs_for_list()
        kwargs = oci_common_utils.merge_dicts(required_kwargs, optional_kwargs)
        return oci_common_utils.list_all_resources(self.client.list_tags, **kwargs)

    def get_create_model_class(self):
        return CreateTagDetails

    def is_update(self):
        if not self.module.params.get("state") == "present":
            return False

        return self.does_resource_exist()

    def is_create(self):
        if not self.module.params.get("state") == "present":
            return False

        return not self.does_resource_exist()

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_tag,
            call_fn_args=(),
            call_fn_kwargs=dict(
                tag_namespace_id=self.module.params.get("tag_namespace_id"),
                create_tag_details=create_details,
                is_lock_override=self.module.params.get("is_lock_override"),
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateTagDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_tag,
            call_fn_args=(),
            call_fn_kwargs=dict(
                tag_namespace_id=self.module.params.get("tag_namespace_id"),
                tag_name=self.module.params.get("name"),
                update_tag_details=update_details,
                is_lock_override=self.module.params.get("is_lock_override"),
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.UPDATE_OPERATION_KEY,
            ),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_tag,
            call_fn_args=(),
            call_fn_kwargs=dict(
                tag_namespace_id=self.module.params.get("tag_namespace_id"),
                tag_name=self.module.params.get("name"),
                is_lock_override=self.module.params.get("is_lock_override"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


TagHelperCustom = get_custom_class("TagHelperCustom")


class ResourceHelper(TagHelperCustom, TagHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            description=dict(type="str"),
            is_retired=dict(type="bool"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            is_cost_tracking=dict(type="bool"),
            validator=dict(
                type="dict",
                options=dict(
                    validator_type=dict(
                        type="str", required=True, choices=["DEFAULT", "ENUM"]
                    ),
                    values=dict(type="list", elements="str"),
                ),
            ),
            tag_namespace_id=dict(type="str", required=True),
            name=dict(type="str", required=True),
            is_lock_override=dict(type="bool"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="tag",
        service_client_class=IdentityClient,
        namespace="identity",
    )

    result = dict(changed=False)

    if resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_update():
        result = resource_helper.update()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
