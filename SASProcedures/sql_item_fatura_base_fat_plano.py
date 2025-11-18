from .proc_log import ProcLog

import json
import os
import pandas as pd

from SASExport import SASExport

class SQLItemFaturaBaseFatPlano(ProcLog):
    
    cilco = {
        'C01': '{ano}-{mes}-01T00:00:00Z'
        , 'C07': '{ano}-{mes}-07T00:00:00Z'
        , 'C14': '{ano}-{mes}-14T00:00:00Z'
        , 'C19': '{ano}-{mes}-19T00:00:00Z'
        , 'C25': '{ano}-{mes}-25T00:00:00Z'
    }
    
    def proc_item_fatura_base_fat(self, dt:str, log=False):
        print('proc item fatura base fat plano -- Iniciado')
        print('')
        
        self.ciclos = self.get_ciclos(dt)
        self.file = 'ITEM_FATURA_BASE_FAT_PLANO{data}.csv'.format(data='_'+max(self.ciclos)[:8].replace('-', ''))
        
        self.__get_path()
        self.__login(log=log)
        self.__create_table(log=log)
        self.__create_table2(log=log)
        self.__create_file(log=log)
        self.__download_file()
        
        print('')
        print('proc item fatura base fat plano -- Finalizado')

    def get_ciclos(self, dt_str:str):
        dt = pd.to_datetime(dt_str)
        return [
            v.format(
                ano=(dt + pd.DateOffset(months=-1)).strftime("%Y")
                , mes=(dt + pd.DateOffset(months=-1)).strftime("%m")
            )
            if k == 'C25' else
            v.format(
                ano=dt.strftime("%Y")
                , mes=dt.strftime("%m")
            )
            for k, v in self.cilco.items()
        ]    
    
    def __get_path(self):
        with open('path.json', 'r') as f:
            path_data = json.loads(f.read())
            self.path = os.path.join(path_data['path'].format(login=os.getlogin()), 'item_fatura')
            
    def __login(self, log=False):
        self.sas_export = SASExport(os.getlogin())
        self.sas_export.connect(log=False)
        
    def __create_table(self, log=False):
        query = self._ProcLog__exec(
            title = self.file
            , module = 'item fatura base fat plano'
            , crud = 'create'
            , name = 'create temp'
            , parm = {'dt_ini': min(self.ciclos), 'dt_fim': max(self.ciclos)}
        )
        self.sas_export.submit(query, log=False)
        
    def __create_table2(self, log=False):
        query = self._ProcLog__exec(
            title = self.file
            , module = 'item fatura base fat plano'
            , crud = 'create'
            , name = 'create temp2'
        )
        self.sas_export.submit(query, log=False)
        
    def __create_file(self, log=False):
        query = self._ProcLog__exec(
            title = self.file
            , module = 'item fatura base fat plano'
            , crud = 'create'
            , name = 'create file'
            , parm = {'path': self.sas_export.sas.workpath, 'file': self.file}
        )
        self.sas_export.submit(query, log=False)
        
    def __download_file(self):
        self.sas_export.download(
            self.path
            , self.file
            , unzip=False
        )
