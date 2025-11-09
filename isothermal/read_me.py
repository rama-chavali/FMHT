from paraview.simple import *
reader = OpenDataFile("401x41.cas.h5")
reader.UpdatePipeline()  # Forces reading
