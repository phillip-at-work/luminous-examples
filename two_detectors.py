from luminous.src.math.vector import Vector
from luminous.src.scene.scene import Scene
from luminous.src.element.element import SphereElement, CheckeredSphereElement
from luminous.src.element.source import IsotropicSource
from luminous.src.element.detector import Camera

from matplotlib import pyplot as plt


scene = Scene()
# scene.attach_ray_debugger()

scene += IsotropicSource(center=Vector(5, 5, -10), radius=0.05, color=Vector(1,0,0))

camera_one = Camera(width=400, height=300, position=Vector(0, 0.35, -1), pointing_direction=Vector(0, 0, 1), screen_width=2, screen_height=None)
scene += camera_one

camera_two = Camera(width=400, height=300, position=Vector(0, 2, -1), pointing_direction=Vector(0, 3, 1), screen_width=2, screen_height=None)
scene += camera_two

scene += SphereElement(center=Vector(0.75, 0.1, 1), radius=0.6, color=Vector(1, 0, 0), user_params={'specular':0.25, 'n_s':10})
scene += SphereElement(center=Vector(-0.75, 0.1, 2.25), radius=0.6, color=Vector(0, 1, 0), user_params={'specular':0.25, 'n_s':10})
scene += SphereElement(center=Vector(-2.75, 0.1, 3.5), radius=0.6, color=Vector(0, 0, 1), user_params={'specular':0.25, 'n_s':10})
scene += CheckeredSphereElement(center=Vector(0, -99999.5, 0), radius=99999, color=Vector(0.75, 0.75, 0.75), user_params={'specular':0.25, 'n_s':10})

scene.raytrace()

image_one = camera_one.view_data()
plt.imshow(image_one)
p = "./results/two_detectors_1of2.png"
print(f"two_detectors example plot saved to: {p}")
plt.savefig(p)
plt.close()

image_two = camera_two.view_data()
plt.imshow(image_two)
p = "./results/two_detectors_2of2.png"
print(f"two_detectors example plot saved to: {p}")
plt.savefig(p)
plt.close()