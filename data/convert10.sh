#!/bin/bash
for i in {1..9}
do
  python3 ../convert_to_old_format.py --input_file kh_mean_$i.nc --output_file mean$i.nc
echo "$i"
done
