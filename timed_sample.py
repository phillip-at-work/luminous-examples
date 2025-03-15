from luminous.src.math.vector import Vector
from luminous.src.scene.scene import Scene, Sphere, CheckeredSphere
from luminous.src.detector.detector import Camera
from luminous.src.source.source import Isotropic

from matplotlib import pyplot as plt


iterations = 100
t = 0

for i in range(iterations):

    scene = Scene()

    scene += Isotropic(position=Vector(5, 5, -10), pointing_direction=Vector(0, 0, 1))
    
    camera = Camera(width=400, height=300, position=Vector(0, 0.35, -1), pointing_direction=Vector(0, 0, 1))
    scene += camera

    scene += Sphere(center=Vector(0.75, 0.1, 1), radius=0.6, color=Vector(0, 0, 1))
    scene += Sphere(center=Vector(-0.75, 0.1, 2.25), radius=0.6, color=Vector(0.5, 0.223, 0.5))
    scene += Sphere(center=Vector(-2.75, 0.1, 3.5), radius=0.6, color=Vector(1, 0.572, 0.184))
    scene += CheckeredSphere(center=Vector(0, -99999.5, 0), radius=99999, color=Vector(0.75, 0.75, 0.75), reflectance=0.25)

    scene.raytrace()
    image = camera.view_data()
    t += scene.elaspsed_time()


print(f"runtime: {t/iterations}") # 0.0322s

plt.imshow(image)
p = "./results/timed_sample_example.png"
print(f"timed_sample example plot saved to: {p}")
plt.savefig(p)
plt.close()