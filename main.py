from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from decouple import config
from config import CHROME_PROFILE_PATH
import textwrap

MESSAGE = config('MESSAGE')

class WhatsAppBot:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument(CHROME_PROFILE_PATH)
        self.driver = webdriver.Chrome(options=options)
    
    def remove_indentation(self, message):
        # Remove a identação extra do texto
        return textwrap.dedent(message).strip()
    
    def send_message_with_line_breaks(self, message):
        lines = message.split('\n')
        message_input = self.driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div[2]/div[1]/p')
        message_input.clear()
        # Envia cada linha pressionando Shift + Enter (ou Shift + Return)
        for line in lines:
            message_input.send_keys(line)
            message_input.send_keys(Keys.SHIFT, Keys.ENTER)  # Simula Shift + Enter para quebra de linha

        message_input.send_keys(Keys.ENTER)
        time.sleep(10)
        

        # # Envia a mensagem
        # send_button = self.driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/span/div/span')
        # send_button.click()

    def connect_whatsapp(self):
        contatos = ["Habby (você)", "Bianca"]
        message = '''
        Desbloqueie o Poder da Business Intelligence (B.I.) - Controle Total para o Seu Negócio.

        Imagine uma ferramenta que coloca o controle total das finanças e operações da sua empresa literalmente nas suas mãos, em tempo real. Agora, essa visão está ao seu alcance com nossa solução de Business Intelligence desenvolvida pela Intech Sistemas.

        Com a nossa solução, você terá acesso a:

        - Contas a Pagar e a Receber Simplificadas;
        - Recebimentos Eletrônicos sem Surpresas;
        - Projeção de Vendas e Compras com Precisão;
        - Seu Estoque Sob Controle;
        - Projeção Orçamentária Financeira;
        - Fluxo de Caixa Sempre Transparente;

        E o melhor de tudo, é uma ferramenta online que você, nosso valioso cliente, pode acessar de qualquer lugar. Apenas a Intech Sistemas, líder em tecnologia, pode oferecer a você essa revolução no controle empresarial.

        Faça parte dessa transformação! Adote a B.I. e desbloqueie o potencial total da sua empresa. Entre em contato conosco hoje e comece a transformar seu negócio para melhor.

        ☎️ 84 99819-0606
        ☎️ 84 99819-0605
        '''
        navegador = self.driver
        navegador.get("https://web.whatsapp.com/")
        navegador.maximize_window()
        time.sleep(30)

        for i in range(len(contatos)):
            # Pesquisa o contato e seleciona
            search_input = navegador.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]/p')
            time.sleep(5)
            search_input.click()
            search_input.clear()
            search_input.send_keys(contatos[i])
            search_input.send_keys(Keys.ENTER)

            # Envia a imagem
            image_button = navegador.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div/div/div')
            image_button.click()
            option_image = navegador.find_element(By.XPATH, '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
            option_image.send_keys("/home/habby/Imagens/intech.jpeg")
            time.sleep(5)
            send_button = navegador.find_element(By.XPATH, '//*[@id="app"]/div/div/div[3]/div[2]/span/div/span/div/div/div[2]/div/div[2]/div[2]/div/div')
            send_button.send_keys(Keys.ENTER)            
            time.sleep(5)

            # Envia a mensagem com quebra de linha
            formatted_message = self.remove_indentation(message)
            self.send_message_with_line_breaks(formatted_message)

            time.sleep(5)
            

bibi_bot_wapp = WhatsAppBot()
bibi_bot_wapp.connect_whatsapp()