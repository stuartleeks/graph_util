"""This is a sample script that uses the Microsoft Graph API to get a all reports for a user"""
import click
import json

from graphutil.graph.user import get_user_photo, get_user_with_reports, flatten_users
from graphutil.output import output_result, output_option, query_option


@click.group("user", help="Query user data")
def user_command() -> None:
    pass


@click.command("reports", help="Get all reports for a user")
@click.argument("user")
@output_option()
@query_option()
def user_reports_command(user, output_format, query):
    user_tree = get_user_with_reports(user)
    user_list = flatten_users([user_tree])

    result_json = json.dumps(user_list)
    output_result(
        result_json,
        output_format=output_format,
        query=query,
        default_table_query=r"[].{name:name, mail:mail, upn:upn, department:department}",
    )


@click.command("photo", help="Get a user's photo")
@click.argument("user")
@click.argument("filename")
def user_photo(user, filename):
    get_user_photo(user, filename)


user_command.add_command(user_photo)
user_command.add_command(user_reports_command)
