def validate_output(data):

    required = [
        "ui_schema",
        "api_schema",
        "db_schema",
        "auth_schema"
    ]

    for key in required:
        if key not in data:
            return False

    pages = data["ui_schema"]["pages"]
    tables = data["db_schema"]["tables"]

    if "Patients" in pages and "patients" not in tables:
        return False

    if "Doctors" in pages and "doctors" not in tables:
        return False

    if "Appointments" in pages and "appointments" not in tables:
        return False

    return True