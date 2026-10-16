# as it turned out, import of sys.path.insert is not needed here
from tbp.monty.frameworks.models.object_model import GridObjectModel
import numpy as np

model = GridObjectModel(
  "test_model",
  max_nodes=10, # the maximum number of nodes that will remain in the graph. The cells that contain the highest number of observations are the ones that remain.
  max_size=0.5, # in meters
  num_voxels_per_dim=50 # number of cells of the grid
)

def dataset ():
  locations = np.random.rand(10, 3) * 0.3
  features = {
    "fdots": np.random.rand(10, 3) * 0.3
  }
  model.build_model(
    locations,
    features
  )
  print(f"Hello, task 1 here.\nLocations: {locations}\nFeatures: {features['fdots']}")
  print(f"{locations.shape}, {features['fdots'].shape}")

dataset()
