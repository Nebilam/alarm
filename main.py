makerbit.set_lcd_backlight(LcdBacklight.ON)
makerbit.connect_lcd(39)
def on_forever():
    makerbit.show_string_on_lcd1602("Alarm on",
        makerbit.position1602(LcdPosition1602.P4),
        16,
        TextOption.PAD_WITH_ZEROS)
    pins.digital_write_pin(DigitalPin.P1, 1)
    basic.pause(1500)
    makerbit.clear_lcd1602()
    makerbit.show_string_on_lcd1602("Activity",
        makerbit.position1602(LcdPosition1602.P4),
        16,
        TextOption.PAD_WITH_ZEROS)
    makerbit.show_string_on_lcd1602("detected",
        makerbit.position1602(LcdPosition1602.P20),
        16,
        TextOption.PAD_WITH_ZEROS)
    pins.digital_write_pin(DigitalPin.P1, 0)
    basic.pause(1500)
    makerbit.clear_lcd1602()
basic.forever(on_forever)
def on_forever2():
    basic.show_leds("""
        # # # # #
        # # # # #
        # # # # #
        # # # # #
        # # # # #
        """,)
    basic.pause(100)
    basic.clear_screen()
    basic.pause(100)
basic.forever(on_forever2)