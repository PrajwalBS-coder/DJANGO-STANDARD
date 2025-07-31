import json
import logging
from django.utils.deprecation import MiddlewareMixin

api_logger = logging.getLogger('api_logger')  # Use correct logger name

class APILoggingMiddleware(MiddlewareMixin):
    def process_request(self, request):
        request.api_log_data = {
            "method": request.method,
            "path": request.path,
            # "body": request.body.decode('utf-8') if request.body else None
        }

    def process_response(self, request, response):
        if hasattr(request, "api_log_data"):
            MAX_RESPONSE_LENGTH = 500  # Limit response size

            request.api_log_data["status"] = response.status_code
            
            try:
                response_content = response.content.decode('utf-8') if response.content else ""
            except UnicodeDecodeError:
                response_content = "[Binary data not shown]"

            # Truncate long responses
            if len(response_content) > MAX_RESPONSE_LENGTH:
                truncated_response = response_content[:MAX_RESPONSE_LENGTH] + "... [TRUNCATED]"
            else:
                truncated_response = response_content

            # Log API call
            log_message = (
                f"API Call: {request.api_log_data['method']} {request.api_log_data['path']} - "
                # f"Status: {request.api_log_data['status']} - Request: {request.api_log_data['body']} - "
                f"Response: {truncated_response}"
            )

            api_logger.info(log_message)  # Now logs in api.log

        return response
