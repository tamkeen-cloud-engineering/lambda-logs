import json
import logging

# Set the root logger to DEBUG so it captures everything
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

LEVEL_LABELS = {
    "debug": "DEBUG",
    "info": "INFO",
    "warn": "WARN",
    "error": "ERROR",
    "critical": "CRITICAL",
}

DEFAULT_MESSAGES = {
    "debug": "DEBUG: Database connection pool health check: 12 active connections.",
    "info": "INFO: User 'student_42' successfully logged in from IP 192.168.1.1.",
    "warn": "WARN: High memory usage detected (82%). Performance may degrade.",
    "error": "ERROR: Failed to fetch user profile. Database timeout after 5000ms.",
    "critical": "CRITICAL: Payment gateway unreachable. All checkout transactions are failing!",
}

LOG_METHODS = {
    "debug": logger.debug,
    "info": logger.info,
    "warn": logger.warning,
    "error": logger.error,
    "critical": logger.critical,
}


def lambda_handler(event, context):
    level = (event.get("pathParameters") or {}).get("level", "info").lower()
    content = (event.get("queryStringParameters") or {}).get("content")

    if content:
        label = LEVEL_LABELS.get(level, "INFO")
        log_message = f"{label}: {content}"
    else:
        log_message = DEFAULT_MESSAGES.get(level)

    log_func = LOG_METHODS.get(level)
    if log_func and log_message:
        log_func(log_message)
        msg = f"Logged a {level.upper()} message."
    else:
        fallback_msg = (
            log_message
            or f"INFO: Standard hit on fallback endpoint with value: {level}"
        )
        logger.info(fallback_msg)
        msg = "Logged default message."

    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(
            {"status": "success", "message": msg, "simulated_level": level}
        ),
    }
