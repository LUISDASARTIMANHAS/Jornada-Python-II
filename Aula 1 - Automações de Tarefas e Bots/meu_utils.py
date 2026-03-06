import pyautogui

def escrever_e_tab(valor: str) -> None:
    """
    Escreve um valor e pressiona TAB.

    @param valor: Texto que será digitado no campo atual
    @return None
    """
    if str(valor) != "nan":
        pyautogui.write(str(valor))
    pyautogui.press("tab")


def preencher_campos(linha) -> None:
    """
    Percorre todos os campos de uma linha do pandas e preenche no sistema.

    @param linha: Linha da tabela pandas (Series)
    @return: None
    """
    print("\n TRABALHANDO NA LINHA \n")
    print(linha)
    for campo in linha:
        escrever_e_tab(campo)