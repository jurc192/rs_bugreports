
import pyrealsense2 as rs

def capture_depthframe(width=1280, height=720, exposure=0, laser_power=240, depth_preset=1):

    pipeline = rs.pipeline()
    config   = rs.config()
    config.enable_stream(rs.stream.depth, width, height)
    if (config.can_resolve(pipeline) == False):
        print("Resolution not supported")
        return

    print("Resolving configuration")
    sensor = config.resolve(pipeline)   # hangs here
    print("Resolved")
    sensor = sensor.get_device().first_depth_sensor()

    sensor.set_option(rs.option.depth_units, 0.0001)
    sensor.set_option(rs.option.enable_auto_exposure, False)
    sensor.set_option(rs.option.exposure, exposure)
    sensor.set_option(rs.option.laser_power, laser_power)
    sensor.set_option(rs.option.visual_preset, depth_preset)

    pipeline.start(config)
    frame = pipeline.wait_for_frames().get_depth_frame()
    config.disable_all_streams()
    pipeline.stop()
    return frame


if __name__ == "__main__":

    resolutions = [(1280, 720), (848, 480), (640, 480), (640, 360), (480, 270)]
    laserpowers = [150, 210, 240, 270, 300]
    exposures   = [4500, 6500, 8500, 10500, 12500]

    for res in resolutions:
        for exp in exposures:
            for lpow in laserpowers:
                capture_depthframe(*res, exp, lpow, 1)
