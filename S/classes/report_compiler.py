from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager, ChromeType
from datetime import datetime


class ReportCompiler(webdriver.Chrome):

    def __init__(self):
        print('Bot started on', datetime.now())
        options = webdriver.ChromeOptions()
        prefs = {
            'profile.managed_default_content_settings.images': 2,
            'intl.accept_languages': 'en-GB'
        }
        options.add_experimental_option('prefs', prefs)
        super().__init__(service=Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()),
                         options=options)
        self.implicitly_wait(5)

    def compile(self) -> str:
        self.get('https://www.google.com/search?q=previsao+do+tempo+para+Morrinhos')
        report_div = self.find_element(By.ID, 'wob_wc')
        return report_div.text.strip()

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Bot execution terminated on', datetime.now())
        self.quit()
