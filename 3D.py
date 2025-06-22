import open3d as o3d

# Load the mesh
mesh = o3d.io.read_triangle_mesh("output_mesh_0003.ply")

# Visualize the mesh
o3d.visualization.draw_geometries([mesh])
