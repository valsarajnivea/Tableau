import tableauserverclient as TSC
import argparse

from tableau_connector import TableauConnector

parser = argparse.ArgumentParser("Tableau")
parser.add_argument('-w', '--workbook-name', type=str, help='Name of the workbook')
parser.add_argument('-p', '--project-name', type=str, help='Name of the project')
args = parser.parse_args()

conn = TableauConnector()

with conn.sign_in():
    workbook_item = conn.query(type='workbooks', 
                               name=args.workbook_name, 
                               project_name=args.project_name)
    
    conn.server.workbooks.populate_connections(workbook_item)
    for connection_item in workbook_item.connections:
        if connection_item.server_address == 'hourly-juicy-phoebe.data-1.use1.tembo.io':
            connection_item.server_port = '5432'
            conn.server.workbooks.update_connection(workbook_item, connection_item=connection_item)
    
# python 2502_EditConnection.py --workbook-name 'SampleWorkbook' --project-name '202502'










