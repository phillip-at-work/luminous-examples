from luminous.src.math.vector import Vector
from luminous.src.scene.scene import Scene
from luminous.src.scene.scene import Sphere, CheckeredSphere
from luminous.src.detector.detector import Imager
from luminous.src.source.source import Point


iterations = 100
t = 0

for i in range(iterations):

    # TODO source should also have pointing direction. for an isotropic source, use arbitrary default.
    source = Point(position=Vector(5, 5, -10), pointing_direction=Vector(0, 0, 1))
    detector = Imager(width=400, height=300, position=Vector(0, 0.35, -1), pointing_direction=Vector(0, 0, 1))
    scene = Scene(source=source, detector=detector)

    scene += Sphere(center=Vector(0.75, 0.1, 1), radius=0.6, color=Vector(0, 0, 1))
    scene += Sphere(center=Vector(-0.75, 0.1, 2.25), radius=0.6, color=Vector(0.5, 0.223, 0.5))
    scene += Sphere(center=Vector(-2.75, 0.1, 3.5), radius=0.6, color=Vector(1, 0.572, 0.184))
    scene += CheckeredSphere(center=Vector(0, -99999.5, 0), radius=99999, color=Vector(0.75, 0.75, 0.75), reflectance=0.25)

    rays = scene.raytrace()
    image = scene.resolve_rays(rays)
    t += scene.elaspsed_time()


print(f"runtime: {t/iterations}")
# 0.0522s

# plt.imshow(image)
# plt.show(block=True)