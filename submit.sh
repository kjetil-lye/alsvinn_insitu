#!/bin/bash -l
#BATCH --job-name="test multiblock viz"
#SBATCH --mail-type=ALL
#SBATCH --mail-user=hohlr@ethz.ch
#SBATCH --time=1:00:00
#SBATCH --nodes=40
#SBATCH --ntasks-per-core=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=1
#SBATCH --partition=normal
#SBATCH --constraint=gpu
#SBATCH --hint=nomultithread

export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK

srun $HOME/alsvinn/build/alsuqcli/alsuqcli --multi-x 2 --multi-y 2 --multi-sample 10 $HOME/alsvinn_insitu/example/catalyst_multiblock2d_mx4_my4_s10.xml

