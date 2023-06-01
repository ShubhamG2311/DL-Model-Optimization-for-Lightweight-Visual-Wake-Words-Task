# DL Model Optimization for Lightweight Visual Wake Words Task

- Author: Shubham Ghelani (B20EE019), Mruganshi Gohel (B20CS014) 

### How to run code:

- Download the .ipynb file.
- Login into google colab (or Jupyter Notebook if you have it)

(Preferred to run on google colab)

1. **If you are using google colab**
- Import .ipynb file into colab (file→open)
- Firstly download the dataset (submitted as a zip on GC)
- Import the dataset(zip) on the drive
- Import dataset zip file by changing the cell-3 code in the .ipynb file

```python
!unzip zip-location-on-drive
```

and run all cells

1. if **using a Jupyter Notebook**
- Just import the dataset from your PC no need to import it on the drive.
- Run all cells

### Required Libraries to Download

1. Numpy

```python
pip install numpy
```

1. pandas

```python
pip install pandas
```

1. matplotlib (for visualization)

```python
pip install matplotlib
```

1. tenserflow

```python
pip install tenserflow
```

1. PIL (for image)

```python
pip install pillow
```

### Problem Description

The Lightweight Visual Wake Words (LVWW) task involves the development of an artificial intelligence (AI) model that can automatically identify whether a person is present or not in the camera input of mobile phones or microcontrollers. This is a useful application for a range of use cases such as security systems, automated attendance systems, and monitoring applications.

The LVWW task is particularly challenging as the model needs to be optimized for deployment on resource-constrained devices with limited computing power and memory. Therefore, the model must be lightweight and efficient, while maintaining high accuracy in detecting people.

### Approach

In this project, we need to build a model which can automatically detect whether a person is present or not in given image. The input image would be mostly from camera of the phone. Based upon the features of the image and its configuration, we need deep learning models to detect whether the person is present or not in the image. The plan of implementation was as follows:

- Stabilizing and reducing the dataset
- Preprocessing the dataset
- Building the Model, Training and Testing the Model
- Model Robustness Check
- Analyzing the Neural Network Design by changing the size of the neural network
- Observing and concluding the final results

### Dataset Description

The dataset is derived from [COCO2017](https://cocodataset.org/#download) and reduced to ~150MB using the Python script, written in report and submitted along with codes.

![image](https://drive.google.com/uc?export=view&id=1q8_JyLFhW_BTxptTmIQAAMHUW4bNdcwU)

![image](https://drive.google.com/uc?export=view&id=1d4ujhhihYKmsGmKOEA-gfmpn3RqG8HS2)

### Experimental results

Results of Model

|  | Accuracy |
| --- | --- |
| Training Data | 97.29% |
| Testing Data | 90% |

The following images shows the trend of loss function,  Accuracy function

![image](https://drive.google.com/uc?export=view&id=1VHig4nOGa0Er49hN825TZiDoGePi-9IJ)

![image](https://drive.google.com/uc?export=view&id=1X6idMlIMi1OLOiJBGbDDKG8XviCMcg4S)

### Prediction

 A random image from the validation set is taken and checked whether the data is properly and with the correct model trained or not.

![image](https://drive.google.com/uc?export=view&id=1bTiLh064c6cFfj6q53SIvcKX62XT8XLA)

### References

[https://towardsdatascience.com/review-mobilenetv2-light-weight-model-image-classification-8febb490e61c](https://towardsdatascience.com/review-mobilenetv2-light-weight-model-image-classification-8febb490e61c)

[https://towardsdatascience.com/visualizing-and-preprocessing-image-dataset-e3ad574f7be6](https://towardsdatascience.com/visualizing-and-preprocessing-image-dataset-e3ad574f7be6)

[https://analyticsindiamag.com/a-deep-dive-into-image-data-preprocessing-by-tensorflow/](https://analyticsindiamag.com/a-deep-dive-into-image-data-preprocessing-by-tensorflow/)

[https://www.quora.com/How-are-smaller-sized-deep-learning-models-i-e-MobileNetv2-EfficientNet-B1-NasNet-Mobile-advantageous-over-larger-sized-models-i-e-VGG-16](https://www.quora.com/How-are-smaller-sized-deep-learning-models-i-e-MobileNetv2-EfficientNet-B1-NasNet-Mobile-advantageous-over-larger-sized-models-i-e-VGG-16)

[https://github.com/Mxbonn/visualwakewords](https://github.com/Mxbonn/visualwakewords)
