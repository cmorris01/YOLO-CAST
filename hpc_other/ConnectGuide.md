# Instructions for connecting to a GPU Compute node in UARK HPC Resource

Before connecting to any compute resources, your local system must be connected to the University directly or through 
the university VPN. Connections will not be allowed otherwise.

Once on the University's network, connect to the HPC Login Node with an ssh call in the local terminal.
The call will take a username and the server address of the on-campus HPC. Should look like this line:

ssh <user_name>@hpc-portal2.hpc.uark.edu

Secure copy the files from your local machine to the UARK HPC server. Be sure to include the SLURM .bash file to submit a job to the pinnacle gpu cluster queue.

scp [file_name]  <user_name>@hpc-portal2.hpc.uark.edu:/created/remote/directory

Submit computationally intensive jobs to the GPU Queue on the Pinnacle Clusters. All 19 GPU nodes host 32 processing cores. All GPU nodes are referenced by allowed job runtime, reserved for 6 or 72 hour jobs. Queue jobs for these nodes in a SLURM script with gpu06 and gpu72, respectively.

Run a bash script on the login node with the SLURM script .sh file:

#!/bin/bash
#SBATCH --job-name=yolov8
#SBATCH --output=yolov8_out.slurm
#SBATCH --nodes=2
#SBATCH --tasks-per-node=32
$SBATCH --time=03:00:00
#SBATCH --partition gpu06
module purge
module load intel/14.0.3 mkl/14.0.3 fftw/3.3.6 impi/5.1.2
cd $SLURM_SUBMIT_DIR
cp *.in *UPF /scratch/$SLURM_JOB_ID
cd /scratch/$SLURM_JOB_ID
mpirun -ppn 16 -hostfile /scratch/${SLURM_JOB_ID}/machinefile_${SLURM_JOB_ID} -genv OMP_NUM_THREADS 2 \ /share/apps/espresso/qe-6.1-intel-mkl-impi/bin/pw.x -npools 1 <ausurf.in
mv ausurf.log *mix* *wfc* *igk* $SLURM_SUBMIT_DIR/

To retrieve results, use another scp commands to access the output file from the upload folder:

scp <user_name>@hpc-portal2.hpc.uark.edu:/path/to_file/on_HPC/file_name 

For inquiries about software installations, assistance with job scripts, assistance trouble shooting a failed run, etc…please provide any of the following information that would apply to the issue in an email to HPC-SUPPORT@listserv.uark.edu

Location of job script on system
A copy of the .out or .err file from SLURM
Any additional bits of information that might help
Specific link to software you wish to have installed