# YOLO-CAST

### Convolutional Neural Networks

Computer vision is a subfield of computer science that focuses on enabling computers to understand and parse images. Object detection/localization in images is a common problem in computer vision--object detection is a technique that deals with detecting instances of objects of a certain class in digital images and videos.  Before the widespread adoption of neural network-based methods, the field of object detection relied on various non-neural approaches that, while innovative for their time, were generally less effective at accurately and robustly detecting objects in complex images than neural-network appraoches. Neural network-based methods became the focus of object-detection research and development with the improvement of compuational resources necessary to efficiently utilize neural networks. The field experimented with a multitude of network architectures, each with varying success in terms of accuracy and speed.

The convolutional neural network (CNN), or ConvNet, is one of the most widely-used, effective architecture, finding use in facial recognition, autonomously-operated robots and cars, and more. Convolutional neural networks are an extension/adaptation of multilayer-feed-forward neural networks [(read about here if new to neural networks)](http://neuralnetworksanddeeplearning.com/chap1.html) with a few specific modifications to make them particularly well-suited for processing visual information. These modifications include convolutional layers that capture features such as edges, textures, and shapes using squares of input data (input data being an image and its associated pixel value data). The square of input data, known as the feature weights, are 'convolved' (the mathematical operation the name of the network is derived from!) across an image in a sliding-window fashion to capture features relevant to identifying an object. Additionally, the convolutional layers contain some kind of activation function to introduce non-linearity into the network [(read about the function of activation functions here)](http://neuralnetworksanddeeplearning.com/chap1.html#sigmoid_neurons) & [(visualization of role of activation functions)](https://www.youtube.com/watch?v=Ln8pV1AXAgQ); ReLU, or rectified linear unit, is one of the most commonly used activation functions, however activation functions are a rapidly developing area of research within deep learning so this is likely to change. The ReLU is defined as: 

`f(x) = max(0, x)`

This means that the output of the function is x if is greater than or equal to 0, and 0 otherwise. This is followed by pooling layers that reduce the spatial size of the feature maps (the map of features highlighted by the convolutional layers), reducing the amount of parameters and computation in the network. Finally, fully connected layers utilize features extracted and condensed by the convolutional layers and pooling layers respectively to perform classification and/or localization. These fully connected layers are the same as neuron layers used in traditional neural networks. It's important to note that these layers flatten the output data from previous layers into single vectors.

This website does a great job of visualizing a ConvNet performing classification: (https://adamharley.com/nn_vis/cnn/2d.html)

There are a lot of details I glossed over, mostly concerning the learning process ConvNets utilize to discover optimal parameter weights; you can read more about the learning process here: (http://neuralnetworksanddeeplearning.com/chap2.html) & (http://neuralnetworksanddeeplearning.com/chap3.html).

### The YOLO (You Only Look Once) Algorithm

The YOLO algorithm is a real-time object detection convolutional network architecture developed by computer-vision researchers Joseph Redmon and Ali Farhadi in 2015. Unlike traditional methods that process an image multiple times to detect objects, YOLO divides the image into a grid and predicts bounding boxes and class probabilities for each grid cell in a single pass. This unique approach allows YOLO to detect objects in real-time, making it ideal for applications requiring fast processing, such as video surveillance and autonomous vehicles.

Today, the YOLO algorithm is open-sourced, maintained, and further developed by Ultralytics, which offers a robust Python implementation of YOLO, known as YOLOv8. Ultralytics provides a suite of tools and features that enhance the usability and functionality of YOLO for a wide array of applications, from academic research to industrial deployment. YOLOv8 is highly customizable, provides a wide array of real-time and post-hoc training metrics, and is easily troubleshooted due to substantial community support.

The Ultralytics YOLO documentation is located at https://docs.ultralytics.com/.

### Gathering Training Data

The demo training notebook located within this repository will detail a majority of the real-time training process; however, the notebook does not detail an essential part of the training process: gathering training data.

The training data for YOLO consists of images and corresponding annotation files that provide details about the objects within these images. Each annotation file corresponds to an image file and contains one or more lines, each representing a different object in the image. A line in the annotation file follows the format:

`object-class, x-center, y-center, width, height`

Here, object-class is an integer representing the class of the object, and x-center, y-center, width, and height are float values relative to the width and height of the image, ranging between 0 and 1. These values denote the center coordinates of the object's bounding box, as well as the bounding box's width and height. The use of relative coordinates makes the model adaptable to images of different sizes.

Training data can be hard to come by, especially if you are attempting to train a model for a niche or novel purpose. If labeled data is unavailable, there are ways to gather and label custom data, although this can be time consuming. Obtaining training imagery is generally done through webscraping or creating custom images. Labeling imagery is typically best done through third party software; cvat.ai is my prefered annotation software (https://www.cvat.ai/). This video is a fantastic introduction to training a YOLO model, and it discusses how to use cvat.ai to label custom data.

Effective models usually require training on a large scale, often involving hundreds, thousands, or even tens of thousands of data points. Insufficient training data can lead to overfitting (https://www.ibm.com/topics/overfitting.), a scenario where the model learns specific idiosyncrasies of the training data that don't apply more broadly. Consequently, it struggles to generalize to new data not included in the limited training set. 

Transfer learning and data augmentation are approaches to 'artificially' supplement/expand training data. Data augmentation is a data expansion technique in which spatial/color transformations are applied to existing imagery in the training set; data augmentation will aid a model in generalizing regardless of environmental variables (lighting, rotation of object in view, etc.) without the need for more unique imagery. Common data augmentations include rotation; translation; rescaling; cropping; adjusting saturation, brightness, or contrast; noise injection; and cutout. 

Unlike data augmentation, transfer learning as a technique does not directly involve expanding training data. Transfer learning refers to repurposing a pre-trained model--a model trained previously for another task--for use in a seperate task; pretrained models are most often models trained on a large, general dataset (usually a task with abundant data, like image classification on ImageNet). Normally, the pre-trained is retrained on the new training data but some semblance of learning already exists within the model. The intuition behind transfer learning's effectiveness is rooted in the hierarchical way deep learning models learn representations. Early layers capture generic features (like edges, colors, and textures) that are common across various tasks, while deeper layers become more specialized to the specifics of the data and task they were originally trained on. By reusing the lower layers' general representations, a model can be adapted to a new task with less data, since it already "understands" the nuances of spatial structure in visual information.

Data augmentation and transfer learning are powerful tools. Note, however, that they are not substitutes for a robust training set. Models that utilize augmentation and transfer learning are still susceptible to problems of overfitting. Data augmentation and transfer learning are demonstrated in the demo training notebook.





