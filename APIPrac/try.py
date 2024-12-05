import logging
from django.http import HttpResponse

# Get the logger for this module
logger = logging.getLogger(__name__)

def my_view(request):
    try:
        # Simulate some logic
        result = 10 / 0  # This will raise a ZeroDivisionError
        return HttpResponse(f"Result: {result}")
    except ZeroDivisionError as e:
        # Log the error with exception details
        logger.error("An error occurred: %s", e, exc_info=True)
        return HttpResponse("An error occurred, check the logs for details.", status=500)