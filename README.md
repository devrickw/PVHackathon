# PVHackathon Jupyter Notebook Solution

## Download Miniconda and choose your OS

https://docs.anaconda.com/free/miniconda/index.html


## Open the Miniconda Prompt by typing in Miniconda in the Search bar
![plot](https://github.com/devrickw/PVHackathon/blob/3a3bb74a3e5f2c6220a358dc38ba9bc4a04ae6f5/minicondasnap.PNG)

## Create Folder

Using the terminal , navigate to the documents folder, and create a new folder called ChevronWorkshop
```
cd Documents
mkdir ChevronWorkshop
cd ChevronWorkshop

```

## Make a python environment
Use the conda create command to make environment (replace 'myenv' with what you want to call your environment)
```
conda create -y --name myenv 
```
## Activate Environment
Windows
```
activate [your environment name]
```
Mac
```
source activate [your environment name]
```

## Install Jupyter Notebook

```
conda install -y jupyter
```
