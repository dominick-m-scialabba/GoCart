# ADC Reading ##########################################################################################################
#
# Dominick M. Scialabba, 6/12/22
#
# This program will read and interpret throttle and brake voltages via an ADC to determine user control input.


# Libraries ############################################################################################################
import numpy as NP
import time as TIME
# import board as BOARD
# import busio as BUSIO
# import adafruit_ads11x5.ads1115 as ADC
# from adafruit_ads11x5.analog_in import AnalogIn
import HMI


# ADC and Board Initialization
i2c = BUSIO.I2C(BOARD.SCL, BOARD.SDA)
adc = ADC.ADS1115(i2c)


# ADC Parameters
adc_pins = ['P0', 'P1']
adc_sample_rate = 100               # in hertz
adc.gain = 1                    # multiplicative factor, 2/3, 1, 2, 4, 8, 16
adc.mode = Mode.SINGLE          # ADC report mode, SINGLE for multi-channel input, CONTINUOUS is faster for one channel


# ADC Channel Initialization
channel_0 = AnalogIn(adc, ADC.adc_pins[0])
channel_1 = AnalogIn(adc, ADC.adc_pins[1])
channel_2 = AnalogIn(adc, ADC.adc_pins[2])
channel_3 = AnalogIn(adc, ADC.adc_pins[3])


# ADC Data Reading
while True:
    # Record Current Throttle and Brake Voltage
    throttle_voltage = channel_0.voltage
    brake_value = channel_1.voltage

    # Impose Sampling Rate
    TIME.sleep(1/adc_sample_rate)

    # Stop Reading if the GUI is Closed
    if HMI.event == HMI.GUI.WINDOW_CLOSED:
        break

