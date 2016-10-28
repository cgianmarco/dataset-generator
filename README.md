# dataset-generator
A set of tools to generate a dataset for machine learning quickly

## Installing

```
git clone https://github.com/cgianmarco/dataset-generator.git

cd dataset-generator

python setup.py install
```

## Usage

```
from datasetGenerator.filters import *

trasformer = verticalFlipTrasformer()

processed_images = test(images, trasformer)