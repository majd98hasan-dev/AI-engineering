import ollama
import LLMcalls
import time

#downaloded models
models = ["gemma4:e2b", "qwen2.5:0.5b"]

prompt = "What is the capital of Sweden?"

#main function to run the code
def main():

    #create the csv file with column names
    #True and False at the end, true would create a new file or clear an existing test.csv file
    #and False just fills the first empty file in the csv
    LLMcalls.add_to_csv("test.csv",[ "Model", "response", "time", "prompt"], new=False)

    #loop through both models using the same prompt
    for model in models:
        #print the models name
        print(f"Model: {model}")

        #start counting working time (elapsed time)
        start = time.perf_counter()

        #send the prompt to the model
        response = ollama.chat(model=model, messages=[{"role": "user", "content": prompt}])

        #stop recording the working time
        end = time.perf_counter()

        #calculate elapsed time
        elapsed = end - start

        #add the results to the test.csv
        #response["message"]["content"] to avoid saving meta data and keep the file info clear
        #round(elapsed, 2) to limit decimals to 2 digits to avoid long digit lines
        #if you want you can test with only "response" and "elapsed" and run the code to see the difference of the result
        LLMcalls.add_to_csv("test.csv",[model, response["message"]["content"], round(elapsed, 2), prompt])

        #pring the response in the terminal
        print(response['message']['content'])
        #print the working time in the terminal
        print(f"response time: {elapsed} seconds")


if __name__ == "__main__":
    main()
