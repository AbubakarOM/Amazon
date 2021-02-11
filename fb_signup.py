from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as abu
from selenium.webdriver.support.wait import WebDriverWait

@given(u'I am on Facebook page')
# constructor
def step_impl(context): 
    context.driver = webdriver.Chrome()
    context.driver.get("https://web.facebook.com/")
    context.driver.maximize_window()
    wait = WebDriverWait(context.driver, 60)
    wait.until(abu.visibility_of_element_located((By.CSS_SELECTOR, "input#email")))
    context.driver.find_element_by_css_selector("input#email").send_keys("abu4real_md@yahoo.com")
    context.driver.find_element_by_css_selector( "input#pass").send_keys("@password")
    context.driver.find_element_by_xpath_selector( "//html[@id='facebook']//button[@id='u_0_f']").click()

@step(u'I click on dropdown')
def step_impl(context):
    wait = WebDriverWait(context.driver, 10)
    wait.until(abu.visibility_of_element_located((By.CSS_SELECTOR, "div[role='button'] > .hu5pjgll.lzf7d6o1.sp_Q_hfOj-xGcZ_3x.sx_8ab2d3")))
    element = context.driver.find_element_by_css_selector("div[role='button'] > .hu5pjgll.lzf7d6o1.sp_Q_hfOj-xGcZ_3x.sx_8ab2d3")
    context.driver.execute_script("arguments[0].scrollIntoView();", element)
    element.click()

@step(u'I click on profile')
def step_impl(context):
    wait = WebDriverWait(context.driver, 60)
    wait.until(abu.visibility_of_element_located((By.CSS_SELECTOR, ".aov4n071:nth-of-type(1) > [data-visualcompletion='ignore-dynamic']:nth-of-type(1) .f10w8fjw")))
    context.driver.find_element_by_css_selector(".aov4n071:nth-of-type(1) > [data-visualcompletion='ignore-dynamic']:nth-of-type(1) .f10w8fjw").click()

@step(u'I click on home icon')
def step_impl(context):
    wait = WebDriverWait(context.driver, 60)
    wait.until(abu.visibility_of_element_located((By.CSS_SELECTOR, ".hw7htvoc:nth-of-type(1) [height]")))
    context.driver.find_element_by_css_selector(".hw7htvoc:nth-of-type(1) [height]").click()

@step(u'I click on new user name')
def step_impl(context):
    wait = WebDriverWait(context.driver, 60)
    wait.until(abu.visibility_of_element_located((By.CSS_SELECTOR, "[data-pagelet] .buofh1pr:nth-of-type(1) > ul:nth-of-type(1) .stjgntxs")))
    context.driver.find_element_by_css_selector("[data-pagelet] .buofh1pr:nth-of-type(1) > ul:nth-of-type(1) .stjgntxs").click()

@step(u'I click on list view')
def step_impl(context):
    wait = WebDriverWait(context.driver, 60)
    wait.until(abu.visibility_of_element_located((By.CSS_SELECTOR, ".ozuftl9m .buofh1pr:nth-of-type(1) .k4urcfbm")))
    context.driver.find_element_by_css_selector(".ozuftl9m .buofh1pr:nth-of-type(1) .k4urcfbm").click()

@step(u'I click on grid view')
def step_impl(context):
    wait = WebDriverWait(context.driver, 60)
    wait.until(abu.visibility_of_element_located((By.CSS_SELECTOR, ".btwxx1t3.ozuftl9m .buofh1pr:nth-of-type(2) [dir]")))
    context.driver.find_element_by_css_selector(".btwxx1t3.ozuftl9m .buofh1pr:nth-of-type(2) [dir]").click()

@step(u'i click on filters')
def step_impl(context):
    wait = WebDriverWait(context.driver, 10)
    wait.until(abu.visibility_of_element_located((By.CSS_SELECTOR, ".hddg9phg .cxgpxx05 > div:nth-of-type(1) .g0qnabr5")))
    element = context.driver.find_element_by_css_selector(".hddg9phg .cxgpxx05 > div:nth-of-type(1) .g0qnabr5")
    context.driver.execute_script("arguments[0].scrollIntoView();", element)
    element.click()

