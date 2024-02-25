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

    def prompt_hyperparameters(self) -> None:
        # prompt the user with hyperparameter choices
        print(f'Select model size (n, s, m, l, x): ')
        self.model_size = input()

        print(f'Select epochs amount: ')
        self.epochs = int(input())

        print(f'Select batch size (-1 for auto): ')
        self.batch = int(input())

        print(f'Specify classes (likely 3): ')
        self.classes[0] = int(input())

        print(f'Select optimizer (SGD, Adam, AdamW, NAdam, RAdam, RMSProp): ')
        self.optimizer = input()

        print(f'Select cosine learning rate status: ')
        while True:
            temp_var_coslr:str = ''
            temp_var_coslr = input()
            if temp_var_coslr == 'False':
                self.cos_lr_stat = False
                break
            elif temp_var_coslr == 'True':
                self.cos_lr_stat = True
                break
            else:
                print('Invalid input, please enter True or False.')

    def train_init(self) -> None:
        # Load a model
        model = YOLO(f'yolov8{self.model_size}.pt')  # load a pretrained model (recommended for training)
        model.to(device_name)

        # Train the model
        results = model.train(data='hpc/data.yaml', epochs=self.epochs, batch=self.batch, classes=self.classes, 
                              optimizer=self.optimizer, cos_lr=self.cos_lr_stat)
            

if __name__ == "__main__":
    test_instance = TrainModel()
    test_instance.prompt_hyperparameters()
    test_instance.train_init()
