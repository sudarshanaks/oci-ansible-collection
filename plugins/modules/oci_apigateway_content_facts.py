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
module: oci_apigateway_content_facts
short_description: Fetches details about a Content resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a Content resource in Oracle Cloud Infrastructure
    - Get the raw API content.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    dest:
        description:
            - The destination file path to write the output. The file will be created if it does not exist. If the file already exists, the content will be
              overwritten.
        type: str
        required: true
    api_id:
        description:
            - The ocid of the API.
        type: str
        aliases: ["id"]
        required: true
    range:
        description:
            - The Range HTTP request header indicates the part of a document that the
              server should return. L(RFC 7233,https://tools.ietf.org/html/rfc7233#section-3.1).
              Note that only a single range of bytes is supported.
        type: str
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific content
  oci_apigateway_content_facts:
    # required
    dest: /tmp/myfile
    api_id: "ocid1.api.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    range: range_example

"""


from ansible.module_utils._text import to_bytes
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.apigateway import ApiGatewayClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ApigatewayContentFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "api_id",
        ]

    def get_resource(self):
        optional_get_method_params = [
            "range",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_get_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.call_with_backoff(
            self.client.get_api_content,
            api_id=self.module.params.get("api_id"),
            **optional_kwargs
        )

    def get(self):
        response = self.get_resource().data
        dest = self.module.params.get("dest")
        chunk_size = oci_common_utils.MEBIBYTE
        with open(to_bytes(dest), "wb") as dest_file:
            for chunk in response.raw.stream(chunk_size, decode_content=True):
                dest_file.write(chunk)
        return None


ApigatewayContentFactsHelperCustom = get_custom_class(
    "ApigatewayContentFactsHelperCustom"
)


class ResourceFactsHelper(
    ApigatewayContentFactsHelperCustom, ApigatewayContentFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            dest=dict(type="str", required=True),
            api_id=dict(aliases=["id"], type="str", required=True),
            range=dict(type="str"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="content",
        service_client_class=ApiGatewayClient,
        namespace="apigateway",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    else:
        resource_facts_helper.fail()

    module.exit_json(content=result)


if __name__ == "__main__":
    main()
