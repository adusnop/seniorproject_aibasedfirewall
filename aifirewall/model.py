from convert_data import create_data_model
from convert_data import create_data_input
import tensorflow as tf
import numpy as np

train_x, train_y, list_ip = create_data_model()
x_input, input_ip = create_data_input()

n_nodes_hl1 = 210
n_nodes_hl2 = 210
n_nodes_hl3 = 210

n_classes = 2
batch_size = 500
hm_epochs = 20

x = tf.placeholder('float')
y = tf.placeholder('float')
z = tf.placeholder('float')

hidden_1_layer = {'f_fum': n_nodes_hl1,
                  'weight': tf.Variable(tf.random_normal([train_x.shape[1], n_nodes_hl1])),
                  'bias': tf.Variable(tf.random_normal([n_nodes_hl1]))}

hidden_2_layer = {'f_fum': n_nodes_hl2,
                  'weight': tf.Variable(tf.random_normal([n_nodes_hl1, n_nodes_hl2])),
                  'bias': tf.Variable(tf.random_normal([n_nodes_hl2]))}

hidden_3_layer = {'f_fum': n_nodes_hl3,
                  'weight': tf.Variable(tf.random_normal([n_nodes_hl2, n_nodes_hl3])),
                  'bias': tf.Variable(tf.random_normal([n_nodes_hl3]))}

output_layer = {'f_fum': None,
                'weight': tf.Variable(tf.random_normal([n_nodes_hl3, n_classes])),
                'bias': tf.Variable(tf.random_normal([n_classes])), }


def neural_network_model(data):
    l1 = tf.add(tf.matmul(data, hidden_1_layer['weight']), hidden_1_layer['bias'])
    l1 = tf.nn.relu(l1)

    l2 = tf.add(tf.matmul(l1, hidden_2_layer['weight']), hidden_2_layer['bias'])
    l2 = tf.nn.relu(l2)

    l3 = tf.add(tf.matmul(l2, hidden_3_layer['weight']), hidden_3_layer['bias'])
    l3 = tf.nn.relu(l3)

    output = tf.matmul(l3, output_layer['weight']) + output_layer['bias']

    return output


def train_neural_network(x):
    prediction = neural_network_model(x)
    cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=prediction, labels=y))
    optimizer = tf.train.AdamOptimizer(learning_rate=0.001).minimize(cost)

    with tf.Session() as sess:
        sess.run(tf.initialize_all_variables())
        for epoch in range(hm_epochs):
            epoch_loss = 0
            i = 0

            while i < len(train_x):
                start = i
                end = i + batch_size
                batch_x = np.array(train_x[start:end])
                batch_y = np.array(train_y[start:end])

                _, c = sess.run([optimizer, cost], feed_dict={x: batch_x,
                                                              y: batch_y})
                epoch_loss += c
                i += batch_size

            print('Epoch', epoch + 1, 'completed out of', hm_epochs, 'loss:', epoch_loss)

        result_array = np.array([])


        batch_x = np.array(x_input)
        result = (sess.run(tf.argmax(prediction.eval(feed_dict={z: batch_x}), 1)))
        result_array = np.append(result_array, result)
        return result_array


def show_output(input_ip):
    result = train_neural_network(z)
    for i in range(len(result)):
        if result[i] == 0:
            input_ip[i].insert(0,'allow')
        elif result[i] == 1:
            input_ip[i].insert(0,'deny')
    with open('output.csv', 'w') as filehandle:
        for l in input_ip:
            for col in l:
                filehandle.write(col)
                filehandle.write(',')
            filehandle.write('\n')

show_output(input_ip)