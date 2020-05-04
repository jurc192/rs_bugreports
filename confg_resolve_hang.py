
import pyrealsense2 as rs
from time import sleep

def capture_depthframe():

    pipeline = rs.pipeline()
    config   = rs.config()
    config.enable_stream(rs.stream.depth)
    print("\tResolving configuration....", end='')
    profile = config.resolve(pipeline)   # hangs here after 200-ish iterations
    print("OK")
    pipeline.start(config)
    pipeline.stop()

for i in range(500):
    print(i, end='')
    capture_depthframe()
