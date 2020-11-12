# Copyright 2020 Vectorized, Inc.
#
# Use of this software is governed by the Business Source License
# included in the file licenses/BSL.md
#
# As of the Change Date specified in that file, in accordance with
# the Business Source License, use of this software will be governed
# by the Apache License, Version 2.0

import sys
sys.path.append("/opt/v/src/consistency-testing/gobekli")
sys.path.append("/opt/v/src/consistency-testing/chaostest")
from chaostest.faults import TerminateNodeRecoverableFault
from rptest.tests.chaos.chaos_base_test import BaseChaosTest
from ducktape.mark.resource import cluster


class TerminateFollowerTest(BaseChaosTest):
    def __init__(self, test_context, num_nodes=3):
        super(TerminateFollowerTest, self).__init__(test_context, num_nodes)

    @cluster(num_nodes=3)
    def test_terminate_follower(self):
        failure_factory = lambda: TerminateNodeRecoverableFault(
            lambda x: x.get_follower(), "follower")
        self.run(failure_factory)
