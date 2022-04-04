=========================
 Tutorial
=========================
This tutorial is intended as an introduction to working with glitter_ and glitter-sdk_.


Getting Started
---------------

We begin by creating an object of class GlitterClient:

.. code-block:: python

    from glitter-sdk import GlitterClient
    url = 'http://sg1.testnet.glitter.link:26659'  # Or Use YOUR Glitter Root URL here

If the Glitter node or cluster doesn't require authentication tokens, you can do:

.. code-block:: python

    glitter_client = GlitterClient(url)

If it *does* require authentication tokens, you can do put them in a dict like so:

.. code-block:: python

    tokens = {'access_token': 'my_token'}
    glitter_client = GlitterClient(url, headers=tokens)


Create Schema
------------------------
First, create a schema for documents.

.. code-block:: python

    schema_name="demo"
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
    res = glitter_client.db.create_schema(schema_name, fields)
    # result like this
    {
        "code": 0,
        "message": "ok",
        "tx": "B88CEA8172F0B8BD7EAC3021C1B347786F74EDCD9110A7525C61237CD91FCE73",
        "data": ""
    }



Put Document to Glitter
--------------------------------
Then, put a document  glitter by glitter-sdk.
For example:

.. code-block:: python

    demo_doc = {
        "doi": "10.1002/(sci)1099-1697(199803/04)7:2<65::aid-jsc357>3.0.c",
        "title": "British Steel Corporation: probably the biggest turnaround story in UK industrial history",
        "ipfs_cid": "https://ipfs.io/ipfs/bafybeicoccgasbfx3puk5fxfol6gnbsaj7ssqs5gmhggotpx52p4pb6oze/6dbc6bb3e4993915f5ca07ca854ac31c.pdf"
    }
    res = self.glitter_client.db.put_doc(self.schema_name, demo_doc)
    # return like this, the tx is transaction id.
    {
      "code": 0,
      "message": "ok",
      "tx": "49429CDC575C0ED6D021FE9BEE1D44578AC7EDAD61A25EBBF0DE72746E0064F8",
      "data": ""
    }


Simple Search
-------------------------------------------------
Now, you can search.

.. code-block:: python

    schema_name = "demo"
    res = glitter_client.db.simple_search(schema_name, "British Steel Corporation")
    # the result like:
    {
        "code": 0,
        "message": "ok",
        "tx": "",
        "data": {
            "search_time": 695,
            "index": "demo",
            "meta": {
                "page": {
                    "current_page": 1,
                    "total_pages": 1,
                    "total_results": 1,
                    "size": 10,
                    "sorted_by": ""
                }
            },
            "items": [{
                "highlight": {
                    "title": ["<span>British</span> <span>Steel</span> <span>Corporation</span>: probably the biggest turnaround story in UK industrial history"]
                },
                "data": {
                    "_creator": "test_broks",
                    "_schema_name": "demo",
                    "doi": "10.1002/(sci)1099-1697(199803/04)7:2<65::aid-jsc357>3.0.c",
                    "ipfs_cid": "https://ipfs.io/ipfs/bafybeicoccgasbfx3puk5fxfol6gnbsaj7ssqs5gmhggotpx52p4pb6oze/6dbc6bb3e4993915f5ca07ca854ac31c.pdf",
                    "title": "British Steel Corporation: probably the biggest turnaround story in UK industrial history"
                }
            }],
            "facet": {}
        }
    }


.. _glitter:
.. _glitter-sdk: