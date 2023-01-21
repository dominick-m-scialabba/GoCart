# GoCart
This repository will hold code that will manage the functions and feedback of an electric go cart. This code will interpret switch-panel, touch-panel, and VESC inputs and outputs for the go cart as well as process and calculate values and display them via a GUI and a Smarti Pi touchscreen. 

# INPUTS & OUTPUTS
- accelerator/brake (AI)
- main power switch (DI)
- drive power switch (DI)
- forward/reverse switch (DI)
- headlights switch (DI)
- horn switch (DI)
- RGB switch outputs (3xDO)

- VESC DATA (UART or CAN)
  - speed
  - disatnce
  - battery voltage
  - battery current
  - motor current x 2
  - power x 2
  - RPM x 2
  - mAh used x 2
  - mAh generated x 2
