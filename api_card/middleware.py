from logs.serializers import LogSerializer

class LoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        serializer = LogSerializer(data={
            'method': request.method,
            'endpoint': request.path,
            'code_status': response.status_code,
            'body': request.data
        })
        if serializer.is_valid():
            serializer.save()

        return response
