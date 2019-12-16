makerbit.setLcdBacklight(LcdBacklight.On)
makerbit.connectLcd(39)
basic.forever(function () {
    makerbit.showStringOnLcd1602("Alarm on", makerbit.position1602(LcdPosition1602.P4), 16, TextOption.PadWithZeros)
    pins.digitalWritePin(DigitalPin.P1, 1)
    basic.pause(1500)
    makerbit.clearLcd1602()
    makerbit.showStringOnLcd1602("Activity", makerbit.position1602(LcdPosition1602.P4), 16, TextOption.PadWithZeros)
    makerbit.showStringOnLcd1602("detected", makerbit.position1602(LcdPosition1602.P20), 16, TextOption.PadWithZeros)
    pins.digitalWritePin(DigitalPin.P1, 0)
    basic.pause(1500)
    makerbit.clearLcd1602()
})
basic.forever(function () {
    basic.showLeds(`
        # # # # #
        # # # # #
        # # # # #
        # # # # #
        # # # # #
        `)
    basic.pause(100)
    basic.clearScreen()
    basic.pause(100)
})
