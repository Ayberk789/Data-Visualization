import matplotlib.pyplot as plt

# Load and prepare the data
data = [['Apples', 5],
        ['Oranges', 3],
        ['Bananas', 7],
        ['Grapes', 4],
        ['Watermelon', 9],
        ['Melon',6],]
x_values = [item[0] for item in data]
y_values = [item[1] for item in data]

# Create the bar chart
plt.bar(x_values, y_values)

# Add labels and title
plt.xlabel('X Label')
plt.ylabel('Y Label')
plt.title('Bar Chart')

# Display the visualization
plt.show()
