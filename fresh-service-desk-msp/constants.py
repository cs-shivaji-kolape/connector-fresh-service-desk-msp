ERROR_MSGS = {
    400: 'Bad/Invalid Request',
    401: 'Unauthorized: Invalid credentials or token provided failed to authorize',
    403: 'Access Denied',
    404: 'Not Found',
    500: 'Internal Server Error',
    503: 'Service Unavailable'
}

STATUS_MAP = {'Open': 2, 'Pending': 3, 'Resolved': 4, 'Closed': 5}
PRIORITY_MAP = {'Low': 1, 'Medium': 2, 'High': 3, 'Urgent': 4}