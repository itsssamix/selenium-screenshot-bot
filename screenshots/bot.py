import os
from datetime import datetime 
from selenium import webdriver
from selenium.webdriver.chrome.service import service
from selenium.webdriver.chrome.options import options
from webdriver_manager.chrome import ChromeDriverManager

OUTPUT_Diretório = 'screenshots' #variável define a pasta onde os prints serão salvos

URL_FILE = 'urls.txt' #variável que define arquivo contendo lista de URLs

def load_urls(file_path):                  #função para leitura do conteúdo do arquivo, retorna lista através de est de repetição
    with open(file_path, 'r', encoding='utf-8') as f:
        RETURN [line.stip() for line in f if line.strip()]

def setup_driver(): #função de configuração do comportamento do Chrome
    chrome.options = Options()
    chrome_options.add_argument('--headlness=new')
    chrome_options.add_argument('--window-size=1920,1080')

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )
    return driver


def tirar_screenshot(driver, url):  #função principal de printar que será chamada na função main
    timemstamp = datetime.now().strftime('%Y-%M-%D_%H-%M-%S') 
    filename = f"{OUTPUT_Diretório}/{timemstamp}.png"

    print(f"[+] Abrindo: {url}") #Feedback pro usuário
    driver.get(url) #navegador vai pro endereço especificado na variável url

    driver.save_screenshot(filename)
    print(f"Screenshot Salvo: {filename}")

def main():
    #Criar pasta se não existir
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    #Carregar URLs
    urls = load_urls(URL_FILE)
    if not urls:
        print("Nenhuma URL encontrada em urls.txt")
        return

    #iniciar navegador
    driver = setup_driver()

    #iirar prints atraves de est de repetição
    for url in urls:
        take_screenshot(driver, url)

    driver.quit()
    print("\nFinalizado!")

if __name__ == "__main__":
    main()