from pyiconlaser import IconLaserClient

laser = IconLaserClient()

laser.prepare_job("test_job")
laser.set_id("SN", "TEST123")
laser.enable_job()
laser.start()
laser.clear_job()