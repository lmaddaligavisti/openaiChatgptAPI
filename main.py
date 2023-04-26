# # This is a sample Python script.
#
# # Press ⌃R to execute it or replace it with your code.
# # Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
# #
# #
# # def print_hi(name):
# #     # Use a breakpoint in the code line below to debug your script.
# #     print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
# #
# #
# # # Press the green button in the gutter to run the script.
# # if __name__ == '__main__':
# #     print_hi('PyCharm')
# #
# # # See PyCharm help at https://www.jetbrains.com/help/pycharm/
#
#
# # run code is control shift R
#
# something = 7
#
# print(something)
# print(something)
# print(something)
# print(something)
# print(something)
# print(something)
#
#
# import openai
# import pandas as pd
#
# openai.api_key = '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'
#
# # Load the training data from a CSV file
# training_data_df = pd.read_csv("/Users/lakshmimaddali/Downloads/training_data.csv")
#
# # Convert the data to a string and use it as the prompt
# # Create a list of examples
# examples = []
# for i, row in training_data_df.iterrows():
#     example = {
#         "prompt": row["prompt"],
#         "completion": row["response"]
#     }
#     examples.append(example)
#
#
# # Set up the engine and parameters
# engine = "davinci"
# prompt = "Tell me a melancholy bedtime story with rain"
# temperature = 0.5
# max_tokens = 1000
#
# # Fine-tune the model with the training data
# response =  openai.FineTune.create(
#     model=engine,
#     prompt=prompt,
#     examples=examples,
#     temperature=temperature,
#     max_tokens=max_tokens)
#
# print(response)
#
#
import openai
import pandas as pd

# Set your OpenAI API key
openai.api_key = "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"

# Load the training data from a CSV file
training_data_df = pd.read_csv("/Users/lakshmimaddali/Downloads/training_data.csv")

# Convert the data to a list of examples
examples = []
for i, row in training_data_df.iterrows():
    example = {
        "input": row["prompt"],
        "output": row["response"]
    }
    examples.append(example)

# Set up the fine-tuning parameters
model_id = "davinci"
model_name = "lakshmi"
prompt = "Tell me a melancholy bedtime story with rain"
temperature = 0.5
max_tokens = 1000

# Create a new model based on the davinci model
response = openai.Model.create(
    engine="text-davinci-002",
    prompt=prompt,
    max_tokens=max_tokens,
    name="lakshmismodel",
    api_key="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"
)

model_id = response["id"]

# Fine-tune the new model with your training data
response = openai.FineTune.create(
    model=model_id,
    examples=examples,
    temperature=temperature,
    epochs=2
)

print(response)

