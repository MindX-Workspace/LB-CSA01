import pandas as pd
import matplotlib.pyplot as plt

file_path = './student-scores.csv'
data = pd.read_csv(file_path, usecols=['gender', 'math_score', 'physics_score'])

colors = {'male': 'blue', 'female': 'red'} 

plt.scatter(data['math_score'], data['physics_score'], c=data['gender'].map(colors))

plt.xlabel('Math Score')
plt.ylabel('Physics Score')
plt.title('Comparison of Math and Physics Scores by Gender')

plt.legend(handles=[plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='blue', label='Male'),
                    plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='red', label='Female')])

plt.grid(True)
plt.show()