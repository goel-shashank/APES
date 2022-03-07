import os
import math
import time
import openai
import argparse
import pandas as pd
from tqdm import tqdm

openai.api_key = "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"

def generate_predictions(options):
    df_examples = pd.read_csv(options.examples_file)
    df_predictions = df_examples.copy(deep = True)

    df_predictions["prediction"] = None
    df_predictions["confidence"] = None

    batch_size = 100
    for i in tqdm(list(range(0, len(df_examples), batch_size))):
        prompts = df_examples[i:min(len(df_predictions), i + batch_size)]["prompt"].tolist()
        prompts = list(map(lambda prompt: f"Q: {prompt}\nA:", prompts))
        try:
            response = openai.Completion.create(engine = "davinci-instruct-beta", prompt = prompts, temperature = 0, max_tokens = 1, top_p = 1, frequency_penalty = 0, presence_penalty = 0, stop = ["\n"], logprobs = 1)["choices"]
            predictions = [d["text"].strip() for d in response]
            confidence = [math.exp(d["logprobs"]["token_logprobs"][0]) for d in response]
            df_predictions.loc[list(range(i, min(len(df_predictions), i + batch_size))), "prediction"] = predictions
            df_predictions.loc[list(range(i, min(len(df_predictions), i + batch_size))), "confidence"] = confidence
            os.makedirs(os.path.dirname(options.predictions_file), exist_ok = True)
            df_predictions.to_csv(options.predictions_file, index = False)
            time.sleep(1)
        except openai.error.RateLimitError:
            print("Key exhausted!")

if(__name__ == "__main__"):
    parser = argparse.ArgumentParser()
    
    parser.add_argument("-i,-e,--input,--examples", dest = "examples_file", type = str, required = True, help = "Input Examples File")
    parser.add_argument("-o,-p,--input,--predictions", dest = "predictions_file", type = str, required = True, help = "Output Predictions File")
    parser.add_argument("-d,--delay", dest = "delay", type = float, default = 1, help = "Time delay (in seconds) based on API'ssupported rate limie")
    
    options = parser.parse_args()
    generate_predictions(options)

# python -m src.generate_predictions -i "data/examples/disability.examples.csv" -o "data/predictions/disability.predictions.csv"
# python -m src.generate_predictions -i "data/examples/gender.examples.csv" -o "data/predictions/gender.predictions.csv"
# python -m src.generate_predictions -i "data/examples/religion.examples.csv" -o "data/predictions/religion.predictions.csv"
# python -m src.generate_predictions -i "data/examples/race.examples.csv" -o "data/predictions/race.predictions.csv"