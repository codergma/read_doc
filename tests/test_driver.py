# Copyright 2022-present glitter, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Test the glitter driver module."""

import unittest
import time
import json
import sys

from glitter_sdk import GlitterClient


class GlitterClientUnitTest(unittest.TestCase):
    glitter_client: GlitterClient
    header = {"access_token": "test_broks"}

    @classmethod
    def setUpClass(cls):
        url = 'http://sg1.testnet.glitter.link:26659'
        cls.glitter_client = GlitterClient(url, headers=cls.header)

    def test_database_operation(self):
        schema_name = "demo"
        demo_doc = {
            "doi": "10.1002/(sci)1099-1697(199803/04)7:2<65::aid-jsc357>3.0.co;2-t",
            "title": "British Steel Corporation: probably the biggest turnaround story in UK industrial history",
            "uri": "https://ipfs.io/ipfs/bafybeicoccgasbfx3puk5fxfol6gnbsaj7ssqs5gmhggotpx52p4pb6oze/6dbc6bb3e4993915f5ca07ca854ac31c.pdf"
        }

        # put doc
        put_res = self.glitter_client.db.put_doc(schema_name, demo_doc)
        print(put_res)
        # self.assertEqual(put_res["code"], 0)
        # Wait a minute
        time.sleep(1)
        return

        # get doc by doc_id
        get_res = self.glitter_client.db.get_docs(schema_name, [doc_id])
        self.assertEqual(get_res["code"], 0)
        self.assertGreaterEqual(get_res["data"]["Total"], 1)
        index_id = self.header["access_token"] + "_" + doc_id
        self.assertEqual(get_res["data"]["Hits"][index_id]["doc_id"], doc_id)

        # search by publisher
        search_res = self.glitter_client.db.simple_search(schema_name, publisher)
        self.assertEqual(search_res["code"], 0)
        self.assertGreaterEqual(search_res["data"]["meta"]["page"]["size"], 1)

        # get app status
        app_status = self.glitter_client.db.app_status()
        self.assertGreaterEqual(app_status["data"]["schema_state"]["libgen"]["count"], 1)

    def chain_operation(self):
        # tx_search
        tx_res = self.glitter_client.chain.tx_search(query="update_doc.token='my_token'")
        tx_dict = json.loads(tx_res)
        height = tx_dict["result"]["txs"][0]["height"]
        self.assertGreaterEqual(int(height, 10), 1)

        tx_res = self.glitter_client.chain.tx_search("tx.height=" + height)
        tx_dict = json.loads(tx_res)
        self.assertGreaterEqual(len(tx_dict["result"]["txs"]), 1)

        # block_search
        block_res = self.glitter_client.chain.block_search(query="block.height > 0")
        block_dict = json.loads(block_res)
        height = block_dict["result"]["blocks"][0]["block"]["header"]["height"]
        self.assertGreaterEqual(int(height), 1)

        block_res = self.glitter_client.chain.block_search("block.height = " + height)
        block_dict = json.loads(block_res)
        self.assertEqual(height, block_dict["result"]["blocks"][0]["block"]["header"]["height"])

    def admin_operation(self):
        valid_res = self.glitter_client.admin.validators()
        valid_dict = json.loads(valid_res)
        self.assertGreaterEqual(int(valid_dict["result"]["total"], 10), 1)


if __name__ == '__main__':
    unittest.main()
