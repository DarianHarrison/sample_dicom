import matplotlib.pyplot as plt
import pydicom
filename = ("testfiles/CT_small.dcm")
ds = pydicom.dcmread(filename)
plt.imshow(ds.pixel_array, cmap=plt.cm.bone) 
plt.show()