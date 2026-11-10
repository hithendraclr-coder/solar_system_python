from vpython import *
import random
import math

scene = canvas(
    title="3D SOLAR SYSTEM",
    width=1100,
    height=720,
    background=vector(0.005, 0.008, 0.025)
)
scene.range = 36
scene.center = vector(0, 0, 0)
scene.forward = vector(-1, -0.45, -1)
scene.caption = "\nDrag to rotate | Scroll to zoom | Right-click and drag to pan\n"

# Star-filled space background
stars = []
for _ in range(650):
    x = random.uniform(-90, 90)
    y = random.uniform(-90, 90)
    z = random.uniform(-90, 90)
    stars.append(vector(x, y, z))

points(
    pos=stars,
    color=color.white,
    radius=0.10
)

# Sun
sun = sphere(
    pos=vector(0, 0, 0),
    radius=2.2,
    color=vector(1, 0.55, 0.05),
    emissive=True,
    shininess=0.8
)

sun_glow = sphere(
    pos=vector(0, 0, 0),
    radius=2.65,
    color=vector(1, 0.35, 0.02),
    opacity=0.12,
    emissive=True
)

local_light(pos=vector(0, 0, 0), color=vector(1, 0.85, 0.65))

# Planet data: name, orbit distance, radius, colour, orbital speed, rotation speed
planet_data = [
    ("Mercury", 4.0, 0.32, vector(0.65, 0.62, 0.58), 1.60, 0.50),
    ("Venus",   6.0, 0.52, vector(0.95, 0.68, 0.30), 1.18, 0.25),
    ("Earth",   8.5, 0.58, vector(0.15, 0.48, 1.00), 0.95, 1.20),
    ("Mars",   11.0, 0.43, vector(0.90, 0.25, 0.12), 0.78, 1.00),
    ("Jupiter",15.5, 1.25, vector(0.78, 0.58, 0.40), 0.42, 1.60),
    ("Saturn", 20.0, 1.05, vector(0.88, 0.76, 0.50), 0.31, 1.35),
    ("Uranus", 24.5, 0.78, vector(0.40, 0.82, 0.88), 0.23, 0.90),
    ("Neptune",29.0, 0.76, vector(0.18, 0.32, 0.95), 0.18, 0.95)
]

planets = []

for name, distance, radius, shade, orbit_speed, spin_speed in planet_data:
    orbit_points = []
    for i in range(181):
        angle = 2 * math.pi * i / 180
        orbit_points.append(
            vector(distance * math.cos(angle), 0, distance * math.sin(angle))
        )

    curve(
        pos=orbit_points,
        radius=0.012,
        color=vector(0.22, 0.25, 0.36)
    )

    planet_options = {}
    if name == "Earth":
        planet_options["texture"] = textures.earth
    elif name == "Jupiter":
        planet_options["texture"] = textures.rough

    planet = sphere(
        pos=vector(distance, 0, 0),
        radius=radius,
        color=shade,
        shininess=0.7,
        make_trail=False,
        **planet_options
    )

    planet_label = label(
        pos=planet.pos,
        text=name,
        xoffset=12,
        yoffset=12,
        height=10,
        box=False,
        line=False,
        opacity=0,
        color=color.white
    )

    planet_ring = None
    if name == "Saturn":
        planet_ring = ring(
            pos=planet.pos,
            axis=vector(0.25, 1, 0.15),
            radius=1.65,
            thickness=0.28,
            color=vector(0.85, 0.72, 0.48),
            opacity=0.8
        )

    planets.append({
        "body": planet,
        "label": planet_label,
        "distance": distance,
        "angle": random.uniform(0, 2 * math.pi),
        "orbit_speed": orbit_speed,
        "spin_speed": spin_speed,
        "ring": planet_ring
    })

# A small moon orbiting Earth
moon_orbit = curve(
    pos=[
        vector(8.5 + 0.95 * math.cos(i * 2 * math.pi / 100), 0,
               0.95 * math.sin(i * 2 * math.pi / 100))
        for i in range(101)
    ],
    radius=0.008,
    color=vector(0.35, 0.38, 0.48)
)
moon = sphere(
    pos=vector(9.45, 0, 0),
    radius=0.16,
    color=vector(0.78, 0.78, 0.78)
)

moon_angle = 0
sun_angle = 0
time_step = 0.01

while True:
    rate(60)

    sun.rotate(
        angle=0.25 * time_step,
        axis=vector(0, 1, 0),
        origin=sun.pos
    )

    for item in planets:
        item["angle"] += item["orbit_speed"] * time_step

        x = item["distance"] * math.cos(item["angle"])
        z = item["distance"] * math.sin(item["angle"])
        new_position = vector(x, 0, z)

        item["body"].pos = new_position
        item["body"].rotate(
            angle=item["spin_speed"] * time_step,
            axis=vector(0, 1, 0),
            origin=new_position
        )
        item["label"].pos = new_position + vector(0, item["body"].radius + 0.25, 0)

        if item["ring"] is not None:
            item["ring"].pos = new_position

        if item["body"].radius == 0.58:
            moon_angle += 2.4 * time_step
            moon.pos = new_position + vector(
                0.95 * math.cos(moon_angle),
                0,
                0.95 * math.sin(moon_angle)
            )
