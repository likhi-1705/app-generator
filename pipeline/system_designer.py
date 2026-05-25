def design_system(intent):

    app_type = intent["app_type"]

    if app_type == "CRM":
        return {
            "entities": ["User", "Contact"],
            "pages": ["Login", "Dashboard", "Contacts"],
            "roles": intent["roles"]
        }

    elif app_type == "Hospital":
        return {
            "entities": ["Patient", "Doctor", "Appointment"],
            "pages": ["Login", "Patients", "Doctors", "Appointments"],
            "roles": intent["roles"]
        }

    elif app_type == "ECommerce":
        return {
            "entities": ["Product", "Order", "Customer"],
            "pages": ["Login", "Products", "Cart", "Orders"],
            "roles": intent["roles"]
        }

    else:
        return {
            "entities": ["User"],
            "pages": ["Dashboard"],
            "roles": intent["roles"]
        }