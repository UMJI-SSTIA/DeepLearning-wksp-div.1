# 深度学习的工作原理

*Completely rough draft by GPT4.0*

## 1. 神经网络

神经网络由多个层组成，每个层都由许多神经元组成。每个神经元接收输入，对其进行处理，然后将输出传递给下一层。

### 1.1 神经元

神经元是神经网络的基本单元。每个神经元接收一些输入，将这些输入与其权重相乘，然后应用一个激活函数，如ReLU或sigmoid。输出然后传递到下一个层。

### 1.2 权重和偏置

权重和偏置是神经网络中的参数，它们在训练过程中被学习。权重决定了每个输入对神经元输出的重要性，而偏置允许神经元调整其输出。

## 2. 训练神经网络

训练神经网络的目标是找到一组权重和偏置，使得网络的输出尽可能接近训练数据的目标输出。这是通过反向传播和梯度下降完成的。

### 2.1 反向传播

反向传播是一种算法，用于在神经网络中更新权重，以便模型可以学习更好的表示。它首先计算网络输出与目标输出之间的误差，然后计算这个误差相对于每个权重的梯度。这些梯度然后用于更新权重。

### 2.2 梯度下降

梯度下降是一种优化算法，用于找到函数的最小值。在神经网络中，这个函数是损失函数，它衡量了网络输出与目标输出之间的差距。通过反复更新权重以减小梯度，网络最终会收敛到一组能够最小化损失的权重。

## 参考资料

- [Deep Learning by Ian Goodfellow, Yoshua Bengio, and Aaron Courville](http://www.deeplearningbook.org/)
- [Deep Learning Specialization by Andrew Ng on Coursera](https://www.coursera.org/specializations/deep-learning)
- [MIT Intro to Deep Learning](http://introtodeeplearning.com/)
- [交大密院Deep Learning学习手册](https://github.com/Banyutong/deep_learning_hands_on)
- GPT 4.0 (不觉得用AI去写AI的资料很有趣吗，很符合我对AI的想像)
