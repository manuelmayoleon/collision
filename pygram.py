from PyGran import simulation, params
PyGran.configure(
    path='/home/user/.local/lib/custom_libliggghts.so',
    version='3.8.0',
    src='/path/to/LIGGGHTS-3.8.0/src'
)
# Create a DEM object for simulation
sim = simulation.DEM(
    boundary=("f", "f", "f"),
    box=(-1e-3, 1e-3, -1e-3, 1e-3, 0, 4e-3),
    species=(
        {
            "material": params.stearicAcid, 
            "radius": ("constant", 5e-5)},
        ),
    gravity=(9.81, 0, 0, -1),
    mesh={
        "hopper": { # arbitrary mesh name
            "file": "silo.stl", # mesh filename
            "mtype": "mesh/surface", # mesh type
            "material": params.steel, # mesh material
        }
    },
)

# Insert 1000 particles for species 1 (stearic acid)
insert = sim.insert(species=1, value=1000)

# Evolve the system in time
sim.run(nsteps=1e6, dt=1e-7)
