import re

def is_valid_post_payload(req_body):
    http_pattern = '^https?://.*\.\w{2,4}/?$'
    
    if isinstance(req_body, dict):
        if 'url' in req_body:
            if re.search(http_pattern, req_body['url']):
                return True
    
    return False


def post_url(req_body):
    return req_body