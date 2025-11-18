from sys import exit
import requests

class ProcLog:
    url = "http://167.99.156.207:1981/"

    headers = {
        "accept": "application/jason"
        , "Content-Type": "application/json"
    }

    data = {
        'project': 'p&cvas'
        , 'sgbd': 'sas'
    }

    def __init__(self):
        pass

    def __exec(self, title:str, module:str, crud:str, name:str, parm:dict=None, log=False):
        print("{title} -- Begin".format(title=title))
        data = self.data
        data['module'] = module
        data['crud'] = crud
        data['name'] = name
        try:
            response = requests.post(self.url, headers=self.headers, json=data)
            if parm:
                query = response.json()['message'].format(**parm)
            else:
                query = response.json()['message']
        except Exception as e:
            if log:
                print(f"An unexpected error occurred: {e}")
            exit("Error!")
#         print("{title} -- Finish".format(title=title))
        return query
