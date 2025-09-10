from luminous.src.math.vector import Vector
from luminous.src.scene.scene import Scene
from luminous.src.element.element import Sphere
from luminous.src.detector.detector import Camera
from luminous.src.source.source import Isotropic

from matplotlib import pyplot as plt

scene = Scene()
# scene.attach_ray_debugger()

scene += Isotropic(position=Vector(0, 6, 1), pointing_direction=Vector(0, -1, 1))

camera = Camera(width=100, height=100, position=Vector(0, 1, 0), pointing_direction=Vector(0, 0, 1))
scene += camera

scene += Sphere(center=Vector(0, 0, 3), radius=1, color=Vector(0, 0.2, 0), refractive_index=1.5, transparent=True, user_params={'diffuse': Vector(1,1,1), 'specular':0.25, 'n_s':10})
scene += Sphere(center=Vector(1, 0, 6), radius=1, color=Vector(1, 0, 0), refractive_index=1.0, user_params={'diffuse': Vector(1,1,1), 'specular':0.25, 'n_s':10})

scene.raytrace()

image = camera.view_data()

plt.imshow(image)
p = "./results/refraction_example.png"
print(f"Refraction example plot saved to: {p}. runtime: {scene.elaspsed_time():.3f}. pixels: {camera.width * camera.height}")
plt.savefig(p)
plt.close()