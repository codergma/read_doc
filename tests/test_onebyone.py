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
from glitter_sdk import GlitterClient


class GlitterClientUnitTest(unittest.TestCase):
    glitter_client: GlitterClient
    schema_name = "demo5"

    @classmethod
    def setUpClass(cls):
        url = 'http://sg1.testnet.glitter.link:26659'
        cls.glitter_client = GlitterClient(url)

    def test_create_schema(self):
        fields = [
            {
                "name": "doi",
                "type": "string",
                "primary": "true",
                "index": {
                    "type": "keyword"
                }
            },
            {
                "name": "title",
                "type": "string",
                "index": {
                    "type": "text"
                }
            },
            {
                "name": "ipfs_cid",
                "type": "string",
                "index": {
                    "index": "false"
                }
            }
        ]
        res = self.glitter_client.db.create_schema(self.schema_name, fields)
        # self.assertEqual(res['code'], 0)
        print(res)

    def test_show_schema(self):
        res = self.glitter_client.db.show_schema(self.schema_name)
        print(res)

    def test_list_schema(self):
        res = self.glitter_client.db.list_schema()
        self.assertEqual(res['code'], 0)
        self.assertIsNotNone(res['data'].get('demo'))
        print(res)

    def test_put_doc(self):
        demo_doc = {
            "doi": "10.1002/(sci)1099-1697(199803/04)7:2<65::aid-jsc357>3.0.c",
            "title": "British Steel Corporation: probably the biggest turnaround story in UK industrial history",
            "ipfs_cid": "https://ipfs.io/ipfs/bafybeicoccgasbfx3puk5fxfol6gnbsaj7ssqs5gmhggotpx52p4pb6oze/6dbc6bb3e4993915f5ca07ca854ac31c.pdf"
        }

        res = self.glitter_client.db.put_doc(self.schema_name, demo_doc)
        self.assertEqual(res['code'], 0)
        self.assertIsNotNone(res['tx'])
        print(res)

    def test_get_docs(self):
        primary_key = "10.1002/(sci)1099-1697(199803/04)7:2<65::aid-jsc357>3.0.c"
        res = self.glitter_client.db.get_docs(self.schema_name, [primary_key])
        print(res)
        # self.assertEqual(res["code"], 0)
        # self.assertGreaterEqual(res["data"]["Total"], 1)
        # self.assertEqual(res["data"]["hits"][primary_key]["doc_id"], primary_key)
        # print(res)

    def test_simple_search(self):
        query_field = ["doi", "title", "uri" ]
        res = self.glitter_client.db.simple_search(self.schema_name, "British Steel Corporation", query_field)
        print(res)
        # self.assertEqual(res["code"], 0)
        # self.assertGreaterEqual(res["data"]["meta"]["page"]["size"], 1)

    def test_app_status(self):
        res = self.glitter_client.db.app_status()
        self.assertEqual(res['code'], 0)
        print(res)

    def test_block(self):
        res = self.glitter_client.chain.block()
        print(res)

    def test_block(self):
        res = self.glitter_client.chain.block_search(query="block.height = 17835")
        print(res)

if __name__ == '__main__':
    unittest.main()
