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
  ax.set_xlabel("x"); ax.set_ylabel("y"); ax.set_zlabel("z")      # axes labels
  plt.show()
dataset()
