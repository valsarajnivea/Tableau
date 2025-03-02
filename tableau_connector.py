import tableauserverclient as TSC
from contextlib import contextmanager

from config import SITE_NAME, SITE_URL, TOKEN_NAME, TOKEN_VALUE
from tableau_logging import tableau_logger

class TableauConnector():
    SITE_NAME = SITE_NAME
    SITE_URL = SITE_URL
    TOKEN_NAME = TOKEN_NAME
    TOKEN_VALUE = TOKEN_VALUE
    
    def __init__(self):
        server = None

    @contextmanager
    def sign_in(self):
        tableauAuth = TSC.PersonalAccessTokenAuth(self.TOKEN_NAME,self.TOKEN_VALUE, site_id = self.SITE_NAME)
        self.server = TSC.Server(self.SITE_URL, use_server_version=True)
        
        try:
            self.server.auth.sign_in(tableauAuth)
            yield self
        except Exception as e:
            tableau_logger.error(f"{e}")

    
    def query(self, type: str, **kwargs):
        endpoint = getattr(self.server, type)
        results = endpoint.filter(**kwargs)
        if len(results)==1:
            return results[0]
        elif len(results)>1:
            tableau_logger.error(f"Multiple '{type}' exist with given values")
        else:
            tableau_logger.error(f"Resource does not exist")