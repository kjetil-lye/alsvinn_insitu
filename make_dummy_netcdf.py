import netCDF4
import sys
import numpy as np

xdim = None
ydim = None
with netCDF4.Dataset(sys.argv[1]) as f:
    with netCDF4.Dataset("newfile.nc", "w", format="NETCDF4_CLASSIC") as outf:
        for v in f.variables.keys():
            if v=="time":
                tdim = outf.createDimension("tdim", 1)
                tvar = outf.createVariable("time", np.float64, ("tdim",))
                tvar[0] = f.variables[v][0]
            else:
                d = f.variables[v][:,:,:]
                N = d.shape[0]
                if xdim is None:
                    xdim = outf.createDimension("x", d.shape[0])

                    ydim = outf.createDimension("y", d.shape[1])

                    ydim = outf.createDimension("z", d.shape[2])

                var = outf.createVariable(v, np.float64, ("x", "y", "z"))

                var[:,:,:] = d
