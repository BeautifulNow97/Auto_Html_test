import time

from pypinyin import lazy_pinyin, Style
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import logger

x = logger.Logger("debug")

# 网页刷新解决方案
# http://www.saoniuhuo.com/article/detail-485316.html


class LoginHtml(object):
    # 操作时间间隔
    USER_SLEEP_TIME = 1

    def __init__(self, u_name, u_tel, u_pinyin, n_star, n_end):
        self.u_name = u_name
        self.u_tel = u_tel
        self.u_pinyin = u_pinyin
        self.n_star = n_star
        self.n_end = n_end

    @staticmethod
    def upper_u_name(name_str):
        res = []
        for i in lazy_pinyin(name_str, style=Style.FIRST_LETTER):
            res.append(i.upper())
        return "".join(res)

    def login(self):
        driver = webdriver.Chrome()
        for i in range(self.n_star, self.n_end + 1):
            if i < 10:
                i = '0' + str(i)

            auto_url = "http://www.shuishantang88.com/reg.php"
            driver.get(auto_url)
            driver.maximize_window()

            self.succes_name = self.u_pinyin + str(i)
            driver.find_element(By.NAME, "u_user").send_keys(self.succes_name)
            driver.find_element(By.NAME, "u_name").send_keys(self.u_name)
            driver.find_element(By.NAME, "u_pass").send_keys("123456")
            driver.find_element(By.NAME, "u_pass2").send_keys("123456")
            # time.sleep(self.USER_SLEEP_TIME)
            driver.find_element(By.XPATH, '//*[@id="reg_xy"]/span').click()
            # 立即注册
            driver.find_element(By.XPATH, '//*[@id="form1"]/ul/li[6]/div/button').click()
            x.debug("用户注册完成")

            # 切换页面增加延时时间
            time.sleep(self.USER_SLEEP_TIME)
            # 菜单
            driver.find_element(By.XPATH, '//*[@id="header"]/div[2]/div/span').click()
            # 隐式等待
            # driver.implicitly_wait(1)  # seconds
            time.sleep(self.USER_SLEEP_TIME)
            # 套装类型
            driver.find_element(By.XPATH, '//*[@id="header"]/div[3]/a[2]').click()
            # time.sleep(10)
            # 立即购买
            time.sleep(0.5)
            driver.find_element(By.XPATH, '//span[@onclick="AddBuy(1);"]').click()
            # print("立即购买")
            time.sleep(self.USER_SLEEP_TIME)
            # 立即结算
            # print("立即结算")
            driver.find_element(By.XPATH, '//*[@id="user_kjs_total"]/div/input').click()
            x.debug("立即结算")
            # print("添加收货地址")
            # 添加收货地址-姓名
            time.sleep(self.USER_SLEEP_TIME)
            driver.find_element(By.NAME, 'u_name').send_keys(self.u_name)
            driver.find_element(By.NAME, 'u_tel').send_keys(self.u_tel)
            driver.find_element(By.NAME, 'u_address').send_keys("龙湖国际")
            ele = driver.find_element(By.NAME, "u_province")
            select_ele = Select(ele)
            select_ele.select_by_visible_text("重庆市")
            time.sleep(self.USER_SLEEP_TIME/2)
            ele1 = driver.find_element(By.NAME, "u_city")
            select_ele1 = Select(ele1)
            select_ele1.select_by_visible_text("重庆市")
            time.sleep(self.USER_SLEEP_TIME/2)
            ele2 = driver.find_element(By.NAME, "u_district")
            select_ele2 = Select(ele2)
            select_ele2.select_by_visible_text("渝北区")
            time.sleep(self.USER_SLEEP_TIME/2)
            driver.find_element(By.XPATH, '//*[@id="checkout_address_edit_form"]/form/div/div').click()
            time.sleep(self.USER_SLEEP_TIME)
            x.debug("添加收货地址")

            # 退出选项
            driver.find_element(By.XPATH, '//*[@id="header"]/ul/li[1]/a/img').click()
            time.sleep(self.USER_SLEEP_TIME)
            driver.find_element(By.XPATH, '// *[ @ id = "user_menu"] / a[4] / p').click()
            time.sleep(self.USER_SLEEP_TIME)
            driver.find_element(By.XPATH, '//*[@id="header"]/ul/li[1]/a/img').click()
            time.sleep(self.USER_SLEEP_TIME)
            driver.find_element(By.XPATH, '//*[@id="login_reg"]/div[2]/a').click()
            # winsound.Beep(600, 1000)

            time.sleep(self.USER_SLEEP_TIME)
            print(time.asctime() + '完成注册账号：' + self.succes_name + " 姓名：" + self.u_name + " 电话：" + self.u_tel)
            x.debug('完成注册账号：' + self.succes_name + " 姓名：" + self.u_name + " 电话：" + self.u_tel)
        driver.close()
        driver.quit()



if __name__ == '__main__':
    """
        
        陈彬 XLCB59-100  17772428063 2022年9月9日16:40:28完成100
    """
    u_name = "杨平tes"
    u_tel = "13658496088"
    u_pinyin = "sas"
    n_star = 17
    n_end = 20
    obj = LoginHtml(u_name, u_tel, u_pinyin, n_star, n_end)
    obj.login()
