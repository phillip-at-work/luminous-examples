# from matplotlib import pyplot as plt

# from luminous.src.math.vector import Vector
# from luminous.src.scene.scene import Scene
# from luminous.src.element.element import SphereElement
# from luminous.src.element.source import Laser
# from luminous.src.element.detector import PowerMeter

# scene = Scene(reverse_trace=False)

# # scene.attach_ray_debugger(path="./results", filename="debug_ray_trace")

# scene += Laser(center=Vector(0,0,0), radius=0.05, color=Vector(1,0,0), pointing_direction=Vector(0,1,0), pixel_count=50)

# wattmeter = PowerMeter(center=Vector(0,5,0), radius=0.5, pointing_direction=Vector(0,1,0))
# scene += wattmeter

# # scene += SphereElement(center=Vector(0.75, 0.1, 1), radius=0.6, color=Vector(0, 0, 1), user_params={'specular':0.25, 'n_s':10})
# # scene += SphereElement(center=Vector(0, 0, 3.5), radius=0.6, color=Vector(1, 0.572, 0.184), user_params={'specular':0.25, 'n_s':10})

# scene.raytrace()

# # image = wattmeter.view_data()

# # plt.imshow(image)
# # p = "./results/forward_trace_laser_power_meter.png"
# # print(f"forward_trace_laser_power_meter example plot saved to: {p}")
# # plt.savefig(p)
# # plt.close()