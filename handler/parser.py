import requests
import os
from fake_useragent import UserAgent
from  models.db_models import ProductModel, ProductDetailsModel, Session

db= Session()

def parser_product(product_id, product_details_data):
    
    return {
        'id':product_id,
        'first_image_url':product_details_data['images']["main"]['url'][0],
        'title_fa':product_details_data['title_fa'],
        'title_en':product_details_data['title_en'],
        'url': "https://www.digikala.com/product/dkp-{}/".format(product_id)
        }



def parser_product_details(product_id, product_details_data, product_comment_data):
    return {
        'product_id':product_id,
        'quality_rate':product_comment_data['ratings'][0]['value'],
        'pbv_rate':product_comment_data['ratings'][1]['value'],
        'innovation_rate':product_comment_data['ratings'][2]['value'],
        'features_rate':product_comment_data['ratings'][3]['value'],
        'useable_rate':product_comment_data['ratings'][4]['value'],
        'Design_rate':product_comment_data['ratings'][5]['value'],
        'price':product_details_data['variants'][0]['price']['selling_price'],
        'price_with_discount':product_details_data['variants'][0]['price']['rrp_price']
    }
    
        
    return priduct_model, priduct_model1