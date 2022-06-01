from django.shortcuts import redirect
from django.utils import timezone
def Time_middleware(get_response):

    def middleware(request):
        print('Before view Middleware')
        request.start_time = timezone.now()
        response = get_response(request)
        total_time = timezone.now() - request.start_time
        print('Time taken: {}'.format(total_time))
        print('After view Middleware')
        return response

    return middleware