#!/bin/bash

# Path to your Python script on your Mac
PYTHON_SCRIPT_PATH="/Users/coymorris/Desktop/YOLO-CAST/train_model.py"

# Name of your Singularity image file (assuming it's already inside the Lima VM)
SINGULARITY_IMAGE_NAME="/Users/coymorris/Desktop/YOLO-CAST/hpc/yolo_training.sif"

# Optional: bind path for singularity, adjust if your script reads from or writes to other directories
# Format: "/path/on/mac:/path/in/lima"
BIND_PATH="/Users/coymorris/Desktop/YOLO-CAST:/mnt"

# Start the default Lima VM
limactl start singularity-ce

# Execute the Python script inside the Singularity container within the Lima VM
# This command uses limactl shell to send a command to the Lima VM
limactl shell singularity-ce -- <<EOF
singularity exec --bind $BIND_PATH $SINGULARITY_IMAGE_NAME python /mnt/$(basename $PYTHON_SCRIPT_PATH)
EOF
