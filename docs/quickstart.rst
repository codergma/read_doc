.. _quickstart:

====================
Quickstart
====================

Simple introduction to giltter.

1.Connection
---------------
connect glitternetwork use a client

.. code-block:: python

     from glitter_sdk import GlitterClient
     client = GlitterClient()

2.Data model
------------------------
In the example below we create a schema which is used to describe data model.

.. tabs::

    .. tab:: Code

        .. code-block:: python

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


    .. tab:: Output

        .. code-block:: python

            {
              "code": 0,
              "message": "ok",
              "data": {
                "fields": [
                  {
                    "index": {
                      "type": "keyword"
                    },
                    "name": "url",
                    "primary": "true",
                    "type": "string"
                  },
                  {
                    "index": {
                      "type": "text"
                    },
                    "name": "title",
                    "type": "string"
                  }
                ],
                "name": "sample",
                "type": "record"
              }
            }


3.Put doc
------------------------
After put success,check the detail of `tx info`_ .

.. tabs::
    .. tab:: Code

        .. code-block:: python

            put_res = client.db.put_doc("sample", {
                    "url": "https://glitterprotocol.io/",
                    "title": "A Decentralized Content Indexing Network",
                })

    .. tab:: Output

        .. code-block:: python

            {
              "code": 0,
              "message": "ok",
              "tx": "8A62859FD12A9A4D678812D65CE280501595C0B947C150E7182B7F099B213B01"
            }

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



.. _tx info: http://sg6.testnet.glitter.link:8000/txs?txID=8A62859FD12A9A4D678812D65CE280501595C0B947C150E7182B7F099B213B01
