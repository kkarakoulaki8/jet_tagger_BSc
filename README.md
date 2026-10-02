# BSc Project on Explainable AI (XAI)

This repository contains the code to help you get started with training a jet tagger.

## Repository Structure

* `train_jet_tagger.ipynb` — Jupyter notebook containing the training and evaluation workflow for the jet tagger.
* `pixi.toml` — contains all the packages you need to run the code and will be used by Pixi (a package management tool) to install all of them in one place.
* `plot/style.py` — Helper functions used in the notebook for consistent plotting and figure styling.
* `training_data_CMS` — Symbolic link to the training dataset stored on DICE.

## Accessing DICE

The repository and training data are intended to be used on **DICE**.

Instructions for connecting to DICE using VS Code can be found in the [Visual Studio Code Remote SSH documentation](https://code.visualstudio.com/docs/remote/ssh).

You will need to have **Pixi installed on DICE** in order to create the required environment and run the notebook. https://pixi.prefix.dev/latest/

## Cloning the respiratory on DICE
After connecting on DICE using VS code. Go to your software directory where you can keep all your code:

```bash
cd /software/<your-username>/
```
and then clone this repository using this command:

```bash
git clone https://github.com/kkarakoulaki8/jet_tagger_BSc.git
```

## Training Data

The training data are not stored directly in this GitHub repository.

The `training_data_CMS` directory is a symbolic link to the dataset stored on DICE:

```text
/dice/users/bm24156/training_data_latest/
```

The model classifies each jet into **8 different classes**:

- Muon
- Electron
- Tau+
- Tau-
- Light-flavour jet
- b jet
- Gluon jet
- Charm jet

Each jet is represented using its **16 highest-pT candidates (constituents)**. For each candidate, **20 variables** describing its properties are used as input to the model.

The input to the model therefore has the shape: (16, 20)



## Setting Up the Environment

Install pixi on dice:
```bash
curl -fsSL https://pixi.sh/install.sh | sh
```

After cloning the repository on DICE, navigate to the repository directory:

```bash
cd jet_tagger_BSc
```
Create the environment using the provided environment file:

```bash
pixi install 

```
Then run this command so that your terminal recognises the changes:

```bash
source ~/.bashrc
```
To be able to use the environment in a jupyter notebook run the following commands:

```bash
pixi run python -m ipykernel install --user     --name jet-tagger-pixi     --display-name "Jet Tagger (Pixi)"
```
```bash
mkdir -p .vscode
```
```bash
nano .vscode/settings.json
```
Copy and paste this into settings.json:
```
{
    "python.defaultInterpreterPath": "/software/<your_username>/jet_tagger_BSc/.pixi/envs/default/bin/python"
}
```
To exit press ctrl+X and to save press Y

## Running the Jet Tagger

Once the environment has been created and activated:

1. Open `train_jet_tagger.ipynb` in VS Code:
    * Go to File
    * Open Folder 
    * Type /users/<your_username>/ (which is where you cloned before the git repo)
2. Select the pixi environment as the Jupyter kernel.
3. Run the notebook cells.

The notebook contains the complete workflow for:

* Training the jet tagger.
* Saving the trained model.
* Testing and evaluating the model.
* Producing and saving plots.


This github repo is based on https://github.com/CMS-L1T-Jet-Tagging/TrainTagger