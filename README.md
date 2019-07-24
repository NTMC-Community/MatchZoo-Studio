# MatchZoo-Studio

> MatchZoo studio aims to facilitate the learning, practicing, and designing of neural text matching models with a user-friendly and interactive interface.



# System Overview

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

``` bash
# install dependencies
npm install

# serve with hot reload at localhost:8080
npm run dev

# build for production with minification
npm run build

# build for production and view the bundle analyzer report
npm run build --report

# run unit tests
npm run unit

# run e2e tests
npm run e2e

# run all tests
npm test
```
