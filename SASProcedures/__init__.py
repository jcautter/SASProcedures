from .sql_apuracao_pos import SQLApuracaoPos
from .sql_item_fatura_simplificado import SQLItemFaturaSimplificado
from .sql_item_fatura_base_fat_plano import SQLItemFaturaBaseFatPlano

class SASProcedures(
    SQLApuracaoPos
    , SQLItemFaturaSimplificado
    , SQLItemFaturaBaseFatPlano
):
    
    def __init__(self):
        pass