logs = [
    "INFO User logged in",
    "ERROR Database connection failed",
    "INFO Data processed",
    "ERROR Timeout occurred",
    "WARNING Low memory"
]

error_count = 0

for log in logs:
    if log.startswith("ERROR"):
        error_count += 1

print("Total ERROR logs:", error_count)
