from codebleu import calc_codebleu

prediction1 = '''import matplotlib.pyplot as plt                                                                                                                                
                                                                                                                                                               
data = [                                                                                                                                                       
    [60, 40, 20, 80, 100, 50, 30, 70, 90],                                                                                                                     
    [40, 20, 60, 80, 100, 50, 30, 70, 90],                                                                                                                     
    [20, 40, 40, 60, 80, 50, 30, 70, 90], 
    [60, 20, 80, 40, 60, 50, 30, 70, 90], 
    [40, 20, 60, 40, 60, 50, 30, 70, 90],
    [20, 40, 40, 40, 60, 50, 30, 70, 90],
    [60, 20, 80, 20, 60, 50, 30, 70, 90],
    [40, 20, 60, 20, 60, 50, 30, 70, 90],
    [20, 40, 40, 20, 60, 50, 30, 70, 90],
]                                                                              
                                                                               
colors = ['red', 'blue', 'orange']

for i in range(len(data)):        
    plt.plot(data[i], label=f'{colors[i]}')
                                       
plt.xlabel('Fruit Supply')                                                     
plt.ylabel('Fruit Color')
plt.legend()              
plt.show()'''

prediction2 = '''import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

fruits = ['apple', 'blueberry', 'cherry', 'orange']
counts = [40, 100, 30, 55]
bar_labels = ['red', 'blue', '_red', 'orange']
bar_colors = ['tab:red', 'tab:blue', 'tab:red', 'tab:orange']

ax.bar(fruits, counts, label=bar_labels, color=bar_colors)

ax.set_ylabel('fruit supply')
ax.set_title('Fruit supply by kind and color')
ax.legend(title='Fruit color')

plt.show()'''

prediction3 = '''import matplotlib.pyplot as plt

# Data
fruit_types = ['apple', 'blueberry', 'cherry', 'orange']
fruit_supply = [50, 90, 30, 80]
fruit_color = ['red', 'blue', 'red', 'orange']

# Create figure and plot space
plt.figure(figsize=(6, 4))

# Create bars with different colors
plt.bar(fruit_types, fruit_supply, color=fruit_color)

# Title and labels
plt.title('Fruit supply by kind and color')
plt.xlabel('Fruit kind')
plt.ylabel('Fruit supply')

# Create legend
from matplotlib.patches import Patch
legend_elements = [Patch(facecolor='red', label='red'),
                   Patch(facecolor='blue', label='blue'),
                   Patch(facecolor='orange', label='orange')]
plt.legend(handles=legend_elements, title='Fruit color')

# Show plot
plt.show()'''

reference = '''import matplotlib.pyplot as plt\n\nfig, ax = plt.subplots()\n\nfruits = ['apple', 'blueberry', 'cherry', 'orange']\ncounts = [40, 100, 30, 55]\nbar_labels = ['red', 'blue', '_red', 'orange']\nbar_colors = ['tab:red', 'tab:blue', 'tab:red', 'tab:orange']\n\nax.bar(fruits, counts, label=bar_labels, color=bar_colors)\n\nax.set_ylabel('fruit supply')\nax.set_title('Fruit supply by kind and color')\nax.legend(title='Fruit color')\n\nplt.show()'''

result = calc_codebleu([reference], [prediction3], lang="python", weights=(0.25, 0.25, 0.25, 0.25), tokenizer=None)
print(result)
# {
#   'codebleu': 0.5537, 
#   'ngram_match_score': 0.1041, 
#   'weighted_ngram_match_score': 0.1109, 
#   'syntax_match_score': 1.0, 
#   'dataflow_match_score': 1.0
# }