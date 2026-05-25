def execution_test(schema):

    required = [
        "ui_schema",
        "api_schema",
        "db_schema",
        "auth_schema"
    ]

    for item in required:
        if item not in schema:
            return {
                "status": "FAIL"
            }

    return {
        "status": "PASS"
    }