import pyautogui
import subprocess


class Screen:

    def __init__(self):
        self.screenSize = pyautogui.size()
        self.mousePosition = pyautogui.position()

    @staticmethod
    def FindElement(self, image):
        button = pyautogui.locateCenterOnScreen(image)
        return button

    @staticmethod
    def moveMouseTo(self, pos):
        pyautogui.moveTo(pos[0], pos[1])

    @staticmethod
    def click_image(self, png_name, clicks=2):
        if subprocess.call("system_profiler SPDisplaysDataType | grep 'retina'", shell=True) == 0:
            x = x / 2
            y = y / 2
        button = pyautogui.locateCenterOnScreen(png_name)
        pyautogui.click(button, clicks=clicks)
        return

    @staticmethod
    def dragTo(self, to, button='left'):
        pyautogui.dragTo(to[0], to[1], button=button)

    @staticmethod
    def write(text):
        for t in text:
            pyautogui.press(t)