@step(u'I click on go to year')
def step_impl(context):
    wait = WebDriverWait(context.driver, 60)
    wait.until(abu.visibility_of_element_located((By.CSS_SELECTOR, "//html[@id='facebook']//div[@id='jsc_c_fo']/span[.='1990']")))
    context.driver.find_element_by_css_selector("//html[@id='facebook']//div[@id='jsc_c_fo']/span[.='1990']").click()

@step(u'I click on go to month')
def step_impl(context):
    wait = WebDriverWait(context.driver, 60)
    wait.until(abu.visibility_of_element_located((By.CSS_SELECTOR, "//html[@id='facebook']//div[@id='jsc_c_g0']/span[.='june']")))
    context.driver.find_element_by_css_selector("//html[@id='facebook']//div[@id='jsc_c_g0']/span[.='june']").click()

@step(u'I click on go to date')
def step_impl(context):
    wait = WebDriverWait(context.driver, 60)
    wait.until(abu.visibility_of_element_located((By.CSS_SELECTOR, "//html[@id='facebook']/body/div[2]/div/div[1]/div/div[4]/div/div[@class='l9j0dhe7 tkr6xdv7']/div[1]/div[@class='h3gjbzrl l9j0dhe7']/div[2]/div/div/div[@role='dialog']//div[@class='j83agx80']/div[3]/div[@role='combobox']/span[.='18']")))
    context.driver.find_element_by_css_selector("//html[@id='facebook']/body/div[2]/div/div[1]/div/div[4]/div/div[@class='l9j0dhe7 tkr6xdv7']/div[1]/div[@class='h3gjbzrl l9j0dhe7']/div[2]/div/div/div[@role='dialog']//div[@class='j83agx80']/div[3]/div[@role='combobox']/span[.='18']").click()

@step(u'I click on posted By')
def step_impl(context):
    wait = WebDriverWait(context.driver, 60)
    wait.until(abu.visibility_of_element_located((By.CSS_SELECTOR, "//html[@id='facebook']//div[@id='jsc_c_fr']/span[.='you']")))
    context.driver.find_element_by_css_selector("//html[@id='facebook']//div[@id='jsc_c_fr']/span[.='you']").click()
    
@step(u'I click on privacy')
def step_impl(context):
    wait = WebDriverWait(context.driver, 60)
    wait.until(abu.visibility_of_element_located((By.CSS_SELECTOR, "//html[@id='facebook']//div[@id='jsc_c_fu']/span[.='Only Me']")))
    context.driver.find_element_by_css_selector("//html[@id='facebook']//div[@id='jsc_c_fu']/span[.='Only Me']").click()
    
@step(u'I i clcik on tagged posts')
def step_impl(context):
    wait = WebDriverWait(context.driver, 60)
    wait.until(abu.visibility_of_element_located((By.CSS_SELECTOR, "//html[@id='facebook']//div[@id='jsc_c_fx']/span[.='All Posts']")))
    context.driver.find_element_by_css_selector("//html[@id='facebook']//div[@id='jsc_c_fx']/span[.='All Posts']").click()

@then(u'I click on done')
def step_impl(context):
    wait = WebDriverWait(context.driver, 60)
    wait.until(abu.visibility_of_element_located((By.CSS_SELECTOR, "//html[@id='facebook']/body/div[2]/div/div[1]/div//div[@class='h3gjbzrl l9j0dhe7']/div[2]/div/div/div[@role='dialog']/div[3]/div[3]/div/div[1]/div[@role='button']")))
    context.driver.find_element_by_css_selector("//html[@id='facebook']/body/div[2]/div/div[1]/div//div[@class='h3gjbzrl l9j0dhe7']/div[2]/div/div/div[@role='dialog']/div[3]/div[3]/div/div[1]/div[@role='button']").click()

