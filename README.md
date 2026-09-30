# BSc Project on Explainable AI (XAI)

This repository contains the code to help you get started with training a jet tagger.

## Repository Structure

* `train_jet_tagger.ipynb` — Jupyter notebook containing the training and evaluation workflow for the jet tagger.
* `environment.yml` — Conda environment configuration containing the required dependencies.
* `plot/style.py` — Helper functions used in the notebook for consistent plotting and figure styling.
* `training_data_CMS` — Symbolic link to the training dataset stored on DICE.

## Accessing DICE

The repository and training data are intended to be used on **DICE**.

Instructions for connecting to DICE using VS Code can be found in the [Visual Studio Code Remote SSH documentation](https://code.visualstudio.com/docs/remote/ssh).

You will need to have **Conda installed on DICE** in order to create the required environment and run the notebook.

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

After cloning the repository on DICE, navigate to the repository directory:

```bash
cd jet_tagger_BSc
```

Create the Conda environment using the provided environment file:

```bash
conda env create -f environment.yml
```

Activate the newly created environment:

```bash
conda activate tagger
```

The required dependencies will be installed automatically from `environment.yml`.

## Running the Jet Tagger

Once the environment has been created and activated:

1. Open `train_jet_tagger.ipynb` in VS Code.
2. Select the newly created Conda environment as the Python kernel.
3. Run the notebook cells.

The notebook contains the complete workflow for:

* Training the jet tagger.
* Saving the trained model.
* Testing and evaluating the model.
* Producing and saving plots.

