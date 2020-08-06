import pyspeedtest

speedr = pyspeedtest.SpeedTest("www.youtube.com")

print(speedr.ping())
print(float(speedr.download())/1024)
#speedr.upload()
