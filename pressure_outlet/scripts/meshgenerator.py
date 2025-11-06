import gmsh

def generate_mesh(name, element_size):
    gmsh.initialize()
    gmsh.model.add(name)

    # Geometry dimensions
    length = 10.0
    height = 0.1

    # Create points
    p1 = gmsh.model.geo.addPoint(0, -height, 0, element_size)
    p2 = gmsh.model.geo.addPoint(0, height, 0, element_size)
    p3 = gmsh.model.geo.addPoint(length, height, 0, element_size)
    p4 = gmsh.model.geo.addPoint(length, -height, 0, element_size)

    # Create lines (counter-clockwise)
    l1 = gmsh.model.geo.addLine(p1, p2)  # Inlet
    l2 = gmsh.model.geo.addLine(p2, p3)  # Top wall
    l3 = gmsh.model.geo.addLine(p3, p4)  # Outlet
    l4 = gmsh.model.geo.addLine(p4, p1)  # Bottom wall

    # Curve loop and surface
    cloop = gmsh.model.geo.addCurveLoop([l1, l2, l3, l4])
    surface = gmsh.model.geo.addPlaneSurface([cloop])

    # Physical groups (required for Fluent)
    gmsh.model.geo.synchronize()
    gmsh.model.addPhysicalGroup(1, [l1], tag=1)
    gmsh.model.setPhysicalName(1, 1, "inlet")
    gmsh.model.addPhysicalGroup(1, [l2], tag=2)
    gmsh.model.setPhysicalName(1, 2, "top_wall")
    gmsh.model.addPhysicalGroup(1, [l3], tag=3)
    gmsh.model.setPhysicalName(1, 3, "outlet")
    gmsh.model.addPhysicalGroup(1, [l4], tag=4)
    gmsh.model.setPhysicalName(1, 4, "bottom_wall")
    gmsh.model.addPhysicalGroup(2, [surface], tag=5)
    gmsh.model.setPhysicalName(2, 5, "fluid")

    # Generate mesh
    gmsh.model.mesh.generate(2)

    # Write in MSH v2 format (required for Fluent)
    gmsh.write(f"{name}.msh")

    print(f"Mesh written to: {name}.msh (Gmsh MSH2 format)")
    gmsh.finalize()


# Generate coarse, moderate, fine meshes
generate_mesh("channel_coarse", 0.2)
generate_mesh("channel_moderate", 0.05)
generate_mesh("channel_fine", 0.01)

