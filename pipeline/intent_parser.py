def extract_intent(prompt: str):

    prompt = prompt.lower()

    if "crm" in prompt:
        return {
            "app_type": "CRM",
            "features": ["login", "contacts", "dashboard"],
            "roles": ["admin", "user"]
        }

    elif "hospital" in prompt:
        return {
            "app_type": "Hospital",
            "features": ["patients", "doctors", "appointments"],
            "roles": ["admin", "doctor", "patient"]
        }

    elif "e-commerce" in prompt or "ecommerce" in prompt:
        return {
            "app_type": "ECommerce",
            "features": ["products", "cart", "payments"],
            "roles": ["admin", "customer"]
        }

    else:
        return {
            "app_type": "Generic",
            "features": ["dashboard"],
            "roles": ["admin"]
        }