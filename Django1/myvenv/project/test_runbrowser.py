from selenium import webdriver

localhost = "http://127.0.0.1:8000/"
browser = webdriver.Firefox(executable_path='/Users/hp/Desktop/Testowanie/Django1/myvenv/Lib/site-packages/selenium/webdriver').get(localhost)

assert 'Django' in browser.title