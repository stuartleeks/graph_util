from azure.identity import DefaultAzureCredential
from msgraph.core import GraphClient

client = None


def get_graph_client():
    global client
    if not client:
        creds = DefaultAzureCredential()
        client = GraphClient(
            credential=creds, scopes=["https://graph.microsoft.com/.default"]
        )
    return client


def user_from_json(user_json):
    """Converts a user JSON object to a user dictionary"""
    return {
        "upn": user_json.get("userPrincipalName", ""),
        "name": user_json.get("displayName", ""),
        "email": user_json.get("mail", ""),
        "city": user_json.get("city", ""),
        "country": user_json.get("country", ""),
        "department": user_json.get("department", ""),
        "jobTitle": user_json.get("jobTitle", ""),
        "office": user_json.get("officeLocation", "")
        if "officeLocation" in user_json
        else "",
        "phone": user_json.get("businessPhones", [])[0]
        if len(user_json.get("businessPhones", [])) > 0
        else "",
        "reports": [],
    }


def get_user_reports(user_name):
    """Gets all reports for a user"""
    reports = []
    # user fields: https://learn.microsoft.com/en-us/graph/api/resources/user?view=graph-rest-1.0
    ## TODO - add paging
    result = get_graph_client().get(
        f"https://graph.microsoft.com/v1.0/users/{user_name}/directReports",
        params={
            "$select": "displayName,mail,userPrincipalName,city,country,department,jobTitle,officeLocation,businessPhones"
        },
    )
    for user_json in result.json()["value"]:
        user = user_from_json(user_json)
        user["reports"] = get_user_reports(user["upn"])
        reports.append(user)
    return reports


def get_user_with_reports(user_name):
    """Gets a user and all their reports"""
    result = get_graph_client().get(
        f"https://graph.microsoft.com/v1.0/users/{user_name}",
        params={
            "$select": "displayName,mail,userPrincipalName,city,country,department,jobTitle,officeLocation,businessPhones"
        },
    )
    user_json = result.json()
    user = user_from_json(user_json)
    user["reports"] = get_user_reports(user["upn"])
    return user


def flatten_users(users):
    """Flattens a user tree into a list of users"""
    result = []
    for user in users:
        user_temp = user.copy()
        user_temp.pop("reports")
        result.append(user_temp)
        result.extend(flatten_users(user["reports"]))
    return result
