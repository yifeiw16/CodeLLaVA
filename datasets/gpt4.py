import unicodedata
import matplotlib.pyplot as plt
from openai import OpenAI

client = OpenAI(
    api_key="sk-mnTfVOUdjIfBf8lAE6E45d150bD344Ac989fC120DbF65e89", # KEY
    base_url="https://lonlie.plus7.plus/v1"
)

inputs = "You are an awesome coder. Given the code:\n{code}\nBased on the provided code, please generate new code by changing bar colors, bar names, bar values and bar style. Please directly output you generated code."

code = "import matplotlib.pyplot as plt\n\nfig, ax = plt.subplots()\n\nfruits = ['apple', 'blueberry', 'cherry', 'orange']\ncounts = [40, 100, 30, 55]\nbar_labels = ['red', 'blue', '_red', 'orange']\nbar_colors = ['tab:red', 'tab:blue', 'tab:red', 'tab:orange']\n\nax.bar(fruits, counts, label=bar_labels, color=bar_colors)\n\nax.set_ylabel('fruit supply')\nax.set_title('Fruit supply by kind and color')\nax.legend(title='Fruit color')\n\nplt.show()"

completion = client.chat.completions.create(
    messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": inputs.format(code=code)}
  ],
    model="gpt-4-0125-preview",
    temperature=0.2
)

message = completion.choices[0].message
content = unicodedata.normalize('NFKC', message.content)

code_start = content.find("```python")
code_end = content[code_start+len("```python"):].find("```")
generated_code = content[code_start+len("```python"):][0:code_end].replace("```","")

print(generated_code)
exec(generated_code)

# Save the plot as a JPG file
plt.savefig('images/test.jpg')