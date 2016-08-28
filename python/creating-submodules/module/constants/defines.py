NAME = 'Jane P. Roult'

# Communication Definitions
BAUDRATE = 115200
COMMAND_COMM_LOCATION = "/dev/robot/arduino"  # For sending commands
SENSORS_COMM_LOCATION = "/dev/robot/sensors"  # For receiving sensor telemetry

# Physical Definitions
WHEEL_BASE_MM = 153.0

# Blue Wheels with geared steppers:
STEPS_PER_CM = 132.0

# Blue Wheels with wimpy-ass steppers:
# STEPS_PER_CM = 26
# Green Wheels with wimpy-ass steppers:
# STEPS_PER_CM = 35
# Green Wheels with gears steppers:
# STEPS_PER_CM = 182

STEPS_PER_MM = STEPS_PER_CM / 10.0
