#!/usr/bin/python3
# Basic migration from Nextcloud JSON (export) to Bitwarden JSON (import)
# - folders are not supported
# - type is only 'login' (no "card" "identity" or "secure note")
#
# Bitwarden JSON format doc: https://bitwarden.com/help/export-your-data/
#
# Authors: Martin Monperrus, Paul Lardet
# Original URL: https://gist.github.com/monperrus/c671817d53f6fc4bfe8d1773f28262d7
# New repository: https://github.com/godisopensource/np2bw/
# License: Public domain

import csv
import json
from datetime import datetime, timezone

def csv_to_json(csv_file_path, json_file_path):
    with open(csv_file_path, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        data = list(reader)

    with open(json_file_path, 'w', encoding='utf-8') as jsonfile:
        json.dump(data, jsonfile, indent=4, ensure_ascii=False)

csv_file_path = "Passwords_2025-05-14.csv" # Put CSV database from Nextcloud Passwords
json_file_path = "nextcloudpasswords.json" # Json converted file will be here
csv_to_json(csv_file_path, json_file_path)

with open(json_file_path, "r", encoding='utf-8') as file:
    kp = json.load(file)

def entry_to_bw_json(entry):
    current_time = datetime.now(timezone.utc).isoformat()
    
    return {
        "passwordHistory": None,
        "revisionDate": current_time,
        "creationDate": current_time,
        "deletedDate": None,
        "id": entry.get("Id", ""),
        "organizationId": None,
        "folderId": entry.get("Folder", None),
        "type": 1,
        "reprompt": 0,
        "name": entry.get("Label", ""),
        "notes": entry.get("Notes") or None,
        "favorite": entry.get("Favorite", "").lower() == "true",
        "login": {
            "fido2Credentials": [],
            "uris": [{"match": None, "uri": entry.get("Url", "")}] if entry.get("Url") else [],
            "username": entry.get("Username", ""),
            "password": entry.get("Password", ""),
            "totp": None
        },
        "collectionIds": None
    }

def export(kp):
    items = [entry_to_bw_json(i) for i in kp]
    data = {
        "encrypted": False,
        "folders": [],
        "items": items
    }
    
    print(f'Imported {len(items)} elements')
    
    try:
        with open('bitwarden_import.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"Successfully saved file to bitwarden_import.json")
    except Exception as e:
        print('An error occurred while trying to save json file:', e)

export(kp)

