# encoding=utf8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from selenium.webdriver.support.wait import WebDriverWait


def open_chrome():
    option = webdriver.ChromeOptions()
    option.add_argument('disable-infobars')
    ch_driver = webdriver.Chrome(chrome_options=option)
    return ch_driver


def operation_auth(cd_driver):
    url = "https://cas.shmtu.edu.cn/cas/login?service=http%3A%2F%2Fjwxt.shmtu.edu.cn%2Fshmtu%2Fhome%21index.action"
    cd_driver.get(url)
    username = cd_driver.find_element_by_id("username")
    username.send_keys("")
    password = cd_driver.find_element_by_id("password")
    password.send_keys("")
    cd_driver.find_element_by_xpath("//*[@id=\"fm1\"]/section[3]/input[4]").click()
    cd_driver.find_element_by_xpath("//*[@id=\"MLeft\"]/div/ul/li[6]/a/div").click()

    WebDriverWait(cd_driver, 10).until(
        expected_conditions.presence_of_element_located(
            (By.XPATH, "//*[@id=\"MLeft\"]/div/table[2]/tbody/tr[1]/td[1]/div[2]/a")
        )
    )

    cd_driver.find_element_by_xpath("//*[@id=\"MLeft\"]/div/table[2]/tbody/tr[1]/td[1]/div[2]/a").click()
    for i in range(1, 20):

        WebDriverWait(cd_driver, 10).until(
            expected_conditions.presence_of_element_located(
                (By.XPATH, "// *[ @ id = \"evaluateForm\"] / table[2] / tbody / tr[" + str(i) + "] / td[6] / a")
            )
        )

        course = cd_driver.find_element_by_xpath(
            "// *[ @ id = \"evaluateForm\"] / table[2] / tbody / tr[" + str(i) + "] / td[6] / a"
        )
        if course.text == '已评估':
            continue
        else:
            course.click()

        WebDriverWait(cd_driver, 10).until(
            expected_conditions.presence_of_element_located(
                (By.CSS_SELECTOR, "b")
            )
        )

        questions_odd = cd_driver.find_elements_by_css_selector(".griddata-odd")
        questions_even = cd_driver.find_elements_by_css_selector(".griddata-even")
        flag = 1
        for question in questions_odd:
            options = question.find_elements_by_css_selector("input")
            value = []
            for option in options:
                value.append(option.get_attribute("value"))
            ans = max(value)
            if flag == 6:
                max1 = max(value)
                min1 = min(value)
                ans = value[0]
            for option in options:
                if option.get_attribute("value") == ans:
                    option.click()
                    break
            flag += 1
        flag = 1
        for question in questions_even:
            options = question.find_elements_by_css_selector("input")
            value = []
            for option in options:
                value.append(option.get_attribute("value"))
            ans = max(value)
            if flag == 6:
                max2 = max(value)
                min2 = min(value)
                ans = value[0]
            for option in options:
                if option.get_attribute("value") == ans:
                    option.click()
                    break
            flag += 1
        cd_driver.find_element_by_xpath("//*[@id=\"content_1\"]").send_keys("都很有帮助。")
        cd_driver.find_element_by_xpath("//*[@id=\"content_2\"]").send_keys("已经很棒了。")
        cd_driver.find_element_by_xpath("//*[@id=\"btnSave\"]").click()
        msgbox = cd_driver.switch_to_alert()
        if msgbox.text == "确认提交?":
            cd_driver.switch_to_alert().accept()
        else:
            cd_driver.switch_to_alert().accept()
            options1 = cd_driver.find_element_by_xpath("//*[@id=\"evaluateTB\"]/tr[12]/td[2]").\
                find_elements_by_css_selector("input")
            options2 = cd_driver.find_element_by_xpath("//*[@id=\"evaluateTB\"]/tr[11]/td[3]").\
                find_elements_by_css_selector("input")
            ans1 = max1
            ans2 = min2
            for option in options1:
                if option.get_attribute("value") == ans1:
                    option.click()
                    break
            for option in options2:
                if option.get_attribute("value") == ans2:
                    option.click()
                    break
            cd_driver.find_element_by_xpath("//*[@id=\"btnSave\"]").click()
            msgbox = cd_driver.switch_to_alert()
            if msgbox.text == "确认提交?":
                msgbox.accept()
            else:
                cd_driver.switch_to_alert().accept()
                options1 = cd_driver.find_element_by_xpath("//*[@id=\"evaluateTB\"]/tr[12]/td[2]"). \
                    find_elements_by_css_selector("input")
                options2 = cd_driver.find_element_by_xpath("//*[@id=\"evaluateTB\"]/tr[11]/td[3]"). \
                    find_elements_by_css_selector("input")
                ans1 = min1
                ans2 = max2
                for option in options1:
                    if option.get_attribute("value") == ans1:
                        option.click()
                        break
                for option in options2:
                    if option.get_attribute("value") == ans2:
                        option.click()
                        break
                cd_driver.find_element_by_xpath("//*[@id=\"btnSave\"]").click()
                msgbox = cd_driver.switch_to_alert()
                if msgbox.text == "确认提交?":
                    msgbox.accept()
                else:
                    cd_driver.switch_to_alert().accept()
                    options1 = cd_driver.find_element_by_xpath("//*[@id=\"evaluateTB\"]/tr[12]/td[2]"). \
                        find_elements_by_css_selector("input")
                    options2 = cd_driver.find_element_by_xpath("//*[@id=\"evaluateTB\"]/tr[11]/td[3]"). \
                        find_elements_by_css_selector("input")
                    ans1 = max1
                    ans2 = max2
                    for option in options1:
                        if option.get_attribute("value") == ans1:
                            option.click()
                            break
                    for option in options2:
                        if option.get_attribute("value") == ans2:
                            option.click()
                            break
                    cd_driver.find_element_by_xpath("//*[@id=\"btnSave\"]").click()
                    msgbox = cd_driver.switch_to_alert()
                    msgbox.accept()

    print('Succeed.')


if __name__ == '__main__':
    driver = open_chrome()
    operation_auth(driver)
