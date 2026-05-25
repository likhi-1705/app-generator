def generate_schemas(blueprint):

    pages = blueprint["pages"]

    if "Patients" in pages:

        return {
            "ui_schema": {
                "pages": pages
            },

            "api_schema": {
                "endpoints": [
                    "/patients",
                    "/doctors",
                    "/appointments"
                ]
            },

            "db_schema": {
                "tables": [
                    "patients",
                    "doctors",
                    "appointments"
                ]
            },

            "auth_schema": {
                "roles": blueprint["roles"]
            }
        }

    elif "Products" in pages:

        return {
            "ui_schema": {
                "pages": pages
            },

            "api_schema": {
                "endpoints": [
                    "/products",
                    "/cart",
                    "/orders"
                ]
            },

            "db_schema": {
                "tables": [
                    "products",
                    "orders",
                    "customers"
                ]
            },

            "auth_schema": {
                "roles": blueprint["roles"]
            }
        }

    else:

        return {
            "ui_schema": {
                "pages": pages
            },

            "api_schema": {
                "endpoints": [
                    "/login",
                    "/contacts"
                ]
            },

            "db_schema": {
                "tables": [
                    "users",
                    "contacts"
                ]
            },

            "auth_schema": {
                "roles": blueprint["roles"]
            }
        }