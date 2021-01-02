#%%
from snappy import jpy
from snappy import ProductIO

s1_identifier = "S1A_IW_GRDH_1SDV_20201228T170552_20201228T170617_035889_0433FB_D8C7"

reader = ProductIO.getProductReader("SENTINEL-1")
product = reader.readProductNodes(f"/data/{s1_identifier}.SAFE/manifest.safe", None)

print("Bands:   %s" % (list(product.getBandNames())))
# %%
