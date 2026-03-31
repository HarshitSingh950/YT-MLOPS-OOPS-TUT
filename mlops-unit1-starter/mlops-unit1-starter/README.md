# MLOPS-UNIT1 (Starter Project)

This starter project mirrors the folder structure used in your assignment.

## Project Structure
- `data/` - dataset files
- `src/` - source code
- `models/` - trained model files
- `requirements.txt` - project dependencies
- `.gitignore` - files/folders excluded from Git

## Environment Setup (Windows)
1. Create the virtual environment:
   `python -m venv mlops`
2. Activate it:
   `.\mlops\Scripts\activate`
3. Install dependencies:
   `pip install -r requirements.txt`

## Run the Project
1. Dataset statistics and correlation matrix:
   `python src\preprocess.py`
2. Train and save model:
   `python src\train_model.py`

After running `train_model.py`, the model will be saved to `models/iris_model.pkl`.
