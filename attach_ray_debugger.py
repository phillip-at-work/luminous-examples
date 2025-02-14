from matplotlib import pyplot as plt

from luminous.src.math.vector import Vector
from luminous.src.scene.scene import Scene, Sphere
from luminous.src.detector.detector import Imager
from luminous.src.source.source import Isotropic

scene = Scene(log_level=10, log_file="./results/luminous.log")

scene.attach_ray_debugger(path="./results", filename="debug_ray_trace")

scene += Isotropic(position=Vector(5, 5, -10), pointing_direction=Vector(0, 0, 1))
scene += Imager(width=400, height=300, position=Vector(0, 0.35, -1), pointing_direction=Vector(0, 0, 1))

scene += Sphere(center=Vector(0.75, 0.1, 1), radius=0.6, color=Vector(0, 0, 1))
scene += Sphere(center=Vector(-2.75, 0.1, 3.5), radius=0.6, color=Vector(1, 0.572, 0.184))

rays = scene.raytrace()
image = scene.resolve_rays(rays)

plt.imshow(image)
p = "./results/attach_ray_debugger_example.png"
print(f"attach_ray_debugger example plot saved to: {p}")
plt.savefig(p)
plt.close()