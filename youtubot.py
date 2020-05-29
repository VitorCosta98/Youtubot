from selenium import webdriver
import time

class Youtubot:
    def __init__(self):
        self.waitTime = 0
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        

    def fetchVideo(self):
        musics = input('Digite a musica: ')

        self.driver = webdriver.Chrome(executable_path=r'./chromedriver')

        self.driver.get('https://www.youtube.com/results?search_query=' + musics)

        musics = self.driver.find_element_by_xpath("//div[@id='contents']/ytd-video-renderer[1]")
        time.sleep(5)
        musics.click()
        time.sleep(5)

        timeDuration = self.driver.find_element_by_class_name('ytp-time-duration').get_attribute('innerHTML')
        print(timeDuration)        

        for index in range(4):
            if index == 0:
                self.waitTime += int(timeDuration[index]) * 60
            elif index == 2:
                self.waitTime += int(timeDuration[index] + timeDuration[index + 1]) + 2
                break
        
        time.sleep(self.waitTime)
        self.driver.close()
        bot.fetchVideo()

bot = Youtubot()
bot.fetchVideo()


