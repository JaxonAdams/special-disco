import re
import random

def is_valid_post_payload(req_body):
    http_pattern = '^https?://.*\.\w{2,4}\S*$'
    
    if isinstance(req_body, dict):
        if 'url' in req_body:
            if re.search(http_pattern, req_body['url']):
                return True
    
    return False

def generate_id():
    available_chars = [*'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789']

    return ''.join(random.choice(available_chars) for _ in range(8))