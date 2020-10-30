from selenium import webdriver

LOGIN = "mocurin"
PASSWORD = "i_love_ilya :3"


if __name__ == "__main__":
    _driver = webdriver.Chrome()
    _driver.get("http://ejudge.bmstu.cloud/new-client?contest_id=3")
    place_for_login = _driver.find_element_by_xpath("//input[@name='login']")
    place_for_password = _driver.find_element_by_xpath("//input[@name='password']")
    place_for_login.send_keys(LOGIN)
    place_for_password.send_keys(PASSWORD)
    button = _driver.find_element_by_name("action_2")
    button.click()
    A_task = _driver.find_element_by_link_text("C")
    A_task.click()
    prosmotr = _driver.find_elements_by_link_text("Просмотр")
    prosmotr[1].click()
    inputs = _driver.find_elements_by_link_text("I")

    for i in range(len(inputs)):
        inputs = _driver.find_elements_by_link_text("I")
        f = open(f'input_{i + 1}.txt', 'w')
        inputs[i].click()
        try:
            text = _driver.find_element_by_tag_name("pre").text
        except:
            text = ""
        _driver.back()
        f.write(text)
        f.close()

        answers = _driver.find_elements_by_link_text("A")
        f = open(f'answer_{i + 1}.txt', 'w')
        answers[i].click()
        try:
            text = _driver.find_element_by_tag_name("pre").text
        except:
            text = ""
        _driver.back()
        f.write(text)
        f.close()

