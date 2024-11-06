import numpy as np


class NeuralNetwork:
    

    def __init__(self):
        
        np.random.seed(np.random.randint(1,100))

        self.synaptic_weights = 2 * np.random.random((13,1)) - 1

    
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def sigmoid_derivative(self, x):
        return x * (1 - x)

    def train(self, training_inputs, training_outputs, training_iterations):

        for iteration in range(training_iterations):

            output = self.think(training_inputs)
            error = training_outputs - output
            adjustments = np.dot(training_inputs.T, error * self.sigmoid_derivative(output))
            self.synaptic_weights += adjustments
    
    def think(self, inputs):
        
        inputs = inputs.astype(float)
        output = self.sigmoid(np.dot(inputs, self.synaptic_weights))

        return output


if __name__ == "__main__":
    
    neural_network = NeuralNetwork()

    print("Random Synaptic Weights:")
    print(neural_network.synaptic_weights)

    training_inputs = np.array([[1,0,0,1,1,0,0,0,0,1,0,1,0],
                                [1,0,0,1,0,1,0,0,0,1,1,1,1],
                                [1,0,0,0,0,1,1,1,0,1,0,0,1],
                                [0,1,0,1,0,1,0,0,1,1,0,0,1],
                                [1,0,0,0,0,1,0,0,0,0,1,1,0],
                                [1,1,1,0,1,0,0,0,0,0,0,1,0],
                                [0,0,0,1,1,0,1,0,0,1,0,1,1],
                                [0,0,1,0,0,1,0,1,1,1,1,0,0],
                                [1,1,1,1,1,0,0,0,0,1,1,0,1],
                                [0,0,0,1,0,1,1,1,0,0,1,1,1],
                                [0,0,1,1,0,1,0,0,0,1,0,1,1],
                                [1,1,1,1,1,0,0,0,1,0,1,0,1],
                                [1,0,0,1,1,1,0,1,1,0,1,0,0],
                                [0,1,0,0,0,1,1,0,1,1,0,1,1],
                                [0,1,1,1,0,1,0,0,0,1,0,1,0],
                                [1,1,1,1,1,0,0,0,0,0,0,0,0],
                                [0,1,1,1,1,1,0,0,0,0,0,0,0],
                                [0,0,1,1,1,1,1,0,0,0,0,0,0],
                                [0,0,0,1,1,1,1,1,0,0,0,0,0],
                                [0,0,0,0,1,1,1,1,1,0,0,0,0],
                                [0,0,0,0,0,1,1,1,1,1,0,0,0],
                                [0,0,0,0,0,0,1,1,1,1,1,0,0],
                                [0,0,0,0,0,0,0,1,1,1,1,1,0],
                                [0,0,0,0,0,0,0,0,1,1,1,1,1],
                                [1,0,0,0,0,0,0,0,0,1,1,1,1],
                                [0,0,1,1,0,1,0,1,0,1,0,0,0]])
    
    training_outputs = np.array([[0,1,0,0,0,0,0,0,1,0,0,1,0,0,0,1,1,1,1,1,1,1,1,1,1,0]]).T

    neural_network.train(training_inputs, training_outputs, 50000)

    print("Synaptic Weights After Training:")
    print(neural_network.synaptic_weights)
    
    running = True

    while running:

        Ace = str(input("Ace? "))
        King = str(input("King? "))
        Queen = str(input("Queen? "))
        Jack = str(input("Jack? "))
        Ten = str(input("Ten? "))
        Nine = str(input("Nine? "))
        Eight = str(input("Eight? "))
        Seven = str(input("Seven? "))
        Six = str(input("Six? "))
        Five = str(input("Five? "))
        Four = str(input("Four? "))
        Three = str(input("Three? "))
        Two = str(input("Two? "))

        print("New Input Data = ", Ace, King, Queen, Jack, Ten, Nine, Eight, Seven, Six, Five, Four, Three, Two)
        print("Output Data: ")
        print(neural_network.think(np.array([Ace, King, Queen, Jack, Ten, Nine, Eight, Seven, Six, Five, Four, Three, Two])))
        running = str(input("Again? "))