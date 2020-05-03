import pyrealsense2 as rs
pipeline = rs.pipeline()
config   = rs.config()
# config.enable_stream(rs.stream.depth, 1, 848, 480, rs.format.z16, 15) # can't resolve
# config.enable_stream(rs.stream.depth, 1)                              # can't resolve
# config.enable_stream(rs.stream.depth, rs.format.z16, 15)              # works
# config.enable_stream(rs.stream.depth, 848, 480, rs.format.z16, 15)    # USB2 fails, USB3 works
# config.enable_stream(rs.stream.depth, 1, rs.format.z16, 15)           # can't resolve

# config.enable_stream(rs.stream.depth, 848, 480)                       # works
# config.enable_stream(rs.stream.depth, 848, 480, rs.format.z16)        # can't resolve
profile = config.resolve(pipeline)
