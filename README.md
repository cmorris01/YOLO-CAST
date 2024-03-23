# YOLO-CAST

### Convolutional Neural Networks

Computer vision is a subfield of computer science that focuses on enabling computers to understand and parse images. Object detection/localization in images is a common problem in computer vision--object detection is a technique that deals with detecting instances of objects of a certain class in digital images and videos.  Before the widespread adoption of neural network-based methods, the field of object detection relied on various non-neural approaches that, while innovative for their time, were generally less effective at accurately and robustly detecting objects in complex images than neural-network appraoches. Neural network-based methods became the focus of object-detection research and development with the improvement of compuational resources necessary to efficiently utilize neural networks. The field experimented with a multitude of network architectures, each with varying success in terms of accuracy and speed.

The convolutional neural network (CNN), or ConvNet, is one of the most widely-used, effective architecture, finding use in facial recognition, autonomously-operated robots and cars, and more. Convolutional neural networks are an extension/adaptation of multilayer-feed-forward neural networks [(read about here if new to neural networks)](http://neuralnetworksanddeeplearning.com/chap1.html) with a few specific modifications to make them particularly well-suited for processing visual information. These modifications include convolutional layers that capture features such as edges, textures, and shapes using squares of input data (input data being an image and its associated pixel value data). The square of input data, known as the feature weights, are 'convolved' (the mathematical operation the name of the network is derived from!) across an image in a sliding-window fashion to capture features relevant to identifying an object. Additionally, the convolutional layers contain some kind of activation function to introduce non-linearity into the network [(read about the function of activation functions here)](http://neuralnetworksanddeeplearning.com/chap1.html#sigmoid_neurons) & [(good visualization of role of activation functions)](https://www.youtube.com/watch?v=Ln8pV1AXAgQ); ReLU, or rectified linear unit, is one of the most commonly used activation functions, however activation functions are a rapidly developing area of research within deep learning so this is likely to change. The ReLU is defined as: 

f(x) = max(0, x)

This means that the output of the function is x if is greater than or equal to 0, and 0 otherwise. This is followed by pooling layers that reduce the spatial size of the feature maps (the map of features highlighted by the convolutional layers), reducing the amount of parameters and computation in the network. Finally, fully connected layers utilize features extracted and condensed by the convolutional layers and pooling layers respectively to perform classification and/or localization. These fully connected layers are the same as neuron layers used in traditional neural networks. It's important to note that these layers flatten the output data from previous layers into single vectors.

This website does a great job of visualizing a ConvNet performing classification: (https://adamharley.com/nn_vis/cnn/2d.html)
