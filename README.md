<div align="center">
<h1>
Text Style Transfer Example
</h1>

Built with `asyncflows`

[![main repo](https://img.shields.io/badge/main_repo-1f425f)](https://github.com/asynchronous-flows/asyncflows)
[![Discord](https://img.shields.io/badge/discord-7289da)](https://discord.gg/AGZ6GrcJCh)
[![Try in Colab](https://img.shields.io/badge/colab-red)](https://colab.research.google.com/github/asynchronous-flows/text-style-transfer-example/blob/main/text_style_transfer.ipynb)

</div>

## Introduction

This example writes about a topic in the style of another writing sample.

<div align="center">
<img width="706" alt="style transfer" src="https://github.com/asynchronous-flows/text-style-transfer-example/assets/24586651/463858e2-e7a0-49de-aecf-d14b9d1a6128">
</div>

## Running the Example

[![Try in Colab](https://img.shields.io/badge/Run_in_Google_Colab-red)](https://colab.research.google.com/github/asynchronous-flows/text-style-transfer-example/blob/main/text_style_transfer.ipynb)

To run the example locally:

1. Set up [Ollama](https://github.com/asynchronous-flows/asyncflows#setting-up-ollama-for-local-inference) or configure [another language model](https://github.com/asynchronous-flows/asyncflows#using-any-language-model)  

2. Clone the repository

```bash
git clone ssh://git@github.com/asynchronous-flows/text-style-tranfer-example
```

3. Change into the directory

```bash
cd text-style-tranfer-example
```

4. Create and activate your virtual environment (with, for example)

```bash
python3.11 -m venv .venv
source .venv/bin/activate
```

5. Install the dependencies

```bash
pip install -r requirements.txt
```

6. Run the example

```bash
python text_style_transfer.py
```

# Using your own Data

Replace the `writing_sample` at the top of `text_style_transfer.py` with your own.
