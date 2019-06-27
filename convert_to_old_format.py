#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Converts the paralle netcdf file to a classic netcdf file hopefully readable by paraview

"""

import netCDF4
import numpy as np
import argparse

if __name__ == '__main__':
    
    
    parser = argparse.ArgumentParser(description="""
Converts the file to the old netcdf file format
            """)

    parser.add_argument('--input_file', type=str, required=True,
                        help='Input file')

    parser.add_argument('--output_file', type=str, required=True,
                        help='Output file')


    args = parser.parse_args()
    
    xdim = None
    ydim = None
    zdim = None

    with netCDF4.Dataset(args.input_file) as f:
        with netCDF4.Dataset(args.output_file, 'w', format='NETCDF4_CLASSIC') as outf:
            for v in f.variables.keys():
                print(f"Converting {v}")
                if v == 'time':
                    tdim = outf.createDimension("t", 1)
                    t = outf.createVariable("time", np.float64, ("t",))
                    t[0] = f.variables[v][0]
                else:
                    d = f.variables[v][:,:,:]
                    if xdim is None:
                        xdim = outf.createDimension("x", d.shape[0])
                        ydim = outf.createDimension("y", d.shape[1])
                        zdim = outf.createDimension("z", d.shape[2])
                        
                    newvar = outf.createVariable(v, d.dtype, ("x", "y", "z"))
                    newvar[:,:,:] = d[:,:,:]
            # copy over the attributes (this is not really needed, but nice for tracing what was done)
            for attribute_name in f.ncattrs():
                outf.setncattr(attribute_name, f.getncattr(attribute_name))
                        
            outf.setncattr("IMPORTANT_NODE", """
This file was converted with the script "convert_to_old_format.py" to be compatiable with paraview.
            """)

