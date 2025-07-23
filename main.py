import os

import google.generativeai as genai


def read_api_key_from_file(file_path: str) -> str:
    """Reads the Gemini API key from a file."""
    with open(file_path, 'r') as file:
        return file.read().strip()


# Set your Gemini API key
genai.configure(api_key=read_api_key_from_file("apikey.txt"))

negative_keywords = [
    "exceeded",
    "failed",
    "fail",
    "failure",
    "error",
    "exception",
    "fatal",
    "critical",
    "panic",
    "abort",
    "denied",
    "rejected",
    "timeout",
    "unavailable",
    "unreachable",
    "invalid",
    "corrupt",
    "overflow",
    "underflow",
    "missing",
    "not found",
    "cannot",
    "unable",
    "disconnect",
    "down",
    "crash",
    "bug",
    "broken",
    "halt",
    "stopped",
    "stop",
    "off",
    "refused",
    "lost",
    "terminated",
    "deprecated",
    "blocked",
    "conflict",
    "unauthorized",
    "forbidden",
    "expired",
    "malformed",
    "incomplete",
    "limit",
    "overflow",
    "retry",
    "shutdown",
    "warning",
    "assert",
    "traceback",
    "stacktrace"
]



def is_log_critical(log_message: str) -> bool:
    """
    Uses Gemini API to determine whether a log message is critical.
    Returns True if critical, False otherwise.
    """
    prompt = (
        "You are a helpful assistant. Determine if the following log message is critical.\n"
        "Return only JSON response only whether log message is 'CRITICAL' true or false along with the log message itself as 'message'.\n"
        f"Log message: {log_message}"
    )

    model = genai.GenerativeModel('gemini-2.0-flash')
    response = model.generate_content(prompt)

    output = response.text.strip().upper()
    return output

# Example usage
log_msg = "Database connection failed: timeout after 30s"
is_critical = is_log_critical(log_msg)
print(f"Is the log message critical? {is_critical}")