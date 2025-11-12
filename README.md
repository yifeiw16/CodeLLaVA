# **CodeLLaVA**

## **Overview**

**CodeLLaVA** aims to build a multimodal dataset and benchmark for *code-to-image* and *image-to-code* understanding, focusing on underexplored yet practical code types. The goal is to develop and evaluate models that can generate, interpret, and visualize code effectively.

## **Target Code Types**

Focus primarily on **(1)** and **(4)** — these are easier to collect and less saturated.

1. **Python Code**

   * Libraries: `matplotlib`, `turtle`, `seaborn`, `pytorch`
   * Tasks:

     * Neural network architecture → PyTorch code
     * Tutorial-style examples (e.g., Runoob)
     * Reproducing plots from research papers
     * LeetCode screenshot to code
   * Reference: [Grok-1.5V](https://x.ai/blog/grok-1.5v)

2. **JavaScript**

   * Focus on visualization (e.g., D3.js, Chart.js) and interactive snippets.

3. **HTML (UI2Code)**

   * Many existing works; may be included as a secondary target.
   * Datasets:

     * [Paper 1](https://arxiv.org/pdf/2404.06369v1.pdf)
     * [Paper 2](https://arxiv.org/pdf/2403.03163.pdf)

4. **LaTeX / Markdown Code**

   * Generating diagrams, equations, and document-style visual content.


## **Data Collection Strategy**

1. **Official and Community Samples**
   Collect code-image pairs from public repositories and documentation:

   * [matplotlib/cheatsheets](https://github.com/matplotlib/cheatsheets)
   * [rougier/matplotlib-tutorial](https://github.com/rougier/matplotlib-tutorial)
   * [rasbt/matplotlib-gallery](https://github.com/rasbt/matplotlib-gallery)
   * [gboeing/data-visualization](https://github.com/gboeing/data-visualization)

2. **Model-Assisted Generation**

   * Use GPT-4 or similar models to generate code via few-shot prompting:

     * Text → Code
     * Code → Code
     * Image → Code
     * Combination tasks (e.g., merge bar and line plots)
   * Execute the generated code to produce images and form code–image pairs.



## **Benchmark Design**

1. **Executability** — whether generated code runs successfully.
2. **Code Similarity** — compare generated vs. reference code using [CodeBLEU](https://github.com/k4black/codebleu).
3. **Image Similarity** — compare output images using visual metrics ([reference 1](https://zhuanlan.zhihu.com/p/652344859), [reference 2](https://arxiv.org/pdf/2403.03163.pdf)).
4. **Human / GPT-4 Judging** — assess semantic correctness, readability, and visual fidelity.



## **Base MLLM and Training Plan**

Start with lightweight supervised fine-tuning (SFT) on existing multimodal bases, then expand to code-focused models.

1. **Initial Models**

   * [LLaVA](https://github.com/haotian-liu/LLaVA)
   * [MiniGemini](https://github.com/dvlab-research/MiniGemini)

2. **Future Base Model Options**

   * `code-gemma`
   * `code-qwen`
   * `code-llama`
   * `starcoder-v2`



## **Next Steps**

* Phase 1: Build dataset and code–image pipeline for Python visualization tasks.
* Phase 2: Develop automatic evaluation scripts for code and image similarity.
* Phase 3: SFT CodeLLaVA and benchmark against LLaVA/MiniGemini baselines.
