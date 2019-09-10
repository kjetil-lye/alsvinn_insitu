from xml_tools import read_config, get_in_xml
import sys
import os
import subprocess
from pathlib import Path
import git

if __name__ == '__main__':

    repo = git.Repo(search_parent_directories=True)


    import argparse

    parser = argparse.ArgumentParser(description="""
Submits the configuration file CSCS Daint. NOTE: Will run in folder of configuration file!
""")



    parser.add_argument('--alsuqcli_path', type=str, default=str(os.path.join(str(Path.home()), 'alsvinn/build/alsuqcli/alsuqcli')),
                        help="path to alsuqlci")
    parser.add_argument('--config', type=str, required=True,
                        help="Path to configuration file")
    parser.add_argument('--wait_time', type=int, default=24,
                        help='Wait time in hours')
    parser.add_argument('--multi_sample', type=int, default=1,
                        help='Number of processes to use in the sample direction')
    parser.add_argument('--dry_run', action='store_true',
                        help='Only do a dry run, no actual submission done')

    args = parser.parse_args()
    configuration_file = args.config

    configuration_path = os.path.abspath(os.path.dirname(configuration_file))

    config = read_config(configuration_file)
    name = get_in_xml(config, 'config.fvm.name').strip()
    resolution = int(get_in_xml(config, 'config.fvm.grid.dimension').split(" ")[0])

    number_of_nodes_per_direction = max(1, resolution // 256)

    total_number_of_nodes = number_of_nodes_per_direction**3*args.multi_sample


    submit_file=f"""#!/bin/bash -l
#SBATCH --job-name="{name}_{resolution}"
#SBATCH --time=24:00:00
#SBATCH --nodes={total_number_of_nodes}
#SBATCH --ntasks-per-core=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=1
#SBATCH --partition=normal
#SBATCH --constraint=gpu
#SBATCH --account=s913

export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
export CRAY_CUDA_MPS=1

srun {args.alsuqcli_path} --multi-sample {args.multi_sample} --multi-x {number_of_nodes_per_direction} --multi-y {number_of_nodes_per_direction} --multi-z {number_of_nodes_per_direction} {os.path.basename(configuration_file)}
"""

    if args.dry_run:
        print(submit_file)
    else:
        subprocess.run(['sbatch'], check = True, cwd = configuration_path,
                       input=submit_file, encoding='ascii')
