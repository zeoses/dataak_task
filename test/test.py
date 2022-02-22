import unittest
import json
from handler.parser import parser_product, parser_product_details


class TestProductParserMethods(unittest.TestCase):
    
    

    def test_product_details(self):
        with open('test/files/input-product.json', 'rb') as handle:
            p = json.loads(handle.read())['product']

        with open('test/files/input-comment.json', 'rb') as handle:
            c = json.loads(handle.read())

        with open('test/files/output.json', 'rb') as handle:
            r = json.loads(handle.read())

        self.assertEqual(parser_product_details(p['id'], p, c), r['product_details'])
        self.assertEqual(parser_product(p['id'], p), r['product'])

if __name__ == '__main__':
    unittest.main()