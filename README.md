![Logo](https://github.com/Logisx/AI_Senior/blob/main/assets/logo-color_cropped.png?raw=true)

# 📋 Table of Contents 

- [📋 Table of Contents](#-table-of-contents)
- [:rocket: Your personal Senior Assistant](#rocket-your-personal-senior-assistant)
  - [:toolbox: Tech Stack](#toolbox-tech-stack)
  - [:file\_folder: Project structure](#file_folder-project-structure)
  - [:computer: Run Locally](#computer-run-locally)
- [:world\_map: Roadmap](#world_map-roadmap)
- [⚖️ License](#️-license)
- [🔗 Links](#-links)
- [📚 References \& Citations](#-references--citations)

# :rocket: Your personal Senior Assistant

Introducing AI Senior! <br> Your friendly AI companion offering experienced guidance for all your tech queries. From coding hiccups to tech dilemmas, AI Senior has your back. Simplify your tech journey with AI Senior by your side! 

*Work is in progress...* 🏗️

![Python](https://img.shields.io/badge/Python-3.10-blue)
![PyTorch](https://img.shields.io/badge/PyTorch-2.1.1-red)
![JupyterLab](https://img.shields.io/badge/Jupyter%20Lab-Research-FF9900)
![Bytewax](https://img.shields.io/badge/Bytewax-Dataflow-FF9900)
![AWS](https://img.shields.io/badge/AWS-Cloud-orange)
![Qdrant](https://img.shields.io/badge/Qdrant-VectorDB-purple) 
![LLMs](https://img.shields.io/badge/LLMs-Model-663399)
![HuggingFace](https://img.shields.io/badge/HuggingFace-NLP-5b68d6)
![Comet](https://img.shields.io/badge/Comet-Tracking-ff6600)
![Beam](https://img.shields.io/badge/Beam-Training-blue)
![LangChain](https://img.shields.io/badge/LangChain-ChatBot-ee4d5f)
![REST](https://img.shields.io/badge/REST-API-5b68d6)
![Gradio](https://img.shields.io/badge/Gradio-UI-009688) 
![Docker](https://img.shields.io/badge/Docker-Containers-blue)
![CI/CD](https://img.shields.io/badge/CI%2FCD-Workflow-4D7A97)
![Terraform](https://img.shields.io/badge/Terraform-Infrastructure-623CE4)



<p align="left">
  <img src="https://github.com/Logisx/AI_Senior/blob/main/assets/architecture.png?raw=true" alt="Architecture" width="800" height="800">
</p>

## :toolbox: Tech Stack

- **ML**: Python, PyTorch, JupyterLab
- **Data Services**: Bytewax, AWS, Qdrant
- **Training**: LLMs, HuggingFace, Comet, Beam
- **ChatBot & UI**: LangChain, REST-API, Gradio
- **Deployment**: Docker, Terraform


## :file_folder: Project structure
🚧 **Work in progress** 🚧
```
|   .beamignore
|   .env
|   .gitignore                  <- Specify files to be ignored by git
|   LICENSE                     <- Project license
|   Makefile                    <- Makefile with commands like `make data` or `make train`
|   README.md                   <- The top-level README for developers using this project.
|   requirements.txt            <- The requirements file for reproducing the analysis environment, e.g. generated with `pip freeze > requirements.txt`
|   setup.py                    <- Make this project pip installable with `pip install -e`
|   test_environment.py
|   tox.ini
|   .venv
|                   
+---assets                       <- Store public assets for readme file
|   |   architecture.png
|   \---logo-color_cropped.png
|               
+---config                       <- Stores pipelines' configuration files
|       data-params.yaml
|       inference-params.yaml
|       model-params.yaml
|       paths.py
|       
+---data
|   |   .gitkeep
|   |   
|   +---external                 <- Data from third party sources.
|   |       .gitkeep
|   |       
|   +---interim                  <- Intermediate data that has been transformed.
|   |       .gitkeep
|   |       
|   +---processed                <- The final, canonical data sets for modeling.
|   |   |   .gitkeep
|   |   |   documents_newsapi_news.json
|   |   |   
|   |   \---fine-tuning
|   |           testing_data.json
|   |           training_data.json
|   |           
|   \---raw                      <- The original, immutable data dump.
|           .gitkeep
|           
+---docs
|       commands.rst
|       conf.py
|       getting-started.rst
|       index.rst
|       make.bat
|       Makefile
|       
+---logs
|       .gitkeep
|       running_logs.log
|       
+---models                      <- Trained and serialized models, model predictions, or model summaries
|   |   .gitkeep
|   |   
|   \---cache
|           .gitkeep
|           
+---notebooks                   <- Jupyter notebooks for research.
|       .gitkeep
|       research-01-data-api-usage.ipynb
|       
+---references
|       .gitkeep
|       
+---reports
|   |   .gitkeep
|   |   
|   \---figures
|           .gitkeep
|           
+---src                          <- Source code for use in this project.
|   |   __init__.py             <- Makes src a Python module
|   |   
|   +---data                    <- Scripts to download or generate data
|   |   |   .gitkeep
|   |   |   generate_training_data.py
|   |   |   run_data_pipeline.py
|   |   |   __init__.py
|   |   |   
|   |   +---modules
|   |   |       data_preprocessor.py
|   |   |       newsapi_data_loader.py
|   |   |       qdrant_data_uploader.py
|   |   |       training_data_generation.py
|   |   |       __init__.py
|   |   |       
|   |   \---pipeline
|   |           data_download.py
|   |           data_preprocessing.py
|   |           data_upload.py
|   |           
|   +---models                  <- Scripts to train models and then use trained models to make predictions
|   |   |   .gitkeep
|   |   |   requirements.txt
|   |   |   run_inference_pipeline.py
|   |   |   run_training_pipeline.py
|   |   |   steps.txt
|   |   |   train_run.py
|   |   |   __init__.py
|   |   |   
|   |   \---training_pipeline
|   |       |   constants.py
|   |       |   metrics.py
|   |       |   models.py
|   |       |   __init__.py
|   |       |   
|   |       +---api
|   |       |       inference.py
|   |       |       training.py
|   |       |       __init__.py
|   |       |       
|   |       +---data
|   |       |       qa.py
|   |       |       __init__.py
|   |       |       
|   |       \---prompt_templates
|   |               prompter.py
|   |               
|   \---utils                  <- Utility functions and classes
|       |   computation_management.py
|       |   configuration_management.py
|       |   file_management.py
|       |   __init__.py
|       |   
|       \---logging
|               __init__.py
|               
\---src.egg-info
```
## :computer: Run Locally

1. Clone the project

```bash
  git clone https://github.com/Logisx/AI_Senior.git
```

2. Go to the project directory

```bash
  cd my-project
```

3. Install dependencies

```bash
  pip install -r requirements.txt
```
🚧 **Work in progress** 🚧

# :world_map: Roadmap

🚧 **Work in progress** 🚧


# ⚖️ License
[![MIT License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/Logisx/AI_Senior/blob/main/LICENSE)


# 🔗 Links
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/aleksandrshishkov)

# 📚 References & Citations
Inspired by awesome [Hands-on LLMs Course](https://github.com/iusztinpaul/hands-on-llms) made by <a href="https://github.com/iusztinpaul">Paul Iusztin</a>, <a href="https://github.com/Paulescu">Pau Labarta Bajo</a> and <a href="https://github.com/Joywalker">Alexandru Razvant</a>

Check it out!
