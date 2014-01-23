#!/usr/bin/env python

# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from build_pack_utils import log_output
from build_pack_utils import Builder


if __name__ == '__main__':
    (Builder()
        .configure()
            .default_config()
            .user_config()
            .done()
        .install()
            .extension()
                .from_build_pack('lib/{WEB_SERVER}')
                .done()
            .extension()
                .from_build_pack('lib/php')
                .done()
            .extensions()
                .from_build_pack('extensions')
                .from_application('extensions')
                .done()
            .done()
        .create_start_script()
            .extension()
                .from_build_pack('lib/{WEB_SERVER}')
                .done()
            .extension()
                .from_build_pack('lib/php')
                .done()
            .extensions()
                .from_build_pack('extensions')
                .from_application('extensions')
                .done()
            .write())
