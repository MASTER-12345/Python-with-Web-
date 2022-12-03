import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import requests
import  cv2




driver=webdriver.Chrome(executable_path="C:\\Users\\Administrator\\Desktop\\chromedriver\\chromedriver.exe")

url="https://pwd.dobest.cn/?pwdchoose=findpwd"
url2="https://pwd.dobest.cn/account"
driver.get(url2)

account="13251203158"
passport=driver.find_element_by_name("passport")
print(passport.text)
time.sleep(0.5)
passport.send_keys(account)
time.sleep(1)
inr=driver.find_element_by_xpath('//*[@id="form-submit"]/div[2]/input')
inr.click()




while True:
    try:

        # 滑块图
        time.sleep(2)
        bacimg = driver.find_element_by_class_name("backImg")
        bockimg = driver.find_element_by_class_name("bock-backImg")

        back = bacimg.get_attribute("src")
        bock = bockimg.get_attribute("src")

        content1 = requests.get(back).content
        f1 = open("img/1.jpg", mode="wb")
        f1.write(content1)
        f1.close()

        content2 = requests.get(bock).content
        f2 = open("img/2.jpg", mode="wb")
        f2.write(content2)
        f2.close()

        b1 = cv2.imread("img/1.jpg")
        b2=cv2.imread("img/2.jpg")

        bg_edge = cv2.Canny(b1, 100, 200)
        tp_edge = cv2.Canny(b2, 100, 200)
        bg_pic = cv2.cvtColor(bg_edge, cv2.COLOR_GRAY2RGB)
        tp_pic = cv2.cvtColor(tp_edge, cv2.COLOR_GRAY2RGB)

        # 缺口匹配
        res = cv2.matchTemplate(bg_pic, tp_pic, cv2.TM_CCOEFF_NORMED)

        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)  # 寻找最优匹配
        X = max_loc[0]
        # 绘制方框
        # th, tw = tp_pic.shape[:2]
        # tl = max_loc  # 左上角点的坐标
        # br = (tl[0] + tw, tl[1] + th)  # 右下角点的坐标
        # cv2.rectangle(b1, tl, br, (0, 0, 255), 2)  # 绘制矩形
        # cv2.imwrite('img/out.jpg', b1)  # 保存在本地
        ##########################################
        ActionChains(driver).drag_and_drop_by_offset(bockimg, X, 0).perform()
        print("松开了")
        time.sleep(0.6)

    except:
        print("找不到图")
        break

##转到邮箱
