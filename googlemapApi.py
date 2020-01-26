from selenium import webdriver
import time

driver = webdriver.Chrome('chromedriver.exe')


def getVal():
        url = "https://mycurrentlocation.net/"
        driver.get(url)
        latEl = driver.find_element_by_xpath('//*[@id="latitude"]')
        lonEl = driver.find_element_by_xpath('//*[@id="longitude"]')

        print(latEl.text)
        print(lonEl.text)
        time.sleep(10)
        return [latEl.text, lonEl.text]


if __name__ == '__main__':
    val = getVal()
    print(val[0])
    driver.quit()

