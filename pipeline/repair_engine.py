def repair(data):

    if "auth_schema" not in data:
        data["auth_schema"] = {
            "roles": []
        }

    return data