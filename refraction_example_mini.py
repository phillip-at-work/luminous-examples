from luminous.src.math.vector import Vector
from luminous.src.scene.scene import Scene
from luminous.src.element.element import SphereElement
from luminous.src.element.source import IsotropicSource
from luminous.src.element.detector import Camera

from matplotlib import pyplot as plt

scene = Scene(log_level=10, log_file="./results/luminous.log", standoff_distance=1e-8)
# scene.attach_ray_debugger()

src = IsotropicSource(center=Vector(0, 6, 1), radius=0.05, color=Vector(1,0,0))
scene += src

camera = Camera(width=500, height=500, position=Vector(0, 1, 0), pointing_direction=Vector(0, 0, 1), screen_width=1e-6, screen_height=1e-6)
scene += camera

scene += SphereElement(center=Vector(0, 0.999999, 3), radius=0.5e-6, color=Vector(0, 0.2, 0), refractive_index=1.5, transparent=True, user_params={'specular':0.25, 'n_s':10})
scene += SphereElement(center=Vector(0, 0.999999, 6), radius=0.5e-6, color=Vector(1, 0, 0), refractive_index=1.0, user_params={'specular':0.25, 'n_s':10})

scene.raytrace()

image = camera.view_data()

plt.imshow(image)
p = "./results/refraction_example_mini.png"
print(f"Refraction example (mini) plot saved to: {p}. runtime: {scene.elaspsed_time():.3f}. pixels: {camera.width * camera.height}")
plt.savefig(p)
plt.close()