
# ---------- METADATA ----------
title = "FoodIt"
version = .1
description = f"""
# Welcome to FoodItApi!
"""
contact_email = "ignacio.pieve@gmail.com"

metadata = {
    "title": title,
    "version": version,
    "contact": {
        "name": f"{title} Team",
        "email": contact_email,
    },
    "description": description,
    "docs_url": "/",
}

# ---------- CONFIG VARIABLES ----------

DB_URL = f"postgresql+psycopg2://foodit:foodit@foodit-database:5432/app"
