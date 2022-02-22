#!/usr/bin/python3
from unittest import result
import requests
import os
from dotenv import load_dotenv
load_dotenv()
from fake_useragent import UserAgent
from models.db_models import Session, ProductModel
from handler.parser import parser_product, parser_product_details, ProductDetailsModel

db= Session()
fake_ua = UserAgent()


if __name__ == '__main__':

    BASE_URL = os.getenv('BASE_URL')
    PRODUCT_BASE_URL = os.getenv('PRODUCT_BASE_URL')
    PRODUCT_COMMENT_BASE_URL = os.getenv('PRODUCT_COMMENT_BASE_URL')

    headers = {'User-Agent': fake_ua.random}
    base_page = requests.get(url=BASE_URL, headers=headers)
    base_data = base_page.json()

    fake_ua = UserAgent()
    headers = {'User-Agent': fake_ua.random}
    model_product = []
    model_product_detales = []
    for product in base_data['data']['products']:
        product_details_url = PRODUCT_BASE_URL.format(product['id'])
        product_page = requests.get(url=product_details_url, headers=headers)
        product_details_data = (product_page.json())['data']['product']

        product_comment_url = PRODUCT_COMMENT_BASE_URL.format(product['id'])
        product_comment_page = requests.get(url=product_comment_url, headers=headers)
        product_comment_data = (product_comment_page.json())['data']
        result = parser_product(product['id'], product_details_data )

        if db.query(ProductModel).filter_by(id=result['id']).first() is None:
            model_product.append(ProductModel(**result))

        model_product_detales.append(
            ProductDetailsModel(
                **parser_product_details(product['id'], product_details_data, product_comment_data)
                )
            )


    db.bulk_save_objects(model_product)
    db.bulk_save_objects(model_product_detales)
    db.commit()
