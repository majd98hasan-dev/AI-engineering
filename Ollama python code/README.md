# Ollama python code

## Purpose
The purpose is to compare responses and working time of two local LLMs using Ollama and Python.

## Models

Models used locally:

- Gemma4:e2b
- Qwen2.5:0.5b

## Running the python code

after downloading Ollama and both AI models and writing the python code.
Using PyCharms built-in Run function the program does this:
- first it sends the same prompt "What is the capital of Sweden?" to both models.
- it measures the working time for both models
- it prints the responses from both models in the terminal
- the `add_to_csv` function saves the (model name, response, working time, used prompt) to `test.csv`and appends new results everytime the program is run.

## Result

Both models answered correctly to the prompt, the only difference here is that Gemma used Markdown formatting in its answer while Qwen only gave the plain answer.
The main difference between the two models was the execution time, Gemma took a considerably longer time to solve a simple prompt while Qwen did it in around a second of thinking.
further tests with more complicated prompts would help determine which model would perform better and faster with complicated task.