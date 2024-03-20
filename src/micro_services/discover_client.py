from configs.env import *

def get_service(service):
    return 'common' if service == 'loki' else service

def get_instance_url(service_name=None):
    if APP_ENV != 'production':
        url = "https://api-nirvana1.dev.cogoport.io"
        if service_name in ["organization", "partner", "user", "loki"]:
            url = url + "/{}".format(get_service(service_name))
        return url
    service_port = COMMON_SERVICE_PORT
    # if service_name in ['organization', 'user', 'lead', 'partner']:
    #     service_port = AUTH_SERVICE_PORT
    # if service_name in ['location', 'sailing_schedule']:
    #     service_port = COGOMAPS_SERVICE_PORT
    # if service_name == 'spot_search':
    #     service_port = SPOT_SEARCH_PORT
    # if service_name == 'checkout':
    #     service_port = CHECKOUT_PORT
    # if service_name == 'shipment':
    #     service_port = SHIPMENT_PORT
    # if service_name == 'loki':
    #     service_port = LOKI_PORT

    if service_name == 'common':
        instance_url = "http://{}:{}".format(INTERNAL_NLB, service_port)
    else:
        instance_url = "http://{}:{}/{}".format(INTERNAL_NLB, service_port, get_service(service_name))
    return instance_url
