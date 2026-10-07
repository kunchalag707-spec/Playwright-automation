import time
from playwright.sync_api import Page, expect



class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.email_input = page.locator("#ion-input-0")
        self.password_input = page.locator("#ion-input-1")
        self.submit_button = page.locator('ion-button[type="submit"]')
    

    def goto(self, base_url: str) -> None:
        self.page.goto(f"{base_url}/signin")
        
        

    def login(self, email: str, password: str) -> None:
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.submit_button.click()




        
        

    
    
    