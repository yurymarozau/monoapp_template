class TrailingSlashAppendingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.path_info.endswith('/'):
            request.path_info += '/'
        response = self.get_response(request)
        return response
