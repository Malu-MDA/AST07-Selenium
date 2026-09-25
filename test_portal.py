import os
import time
from pathlib import Path

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


@pytest.fixture
def navegador():
    opcoes = webdriver.ChromeOptions()

    # No GitHub Actions, o Chrome será executado sem abrir uma janela.
    if os.getenv("CI") == "true":
        opcoes.add_argument("--headless=new")
        opcoes.add_argument("--no-sandbox")
        opcoes.add_argument("--disable-dev-shm-usage")

    navegador = webdriver.Chrome(options=opcoes)

    caminho_portal = Path(__file__).parent / "portal.html"
    navegador.get(caminho_portal.resolve().as_uri())

    time.sleep(2)

    yield navegador

    time.sleep(2)
    navegador.quit()


def test_preencher_formulario(navegador):

    # Verifica o título da página
    assert navegador.title == "Portal do Colaborador"
    time.sleep(2)

    # Localiza e preenche o campo Nome
    nome = navegador.find_element(By.ID, "nome_usuario")
    nome.send_keys("Maria Luiza")
    time.sleep(2)

    # Localiza e preenche o campo E-mail
    email = navegador.find_element(By.ID, "email")
    email.send_keys("maria.luiza@empresa.com")
    time.sleep(2)

    # Localiza e clica no botão Enviar Dados
    botao = navegador.find_element(By.ID, "btn-enviar")
    botao.click()
    time.sleep(2)

    # Localiza a mensagem de sucesso
    mensagem = navegador.find_element(By.ID, "msg-sucesso")

    # Verifica se a mensagem está visível
    assert mensagem.is_displayed()

    # Verifica o texto da mensagem
    assert mensagem.text == "Dados enviados com sucesso!"

    time.sleep(2)


def test_acoes_avancadas_mouse(navegador):

    # Cria uma instância do ActionChains
    acoes = ActionChains(navegador)

    # Localiza o botão de duplo clique
    botao_duplo = navegador.find_element(By.ID, "btn-duplo")

    time.sleep(2)

    # Executa o duplo clique
    acoes.double_click(botao_duplo).perform()

    time.sleep(2)

    # Verifica se o texto mudou
    assert botao_duplo.text == "Autorizado!"

    time.sleep(2)

    # Localiza o botão de clique direito
    botao_direito = navegador.find_element(By.ID, "btn-direito")

    time.sleep(2)

    # Executa o clique com o botão direito
    acoes.context_click(botao_direito).perform()

    time.sleep(2)

    # Verifica se o texto mudou
    assert botao_direito.text == "Menu Aberto!"

    time.sleep(2)


def test_acoes_teclado(navegador):

    # Localiza o campo de observações
    campo = navegador.find_element(By.ID, "obs")

    time.sleep(2)

    # Clica no campo
    campo.click()

    time.sleep(1)

    # Seleciona todo o texto
    campo.send_keys(Keys.CONTROL, "a")

    time.sleep(1)

    # Apaga o texto selecionado
    campo.send_keys(Keys.BACKSPACE)

    time.sleep(2)

    # Digita o novo texto
    campo.send_keys("Teste automatizado finalizado.")

    time.sleep(2)

    # Verifica se o valor digitado está correto
    assert campo.get_attribute("value") == "Teste automatizado finalizado."

    time.sleep(2)