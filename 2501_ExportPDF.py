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
    pdf_options = TSC.PDFRequestOptions(orientation=TSC.PDFRequestOptions.Orientation.Portrait, 
                                        maxage = 1)
    
    conn.server.workbooks.populate_pdf(workbook_item)
    workbook_pdf =  workbook_item.pdf
    with open('files/pdfresult.pdf', 'wb') as f:
        f.write(workbook_pdf)
    
# python 2501_ExportPDF.py --workbook-name 'Superstore' --project-name 'Samples'








