import time
from django.core.cache import cache

class CacheGETMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if the HTTP method is GET
        if request.method == 'GET':
            # Generate a unique cache key based on the request path
            cache_key = f"cache_{request.get_full_path()}"
            
            # Try to fetch the response from the cache
            response = cache.get(cache_key)
            if response:
                return response  # Return the cached response if found

            # If not cached, process the request
            response = self.get_response(request)
            
            # Cache the response for 5 minutes (300 seconds)
            cache.set(cache_key, response, timeout=300)
            return response

        # Process non-GET requests as usual
        return self.get_response(request)
