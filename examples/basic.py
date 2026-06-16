from pyiconlaser import IconLaserClient


laser = IconLaserClient()

print(laser.version())
print(laser.job_status())
print(laser.loaded_job())
print(laser.state())