# GoCart
This repository will hold code that will manage the functions and feedback of an electric go cart. This code will interpret switch-panel, touch-panel, VESC, and ADC inputs for the go cart as well as process those values and display them via a GUI and a Smarti Pi. 

# INPUTS & OUTPUTS
- accelerator (AI)
- brake (AI)
- main power switch (DI)
- drive power switch (DI)
- forward/reverse switch (DI)

- VESC DATA (UART)
  - battery voltage
  - current x 2
  - power x 2
  - RPM x 2
  - mAh used x 2
  - mAh generated x 2
- VESC CONTROL (UART)
  - throttle
  - direction
  - current max (?)
  - brake current max (?)
  - RPM max (?)