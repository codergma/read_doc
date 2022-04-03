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
    schema_name = "demo"

    @classmethod
    def setUpClass(cls):
        url = 'http://sg1.testnet.glitter.link:26659'
        cls.glitter_client = GlitterClient(url, headers=cls.header)

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
        self.assertEqual(res['code'], 0)
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
        doi = "10.1002/(sci)1099-1697(199803/04)7:2<65::aid-jsc357>3.0.c"
        res = self.glitter_client.db.get_docs(self.schema_name, [doi])
        self.assertEqual(res["code"], 0)
        self.assertGreaterEqual(res["data"]["Total"], 1)
        self.assertEqual(res["data"]["hits"][doi]["doc_id"], doi)
        print(res)

    def test_search(self):
        schema_name = 'demo'
        search_res = self.glitter_client.db.simple_search(schema_name, query_word="", order_by="", limit=10, page=1)
        self.assertEqual(search_res["code"], 0)
        self.assertGreaterEqual(search_res["data"]["meta"]["page"]["size"], 1)

    def test_app_status(self):
        res = self.glitter_client.db.app_status()
        self.assertEqual(res['code'], 0)
        print(res)


if __name__ == '__main__':
    unittest.main()
