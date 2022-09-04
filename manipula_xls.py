# Módulo manipula XLS
# Este módulo oferece funções para manipulação de arquivos
# no formato .xls.
# Autor: Francisco Gomes
# Data: 20220904
# Versão: 0.0.1

# importando pacotes

from openpyxl import workbook


def cria_xls() -> workbook:
    """Esta função cria uma pasta de trabalho MS-Excel."""
    pasta = workbook
    return pasta
    
def cria_planilha(nome_planilha: str, pasta: workbook) -> None:
    pasta.active
    pasta.create_sheet(planilha, pasta)
    