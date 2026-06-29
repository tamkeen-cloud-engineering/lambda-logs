import json
import logging

# Set the root logger to DEBUG so it captures everything
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

def lambda_handler(event, context):
    # Grab the log level from the URL path parameter
    # e.g., if path is /api/log/warn, level is "warn"
    level = event.get('pathParameters', {}).get('level', 'info').lower()
    
    if level == 'debug':
        logger.debug("DEBUG: Database connection pool health check: 12 active connections.")
        msg = "Logged a DEBUG message."
    elif level == 'info':
        logger.info("INFO: User 'student_42' successfully logged in from IP 192.168.1.1.")
        msg = "Logged an INFO message."
    elif level == 'warn':
        logger.warning("WARN: High memory usage detected (82%). Performance may degrade.")
        msg = "Logged a WARNING message."
    elif level == 'error':
        logger.error("ERROR: Failed to fetch user profile. Database timeout after 5000ms.")
        msg = "Logged an ERROR message."
    elif level == 'critical':
        logger.critical("CRITICAL: Payment gateway unreachable. All checkout transactions are failing!")
        msg = "Logged a CRITICAL message."
    else:
        logger.info(f"INFO: Standard hit on fallback endpoint with value: {level}")
        msg = "Logged default message."

    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps({"status": "success", "message": msg, "simulated_level": level})
    }