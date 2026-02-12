from luminous.src.math.vector import Vector
from luminous.src.scene.scene import Scene
from luminous.src.element.element import SphereElement, CheckeredSphereElement
from luminous.src.element.source import IsotropicSource
from luminous.src.element.detector import Camera

from matplotlib import pyplot as plt


iterations = 100
t = 0

for i in range(iterations):

    scene = Scene()

    scene += IsotropicSource(center=Vector(5, 5, -10), radius=0.05, color=Vector(1,0,0), pointing_direction=Vector(0, 0, 1))
    
    camera = Camera(width=400, height=300, position=Vector(0, 0.35, -1), pointing_direction=Vector(0, 0, 1), screen_width=2, screen_height=None)
    scene += camera

    scene += SphereElement(center=Vector(0.75, 0.1, 1), radius=0.6, color=Vector(0, 0, 1), user_params={'specular':0.25, 'n_s':10})
    scene += SphereElement(center=Vector(-0.75, 0.1, 2.25), radius=0.6, color=Vector(0.5, 0.223, 0.5), user_params={'specular':0.25, 'n_s':30})
    scene += SphereElement(center=Vector(-2.75, 0.1, 3.5), radius=0.6, color=Vector(1, 0.572, 0.184), user_params={'specular':1, 'n_s':10})
    scene += CheckeredSphereElement(center=Vector(0, -99999.5, 0), radius=99999, color=Vector(0.75, 0.75, 0.75), user_params={'specular':0.01, 'n_s':5})

    scene.raytrace()
    image = camera.view_data()
    t += scene.elaspsed_time()


print(f"runtime: {t/iterations}") # 0.0322s

plt.imshow(image)
p = "./results/timed_sample_example.png"
print(f"timed_sample example plot saved to: {p}")
plt.savefig(p)
plt.close()