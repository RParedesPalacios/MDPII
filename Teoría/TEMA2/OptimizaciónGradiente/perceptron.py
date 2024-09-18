import numpy as np
import matplotlib.pyplot as plt

"""
Ejemplo de implementación del algoritmo del perceptrón para un problema de clasificación binaria.
Asignatura MDP II
Demo visual. El algoritmo en sí mismo es mucho más simple.
"""

def perceptron(S, learning_rate=0.1, max_iterations=100):

    # Initialize theta arbitrarily, add one extra dimension for the bias
    np.random.seed(0)
    theta = np.random.rand(S[0][0].shape[0])  # Random initialization

    # Set up the plot
    fig, ax = plt.subplots()
    ax.set_xlim(-1, 3)
    ax.set_ylim(-1, 4)
    ax.set_xlabel('x1')
    ax.set_ylabel('x2')
    ax.set_title('Perceptron Decision Boundary and Regions')

    # Plot the dataset points
    for x, c in S:
        if c == 1:
            ax.scatter(x[0], x[1], color='b', marker='o', label='Class +1' if 'Class +1' not in ax.get_legend_handles_labels()[1] else "")
        else:
            ax.scatter(x[0], x[1], color='g', marker='x', label='Class -1' if 'Class -1' not in ax.get_legend_handles_labels()[1] else "")
    ax.legend()

    # Function to plot the decision boundary and regions
    def plot_decision_boundary(theta, ax, misclassified_points=[]):
        # Create a grid to plot the decision regions
        xx, yy = np.meshgrid(np.linspace(-1, 3, 200), np.linspace(-1, 4, 200))
        grid = np.c_[xx.ravel(), yy.ravel(), np.ones(xx.ravel().shape)]  # Include bias term
        Z = np.dot(grid, theta)  # Compute the decision function
        Z = Z.reshape(xx.shape)


        # Clear previous plots
        for collection in ax.collections:
            collection.remove()

        # Plot the dataset points
        for index, (x, c) in enumerate(S):
            if index in misclassified_points:
                ax.scatter(x[0], x[1], color='red', s=100, edgecolors='black', linewidth=1.5)
            else:
                if c == 1:
                    ax.scatter(x[0], x[1], color='b', marker='o', s=50)
                else:
                    ax.scatter(x[0], x[1], color='g', marker='x', s=50)

        for index, (x, c) in enumerate(S):
            if c == 1:
                ax.scatter(x[0], x[1], color='b', marker='o', edgecolors='red' if index in misclassified_points else 'black')
            else:
                ax.scatter(x[0], x[1], color='g', marker='x', edgecolors='red' if index in misclassified_points else 'black')

        
        # Plot decision regions
        ax.contourf(xx, yy, Z, levels=[-np.inf, 0, np.inf], colors=['lightgreen', 'lightblue'], alpha=0.3)

        # Plot the decision boundary
        ax.contour(xx, yy, Z, levels=[0], colors='red')
    
    
    plot_decision_boundary(theta, ax)
    plt.waitforbuttonpress()

    for iteration in range(max_iterations):
        print("Iteration", iteration + 1)
        any_misclassified = False  
        misclassified_points = [] 

        for index, (x, c) in enumerate(S):
            # Check the misclassification condition: c * (theta^T * x) < 0
            if c * np.dot(theta, x) < 0:
                any_misclassified = True
                misclassified_points.append(index)
            else: 
                print("-")

        # Draw the current decision boundary, regions and errors
        plot_decision_boundary(theta, ax, misclassified_points)
        # Control with key-press or pause, comment to see only the final decision boundary
        plt.waitforbuttonpress()
        #plt.pause(0.1)

        #Update the parameter
        for index in misclassified_points:
            # Update theta: θ(k + 1) = θ(k) + ρ_k * c * x
            (x, c) = S[index]
            theta += learning_rate * c * x

        # If no misclassifications were made in the entire pass, we're done
        if not any_misclassified:
            print("Converged in", iteration + 1, "iterations.")
            break
    plt.waitforbuttonpress()
    return theta



## Main code

S = [
    (np.array([2, 3, 1]), 1),  # Example 1: x = [2, 3, 1], c = +1
    (np.array([1, 1, 1]), 1), # Example 2: x = [1, 1, 1], c = +1
    (np.array([2, 0, 1]), -1),  # Example 3: x = [2, 0, 1], c = -1
    (np.array([0, 1, 1]), -1)  # Example 4: x = [0, 1, 1], c = -1
]

# Run the perceptron algorithm
theta_final = perceptron(S, learning_rate=1.0, max_iterations=1000)
print("Final weight vector:", theta_final)
