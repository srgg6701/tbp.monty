# as it turned out, import of sys.path.insert is not needed here
from tbp.monty.frameworks.models.object_model import GridObjectModel
import numpy as np
import matplotlib.pyplot as plt

model = GridObjectModel(
  "test_model",
  max_nodes=10, # the maximum number of nodes that will remain in the graph. The cells that contain the highest number of observations are the ones that remain.
  max_size=0.6, # in meters
  num_voxels_per_dim=50 # number of cells of the grid
)

def dataset ():
  locations = np.random.rand(10, 3) * 0.3 # must be not larger than max_size / 2
  features = {
    "fdots": np.random.rand(10, 3) * 0.3
  }
  model.build_model(
    locations,
    features
  )
  # print(f"Hello, task 1 here.\nLocations: {locations}\nFeatures: {features['fdots']}")
  # print(f"{locations.shape}, {features['fdots'].shape}")
  print("model.pos (coordinates): ")
  print(model.pos)
  print("\nmodel.x (features): ")
  print(model.x)
  print("\nmodel.feature_mapping: ")
  print(model.feature_mapping)
  fig = plt.figure()                          # canvas
  ax = fig.add_subplot(projection="3d")       # 3D-axes on the canvas
  ax.scatter(locations[:, 0], locations[:, 1], locations[:, 2])   # dots
  # ----------------------------------------
    # Borders of 50 cells on each axis considering location of the model's grid
  n = model._num_voxels_per_dim
  scale = model._location_scale_factor
  offset = model._location_offset

  edges = [
      (np.arange(n + 1) - 0.5 - offset[i]) / scale
      for i in range(3)
  ]
  x, y, z = edges

  # Drow lines on three surfaces of the cube
  for yi in y:
      ax.plot([x[0], x[-1]], [yi, yi], [z[0], z[0]],
              color="gray", linewidth=0.35)
  for zi in z:
      ax.plot([x[0], x[-1]], [y[0], y[0]], [zi, zi],
              color="gray", linewidth=0.35)
  for xi in x:
      ax.plot([xi, xi], [y[0], y[-1]], [z[0], z[0]],
              color="gray", linewidth=0.35)
  for zi in z:
      ax.plot([x[0], x[0]], [y[0], y[-1]], [zi, zi],
              color="gray", linewidth=0.35)
  for xi in x:
      ax.plot([xi, xi], [y[0], y[0]], [z[0], z[-1]],
              color="gray", linewidth=0.35)
  for yi in y:
      ax.plot([x[0], x[0]], [yi, yi], [z[0], z[-1]],
              color="gray", linewidth=0.35)
  # ----------------------------------------
  ax.set_xlabel("x"); ax.set_ylabel("y"); ax.set_zlabel("z")      # axes labels
  plt.show()
dataset()
