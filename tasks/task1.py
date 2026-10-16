# as it turned out, import of sys.path.insert is not needed here
# from tbp.monty.frameworks.models.object_model import GridObjectModel
import numpy as np

def dataset ():
  locations = np.zeros((10, 3), dtype=int)
  features = {
    "place": np.zeros((10, 3), dtype=int)
  }
  print(f"Hello, task 1 here.\nLocations: {locations}\nFeatures: {features['place']}")
  print(f"{locations.shape}, {features['place'].shape}") # (2,)

dataset()