@when(u'I click on Manage posts')
def step_impl(context):
    wait = WebDriverWait(context.driver, 60)
    wait.until(abu.visibility_of_element_located((By.CSS_SELECTOR, ".lq239pai .h676nmdw .g0qnabr5")))
    context.driver.find_element_by_css_selector(".lq239pai .h676nmdw .g0qnabr5").click()

@step(u'i click on checkbox')
def step_impl(context):
    wait = WebDriverWait(context.driver, 60)
    wait.until(abu.visibility_of_element_located((By.CSS_SELECTOR, "//html[@id='facebook']/body/div[2]/div/div[1]/div/div[4]/div/div[@class='l9j0dhe7 tkr6xdv7']/div[1]/div[@class='h3gjbzrl l9j0dhe7']/div[2]/div/div/div[@role='dialog']/div/div[1]//div[@class='dati1w0a hv4rvrfc']/div[1]/div[2]/div/div[1]//input[@name='checkbox']")))
    checkbox = context.driver.find_element_by_xpath("//html[@id='facebook']/body/div[2]/div/div[1]/div/div[4]/div/div[@class='l9j0dhe7 tkr6xdv7']/div[1]/div[@class='h3gjbzrl l9j0dhe7']/div[2]/div/div/div[@role='dialog']/div/div[1]//div[@class='dati1w0a hv4rvrfc']/div[1]/div[2]/div/div[1]//input[@name='checkbox']")
    checkbox.click()

@step(u'I click next')
def step_impl(context):
    wait = WebDriverWait(context.driver, 60)
    wait.until(abu.visibility_of_element_located((By.CSS_SELECTOR, "//html[@id='facebook']/body/div[2]/div/div[1]/div//div[@class='h3gjbzrl l9j0dhe7']/div[2]/div/div/div[@role='dialog']/div/div[1]//div[@class='h676nmdw']/div[@role='button']/div[1]/div/span/span[.='Next']")))
    context.driver.find_element_by_css_selector("//html[@id='facebook']/body/div[2]/div/div[1]/div//div[@class='h3gjbzrl l9j0dhe7']/div[2]/div/div/div[@role='dialog']/div/div[1]//div[@class='h676nmdw']/div[@role='button']/div[1]/div/span/span[.='Next']").click()

@step(u'I click hide post')
def step_impl(context):
    wait = WebDriverWait(context.driver, 60)
    wait.until(abu.visibility_of_element_located((By.CSS_SELECTOR, "//html[@id='facebook']/body/div[2]/div/div[1]/div//div[@class='h3gjbzrl l9j0dhe7']/div[2]/div/div/div[@role='dialog']/div/div[2]/div/div[4]/div[1]/div[1]//div[@role='radio']")))
    radio = context.driver.find_element_by_xpath("//html[@id='facebook']/body/div[2]/div/div[1]/div//div[@class='h3gjbzrl l9j0dhe7']/div[2]/div/div/div[@role='dialog']/div/div[2]/div/div[4]/div[1]/div[1]//div[@role='radio']")
    radio.click()

@step(u'I click done')
def step_impl(context):
    wait = WebDriverWait(context.driver, 60)
    wait.until(abu.visibility_of_element_located((By.CSS_SELECTOR, "//html[@id='facebook']/body/div[2]/div/div[1]//div[@class='h3gjbzrl l9j0dhe7']/div[2]/div/div/div[@role='dialog']/div/div[2]/div/div[4]/div[2]/div/div/div[@role='button']")))
    context.driver.find_element_by_css_selector("//html[@id='facebook']/body/div[2]/div/div[1]//div[@class='h3gjbzrl l9j0dhe7']/div[2]/div/div/div[@role='dialog']/div/div[2]/div/div[4]/div[2]/div/div/div[@role='button']").click()


