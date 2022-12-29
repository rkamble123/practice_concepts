class NimapMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def process_request(self, request):
        request_path = request.get_full_path()
        hosted_by_nimap = request.gethostname()
        if hosted_by_nimap not in ['127.0.0.1', '192.168.0.1']:
            self.proess_exception()
        return request