"""
train_model.py
~~~~~~~~~~~~

A module to train YOLO models on UARK hpc. Functionality includes (as far as I've thought)....
TO DO: create a tune_hyperparamter script that outputs


"""

# Setting environmental variable and import statements
import os
import torch
from ultralytics import YOLO
from typing import List, Any
import pandas as pd

# Specifying cuda GPU memory allocation. Required in google colab to deal with memory overrun, using as safeguard for HPC
os.environ['PYTORCH_CUDA_ALLOC_CONF'] = 'max_split_size_mb:256'

# Intializing GPU use if available for training.
if torch.cuda.is_available():
    device_name = torch.device("cuda")
else:
    device_name = torch.device('cpu')
print(f"Using {device_name} for training.")

# Create function that trains model
class TrainModel:

    def __init__(self) -> None:
        # initialize hyperparameters
        self.model_size:str = ''
        self.epochs:int = 100
        self.batch:int = -1
        self.classes:List[int] = [3]
        self.optimizer:str = ''
        self.cos_lr_stat:bool = False
        self.project:str = ''
        self.name:str = ''

    def prompt_hyperparameters(self) -> None:
        # read in config as pandas dataframe
        config = pd.read_csv('hpc/config.csv')

        # prompt the user with hyperparameter choices
        self.model_size = config.iloc[0, 0].strip()
        print(f'Selected model size (n, s, m, l, x): {self.model_size}')

        self.epochs = int(config.iloc[0, 1])
        print(f'Selected epochs amount: {self.epochs}')

        self.batch = int(config.iloc[0, 2])
        print(f'Selected batch size (-1 for auto): {self.batch}')

        self.classes[0] = int(config.iloc[0, 3])
        print(f'Specified classes (likely 3): {self.classes[0]}')

        self.optimizer = config.iloc[0, 4].strip()
        print(f'Selected optimizer (SGD, Adam, AdamW, NAdam, RAdam, RMSProp): {self.optimizer}')

        self.cos_lr_stat = bool(config.iloc[0, 5].strip())
        print(f'Select cosine learning rate status: {self.cos_lr_stat}')

        self.project = config.iloc[0, 6].strip()
        self.name = config.iloc[0, 7].strip()
        print(f'Results will be saved in {self.project}/{self.name}')

    def train_init(self) -> None:
        # Load a model
        model = YOLO(f'yolov8{self.model_size}.pt')  # load a pretrained model (recommended for training)
        model.to(device_name)

        # Train the model
        results = model.train(data='hpc/data.yaml', epochs=self.epochs, batch=self.batch, classes=self.classes, 
                              optimizer=self.optimizer, cos_lr=self.cos_lr_stat, project=self.project, name=self.name)
            
if __name__ == "__main__":
    test_instance = TrainModel()
    test_instance.prompt_hyperparameters()
    test_instance.train_init()
