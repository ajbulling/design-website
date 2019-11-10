from Adafruit_ADS1x15 import ADS1x15
import matplotlib.pyplot as plt
import numpy as np
import time

pga = 0256
sps = 860
adc = ADS1x15(ic=0x01)
adc.startContinuousConversion(0,pga,sps)
data = []
print("Go!")
for num in range(1000):
	data.append(adc.getLastConversionResults())
	time.sleep(0.01)
adc.stopContinuousConversion()

t = np.arange(1000)
plt.plot(t, data)
plt.show()

