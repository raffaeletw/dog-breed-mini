# 🐶 Dog Breed Mini — 3-Class CNN (Streamlit + Keras)

A small end-to-end project:
- Train a CNN on a subset of the **Dog Breed Identification** dataset (Kaggle).
- Build a simple **Streamlit** app to predict among 3 breeds:
  - `scottish_deerhound`
  - `maltese_dog`
  - `bernese_mountain_dog`

<div align="center">
  <img src="assets/screenshot_app.png" alt="App screenshot" width="70%">
</div>

## ✨ Highlights
- Colab-friendly notebook to download data with Kaggle API.
- Clean Streamlit UI for single-image inference.

## 🚀 Quickstart

### 1) Environment
```bash
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt

### 2) Get the model 

Option A: download dog_breed.h5.
Option B: train it yourself (see notebook below).

### 3) Run the app
```bash
streamlit run app/main_app.py




