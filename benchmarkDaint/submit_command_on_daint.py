import sys
import os
import subprocess
from pathlib import Path


if __name__ == '__main__':

    import argparse

    parser = argparse.ArgumentParser(description="""
Submits the configuration file CSCS Daint. NOTE: Will run in folder of configuration file!
""")

    parser.add_argument('-w', '--working_directory', type=str,
                        default=os.getcwd(),
                        help='Working directory')

    parser.add_argument('--command', type=str, required=True,
                        help="command to run")
    parser.add_argument('--wait_time', type=int, default=24,
                        help='Wait time in hours')
    parser.add_argument('--nodes', type=int, default=1,
                        help='number of node to use')
    parser.add_argument('--tasks_per_node', type=int, default=1,
                        help='number of tasks per node')

    parser.add_argument('--cpus_per_task', type=int, default=1,
                        help='number of cpus per task')

    parser.add_argument('--name', type=str, required=True,
                        help="name of job")
    parser.add_argument('--dry_run', action='store_true',
                        help='Only do a dry run, no actual submission done')

    args = parser.parse_args()
    submit_file=f"""#!/bin/bash -l
#SBATCH --job-name="{args.name}"
#SBATCH --time={args.wait_time}:00:00
#SBATCH --nodes={args.nodes}
#SBATCH --ntasks-per-core=1
#SBATCH --ntasks-per-node={args.tasks_per_node}
#SBATCH --cpus-per-task={args.cpus_per_task}
#SBATCH --partition=normal
#SBATCH --constraint=gpu


export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK


srun {args.command}
"""

    if args.dry_run:
        print(submit_file)
    else:
        subprocess.run(['sbatch'], check = True, cwd = args.working_directory,
                       input=submit_file, encoding='ascii')
