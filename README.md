# MatchZoo-Studio

> MatchZoo studio aims to facilitate the learning, practicing, and designing of neural text matching models with a user-friendly and interactive interface.



## System Overview

The architecture of the system is shown in the Figure. The system consists of two major components, namely the **MatchZoo library** and the **MatchZoo studio**. The library provides a number of text processing units, popular neural text matching models, as well as matching based evaluation and loss functions, for all stages (i.e, data preparation, model construction, and train and test.) of the machine learning based text matching tasks. Moreover, we have also provided the AutoML operators to support automatic data preparation, hyper-parameter tuning, and model selection in the library. The studio provides an interactive interface based on the MatchZoo library. There are three key functions, i.e., **model learning**, **model practicing**, and **model designing**, to ease the process of learning, using and creating neural text matching models. The studio contains a user-friendly GUI which is built on the Web server, and users can interact with the studio through Web browsers.

![MatchZoo Studio](./static/images/architecture.pdf)



## Model Learning

This panel shows the interface how users can learn different neural matching models in MatchZoo. Specifically, users can select a model in the navigation panel. Then, a systematical tutorial including theoretical descriptions and implementation details could be found under the description tab and guideline tab in the primary panel. As shown in Figure, the description tab contains a brief introduction of the model structure, parameters, performance of the selected neural text matching model DSSM. The guideline tab is an interactive Jupyter notebook. Under this tab, users can not only learn the original implementation code of DSSM, but also modify the code and experience with it.

![Model Learning](./static/images/model_learn.pdf)

## Model Practicing

This panel shows the interface how users can practice different neural matching models in MatchZoo. After selecting a model from the navigation panel, there are two stages to experience with the model, namely training stage and testing stage. In training stage, as is shown in Figure (1), users can interactively configure the model hyper-parameters and select/upload a dataset in the primary panel. Then, the secondary panel will display the training process, including the loss curve on the training set and performance curves on the validation set. In testing stage, as is shown in Figure (2), users can type in or select two texts as inputs in the primary panel. Then, the secondary panel will show the matching score as well as the layer weights. Note here the example DSSM model is a representation-focused model, so the learned representation vector of the two inputs are displayed for comparison and intuitive understanding. For interaction-focused model, one can visualize the interaction matrix for model explanation.

![Model Practice](./static/images/model_practice.pdf)

## Model Designing

This panel shows the interface how users can create a new neural matching models in MatchZoo. Specifically, users can click the  *Model Design* in the navigation panel. Then, a Jupyter Notebook will be present in the primary panel where users can directly implement his/her own neural matching model. At the same time, on the secondary panel, a detailed documentation about all the existing component APIs in MatchZoo would be displayed for users to search and access.

![Model Design](./static/images/new_model.pdf)

## Guideline

### Download source code from GitHub

```bash
git clone https://github.com/NTMC-Community/MatchZoo-Studio.git
cd MatchZoo-Studio
```

### Install requirements

```bash
pip install -r requirements.txt
```

###Configure Jupyter

Create a new file `jupyter_notebook_config.py` in the directory `~/.jupyter/` (Note: remember to delete it otherwise it will affect your usage of Jupyter) and copy the code below:

```python
c.NotebookApp.port = 8999
c.NotebookApp.token = ''
c.NotebookApp.open_browser = False
c.NotebookApp.disable_check_xsrf = True
c.NotebookApp.ip = '0.0.0.0'
c.NotebookApp.tornado_settings = {
    'headers': {    
        'Content-Security-Policy': "frame-ancestors * self"            
    }   
}
```

### Run server

In root directory of source code, run `app.py`:

```bash
python app.py
```

### Run Jupyter

```bash
cd ./matchzoo_temp_files/jupyters
jupyter notebook
```

### Open in browser

Enter `localhost:9773` or `127.0.0.1:9773` in your browser



## Front End

The Front end of MatchZoo Studio is based on [Vue.js](https://vuejs.org). Codes can be found in `./front_end`. Follow below instructions if you want to modify by yourself.

### Install Vue.js

First, you need to install `Vue.js`:

```bash
npm install vue
```

### Install dependencies

You can use `npm` to install dependencies:

```bash
cd ./front_end/
npm install
```

Or you can directly download `node_modules` from [Google Driver](https://drive.google.com/file/d/12THMke82xWGgZkEaW51mYgw9sDRHC-AP/view?usp=sharing), and unzip under `./front_end/node_modules/`

### Run as develop mode

```bash
npm run dev
```

### Build for production

After you have finished modifying, you need to build final files for production:

```bash
npm run build
```

Files will be saved in `./dist/` . Put these files in the right place:

```bash
./move.sh
```

