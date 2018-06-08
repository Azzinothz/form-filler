# encoding=utf8
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from time import sleep

def open_chrome():
    option = webdriver.ChromeOptions()
    option.add_argument('disable-infobars')
    ch_driver = webdriver.Chrome(chrome_options=option)
    return ch_driver


def operation_auth(cd_driver):
    url = "https://cas.shmtu.edu.cn/cas/login?service=http%3A%2F%2Fjwxt.shmtu.edu.cn%2Fshmtu%2Fhome%21index.action"
    cd_driver.get(url)
    username = cd_driver.find_element_by_id("username")
    username.send_keys("201610733026")
    password = cd_driver.find_element_by_id("password")
    password.send_keys("050915")
    cd_driver.find_element_by_xpath("//*[@id=\"fm1\"]/section[3]/input[4]").click()
    cd_driver.find_element_by_xpath("//*[@id=\"MLeft\"]/div/ul/li[6]/a/div").click()
    sleep(2)
    cd_driver.find_element_by_xpath("//*[@id=\"MLeft\"]/div/table[2]/tbody/tr[1]/td[1]/div[2]/a").click()
    for i in range(10, 20):
        sleep(2)
        cd_driver.find_element_by_xpath("// *[ @ id = \"evaluateForm\"] / table[2] / tbody / tr[" + str(i) + "] / td[6] / a").click()
        sleep(2)
        questions_odd = cd_driver.find_elements_by_css_selector(".griddata-odd")
        questions_even = cd_driver.find_elements_by_css_selector(".griddata-even")
        for question in questions_odd:
            options = question.find_elements_by_css_selector("input")
            value = []
            for option in options:
                value.append(option.get_attribute("value"))
            ans = max(value)
            for option in options:
                if option.get_attribute("value") == ans:
                    option.click()
                    break
        flag = 1
        for question in questions_even:
            options = question.find_elements_by_css_selector("input")
            value = []
            for option in options:
                value.append(option.get_attribute("value"))
            ans = max(value)
            if flag == 6:
                value.remove(max(value))
                value.remove(min(value))
                ans = value[0]
            for option in options:
                if option.get_attribute("value") == ans:
                    option.click()
                    break
            flag += 1
        cd_driver.find_element_by_xpath("//*[@id=\"content_1\"]").send_keys("都很有帮助。")
        cd_driver.find_element_by_xpath("//*[@id=\"content_2\"]").send_keys("已经很棒了。")
        cd_driver.find_element_by_xpath("//*[@id=\"btnSave\"]").click()
        cd_driver.switch_to_alert().accept()
        sleep(2)

    print('Succeed.')


if __name__ == '__main__':
    driver = open_chrome()
    operation_auth(driver)
