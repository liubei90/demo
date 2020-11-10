import asyncio
import json

from tornado.httpclient import HTTPClient, HTTPRequest, AsyncHTTPClient, HTTPClientError


test_no_analysis = {
  "settings": {
    "analysis": {
      "analyzer": {
        "ik_smart_gt1": {
          "tokenizer": "ik_smart111",
          "filter": [ "length_gt1" ]
        },
        "semicolon": {
          "tokenizer": "semicolon_tokenizer",
          "filter": ["lowercase", "trim", "length_gt0"]
        },
        "keyword_lowercase": {
          "tokenizer": "keyword",
          "filter": ["lowercase"]
        }
      },
      "tokenizer": {
        "semicolon_tokenizer": {
          "type": "char_group",
          "tokenize_on_chars": [";"]
        }
      },
      "filter": {
        "length_gt0": {
          "type": "length",
          "min": 1
        },
        "length_gt1": {
          "type": "length",
          "min": 2
        }
      }
    }
  },
  "mappings": {
    "default": {
      "properties": { 
        "material_id": {
          "type": "long"
        },
        "trade_name": {
          "type": "text"
        },
        "trade_name_copy" : {
          "type" : "text",
          "analyzer" : "ik_smart_gt1"
        },
        "category_id": {
          "type": "long"
        },
        "brand_id": {
          "type": "long"
        },
        "shelf_state": {
          "type": "long"
        },
        "attribute_value_id": {
          "type": "long"
        },
        "attribute_id": {
          "type": "long"
        },
        "jf_provider_guid": {
          "type": "text",
          "analyzer": "keyword_lowercase"
        },
        "apply_area_list": {
          "type": "text",
          "analyzer": "semicolon"
        }
      }
    }
  }
}


async def async_fetch():
    try:
        req = HTTPRequest('http://10.8.60.127:9200/test_no_analysis', method='PUT', body=json.dumps(test_no_analysis), headers={'Content-Type': 'application/json'}, auth_username='1', auth_password='2')

        client = AsyncHTTPClient()
        res = await client.fetch(req)

        print(res)
    except Exception as e:
        print(e)
        if hasattr(e, 'response'):
            print(e.response.body.decode('utf8'))


def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(async_fetch())


if __name__ == "__main__":
    main()