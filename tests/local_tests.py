from pyiconlaser.client import IconLaserClient

laser = IconLaserClient()

print(laser.version())
print(laser.loaded_job())
print(laser.job_status())
print(laser.state())