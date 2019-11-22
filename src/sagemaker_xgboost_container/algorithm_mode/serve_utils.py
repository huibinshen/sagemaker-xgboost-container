# Copyright 2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the 'License'). You
# may not use this file except in compliance with the License. A copy of
# the License is located at
#
#     http://aws.amazon.com/apache2.0/
#
# or in the 'license' file accompanying this file. This file is
# distributed on an 'AS IS' BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
# ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.
from sagemaker_algorithm_toolkit import exceptions


def get_content_type(request):
    content_type = request.content_type or "text/csv"
    content_type = content_type.lower()
    tokens = content_type.split(";")
    content_type = tokens[0].strip()
    if content_type not in ['text/csv', 'text/libsvm', 'text/x-libsvm', 'application/x-recordio-protobuf']:
        raise exceptions.UserError("Content-type {} not supported. "
                                   "Supported content-type is text/csv, text/libsvm,"
                                   " application/x-recordio-protobuf".format(content_type))
    return content_type