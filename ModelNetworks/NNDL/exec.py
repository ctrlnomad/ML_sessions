from ModelNetworks.NNDL.Network import Network, load_data_shared, ReLU
from ModelNetworks.NNDL.ConvLayer import ConvPoolLayer
from ModelNetworks.NNDL.FullyConnectedLayer import FullyConnectedLayer
from ModelNetworks.NNDL.SoftmaxLayer import SoftmaxLayer

expanded_training_data, validation_data, test_data = load_data_shared()

mini_batch_size = 20

net = Network([
    ConvPoolLayer(image_shape=(mini_batch_size, 1, 28, 28),
                  filter_shape=(20, 1, 5, 5),
                  poolsize=(2, 2),
                  activation_fn=ReLU),
    ConvPoolLayer(image_shape=(mini_batch_size, 20, 12, 12),
                  filter_shape=(40, 20, 5, 5),
                  poolsize=(2, 2),
                  activation_fn=ReLU),
    FullyConnectedLayer(
        n_in=40 * 4 * 4, n_out=1000, activation_fn=ReLU, p_dropout=0.5),
    FullyConnectedLayer(
        n_in=1000, n_out=1000, activation_fn=ReLU, p_dropout=0.5),
    SoftmaxLayer(n_in=1000, n_out=10, p_dropout=0.5)],
    mini_batch_size)

net.SGD(expanded_training_data, 10, mini_batch_size, 0.03,
        validation_data, test_data)
