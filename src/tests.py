import time
from lib.color_setup import SSD
import lib.sdcard as sdcard
from machine import Pin, SPI
import uos
from lib.keyboard import Keyboard, KeyboardObserver


def obs_cb(button_id, label):
    print("ID: ", button_id, " Label: ", label)


def sd_test():
    cs = Pin(1, Pin.OUT)
    spi = SPI(0,
              baudrate=1000000,
              polarity=0,
              phase=0,
              bits=8,
              firstbit=SPI.MSB,
              sck=Pin(2),
              mosi=Pin(3),
              miso=Pin(4))
    sd = sdcard.SDCard(spi, cs)
    vfs = uos.VfsFat(sd)
    uos.mount(vfs, "/sd")
    print(uos.listdir("/sd"))

    # Create a file and write something to it
    with open("/sd/test01.txt", "w") as file:
        file.write("SD card text.\r\n")

    # Open the file we just created and read from it
    with open("/sd/test01.txt", "r") as file:
        data = file.read()
        print(data)
        # sd_text_test(data.replace('\n', '').replace('\r', ''))


def eink_test():
    epd = EPD_4in2()
    epd.image1Gray.fill(0xff)
    epd.image4Gray.fill(0xff)

    epd.image4Gray.text("Waveshare", 5, 10, epd.black)
    epd.image4Gray.text("Pico_ePaper-4.2", 5, 40, epd.black)
    epd.image4Gray.text("Raspberry Pico", 5, 70, epd.black)
    epd.EPD_4IN2_4GrayDisplay(epd.buffer_4Gray)
    epd.delay_ms(500)

    epd.image4Gray.vline(10, 90, 60, epd.black)
    epd.image4Gray.vline(90, 90, 60, epd.black)
    epd.image4Gray.hline(10, 90, 80, epd.black)
    epd.image4Gray.hline(10, 150, 80, epd.black)
    epd.image4Gray.line(10, 90, 90, 150, epd.black)
    epd.image4Gray.line(90, 90, 10, 150, epd.black)
    epd.EPD_4IN2_4GrayDisplay(epd.buffer_4Gray)
    epd.delay_ms(500)

    epd.image4Gray.rect(10, 180, 50, 80, epd.black)
    epd.image4Gray.fill_rect(70, 180, 50, 80, epd.black)
    epd.EPD_4IN2_4GrayDisplay(epd.buffer_4Gray)
    epd.delay_ms(500)

    epd.image4Gray.fill_rect(150, 10, 250, 30, epd.black)
    epd.image4Gray.text('GRAY1 with black background', 155, 21, epd.white)
    epd.image4Gray.text('GRAY2 with white background', 155, 51, epd.grayish)
    epd.image4Gray.text('GRAY3 with white background', 155, 81, epd.darkgray)
    epd.image4Gray.text('GRAY4 with white background', 155, 111, epd.black)
    epd.EPD_4IN2_4GrayDisplay(epd.buffer_4Gray)
    epd.delay_ms(5000)

    #     print("Support for partial refresh, but the refresh effect is not good, but it is not recommended\r\n")
    #     print("Partial refresh\r\n")
    #     epd.EPD_4IN2_Init()
    #     for i in range(0, 10):
    #         print(str(i))
    #         epd.image1Gray.fill_rect(0, 200, 10, 10, epd.white)
    #         epd.image1Gray.text(str(i), 2, 201, epd.black)
    #         epd.EPD_4IN2_PartialDisplay(0, 200, 10, 10, epd.buffer_1Gray)

    epd.EPD_4IN2_Init()
    epd.EPD_4IN2_Clear()
    epd.Sleep()


# def sd_text_test(text):
#     epd.EPD_4IN2B_Init()
#     epd.imageblack.text(text, 250, 10, 0x00)
#     epd.EPD_4IN2B_Display(epd.buffer_black, epd.buffer_red)
#     epd.delay_ms(20)
#     epd.Sleep()
#
#
# def eink_clear():
#     epd.EPD_4IN2B_Init()
#     epd.EPD_4IN2B_Clear()
#     epd.delay_ms(20)
#     epd.Sleep()


def keyboard_test():
    keyboard = Keyboard([21, 22, 26, 27, 28], ["OK", "UP", "DOWN", "LEFT", "RIGHT"])
    obs = KeyboardObserver(obs_cb)
    keyboard.connect(obs)
    time.sleep(5)
