from matplotlib import pyplot as plt

from luminous.src.math.vector import Vector
from luminous.src.scene.scene import Scene
from luminous.src.element.element import Sphere
from luminous.src.detector.detector import Camera
from luminous.src.source.source import Isotropic

scene = Scene(log_level=10, log_file="./results/luminous.log")

scene.attach_ray_debugger(path="./results", filename="debug_ray_trace")

scene += Isotropic(position=Vector(5, 5, -10), pointing_direction=Vector(0, 0, 1))

camera = Camera(width=75, height=75, position=Vector(0, 0.35, -1), pointing_direction=Vector(0, 0, 1))
scene += camera

scene += Sphere(center=Vector(0.75, 0.1, 1), radius=0.6, color=Vector(0, 0, 1))
# scene += Sphere(center=Vector(0, 0, 3.5), radius=0.6, color=Vector(1, 0.572, 0.184))

scene.raytrace()

image = camera.view_data()

plt.imshow(image)
p = "./results/attach_ray_debugger_basic_example.png"
print(f"attach_ray_debugger example plot saved to: {p}")
plt.savefig(p)
plt.close()