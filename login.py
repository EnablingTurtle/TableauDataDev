

import argparse
import getpass
import logging
import tableauserverclient as TSC
import pandas as pd
import json

def main():

    query = """
    {
        fields{
            name
        }
    }
    """

    parser = argparse.ArgumentParser(description='Logs in to the server.')

    parser.add_argument('--logging-level', '-l', choices=['debug', 'info', 'error'], default='error',
                        help='desired logging level (set to error by default)')

    parser.add_argument('--server', '-s', required=True, help='server address')
    parser.add_argument('--token-name', '-n', help='name of the personal access token used to sign into the server')
    parser.add_argument('--token', '-t', help='personal token')
    parser.add_argument('--sitename', '-S', default=None)

    args = parser.parse_args()

    # Set logging level based on user input, or error by default.
    logging_level = getattr(logging, args.logging_level.upper())
    logging.basicConfig(level=logging_level)

    # Make sure we use an updated version of the rest apis.
    server = TSC.Server(args.server, use_server_version=True)
    tableau_auth = TSC.PersonalAccessTokenAuth(token_name=args.token_name,
                                               personal_access_token=args.token, site_id=args.sitename)
    with server.auth.sign_in_with_personal_access_token(tableau_auth):
        print('Logged in successfully')
        workbooks, pagination_item = server.workbooks.get()
        resp = server.metadata.query(query)
        datasources = resp['data']
        datasource = pd.json_normalize(datasources, max_level=1)
        print(datasource)

main()