"""
train_model.py
~~~~~~~~~~~~

A module to train YOLO models on UARK hpc. Functionality includes (as far as I've thought)....
TO DO: create a tune_hyperparamter script that outputs


"""
# %%
# Setting environmental variable and import statements
import os
import torch
from ultralytics import YOLO
import typing

# Specifying cuda GPU memory allocation. Required in google colab to deal with memory overrun, using as safeguard for HPC
os.environ['PYTORCH_CUDA_ALLOC_CONF'] = 'max_split_size_mb:256'

# Intializing GPU use if available for training.
if torch.cuda.is_available():
    device_name = torch.device("cuda")
else:
    device_name = torch.device('cpu')
print(f"Using {device_name} for training.")

# %%
# Hyperparameter selection 
def choose_hyperparameters() -> None:
    pass