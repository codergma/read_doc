.. _quickstart:

====================
Quickstart
====================

Simple introduction to giltter.

1.Connection
---------------
connect glitternetwork use a client

.. ipython::

     from glitter_sdk import GlitterClient
     client = GlitterClient()

2.Data model
------------------------
In the example below we create a schema which is used to describe data model.

.. ipython::

    # create schema with a url and title
    schema = [
        {
            "name": "url",
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
        }
    ]
    res = client.db.create_schema("sample", schema)
    #get the schema you create use get_schema
    client.db.get_schema("sample")



3.Put doc
------------------------
After put success,check the detail of `tx info`_ .

.. code-block:: python

    put_res = client.db.put_doc("sample", {
            "url": "https://glitterprotocol.io/",
            "title": "A Decentralized Content Indexing Network",
        })

4.Search
------------------------

.. code-block:: python

    # search doc
    search_res = client.db.search("sample", "Content Indexing Network")


5.Another search example
------------------------
search rss data. same as  sci检索页面

.. code-block:: python

    client.db.search("rss", "oppo")
    client.db.search("rss", "oppo", ['title'])
    client.db.search("rss", "oppo", ['title', 'description'], filters=[], aggs_field=["tags"])


_tx info: http://sg6.testnet.glitter.link:8000/txs?txID=D4D9F93B60770952A33BD3C7A8C0F70A72CB78F800AD1C100CA73EBCF2825BDC
