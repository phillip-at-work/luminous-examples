from luminous.src.math.vector import Vector
from luminous.src.scene.scene import Scene
from luminous.src.element.element import Sphere, CheckeredSphere
from luminous.src.detector.detector import Camera
from luminous.src.source.source import Isotropic

from matplotlib import pyplot as plt


scene = Scene()

scene += Isotropic(position=Vector(5, 5, -10), pointing_direction=Vector(0, 0, 1))

camera_one = Camera(width=400, height=300, position=Vector(0, 0.35, -1), pointing_direction=Vector(0, 0, 1))
scene += camera_one

camera_two = Camera(width=400, height=300, position=Vector(0, 2, -1), pointing_direction=Vector(0, 3, 1))
scene += camera_two

scene += Sphere(center=Vector(0.75, 0.1, 1), radius=0.6, color=Vector(1, 0, 0))
scene += Sphere(center=Vector(-0.75, 0.1, 2.25), radius=0.6, color=Vector(0, 1, 0))
scene += Sphere(center=Vector(-2.75, 0.1, 3.5), radius=0.6, color=Vector(0, 0, 1))
scene += CheckeredSphere(center=Vector(0, -99999.5, 0), radius=99999, color=Vector(0.75, 0.75, 0.75), reflectance=0.25)

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