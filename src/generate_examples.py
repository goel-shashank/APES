import os
import re
import argparse
import itertools
import pandas as pd
from utils import config
from utils.load_domains import load_domains 

def get_constraint_argument_values(constraint_arguments, param_id_value_map):
    constraint_arguments = list(map(str.strip, constraint_arguments.split(",")))
    constraint_argument_values = []
    for constraint_argument in constraint_arguments:
        constraint_arguments_param_id = constraint_argument.split("_")[0][1:]
        constraint_argument_value = param_id_value_map[constraint_arguments_param_id]["class"] if (constraint_argument.endswith("_class")) else param_id_value_map[constraint_arguments_param_id]["name"]
        constraint_argument_values.append(constraint_argument_value)
    return constraint_argument_values

def generate_examples(options):
    domains = load_domains(domain_dir_path = os.path.join(config.root, "data", "domains"))
    
    df_templates = pd.read_csv(options.templates_file)
    df_examples = pd.DataFrame(columns = ["template_id", "prompt"])

    param_column_pattern = re.compile("^param_\d+$")
    param_columns = [column for column in df_templates.columns if param_column_pattern.match(column)]
    param_ids = [param_column.split("_")[1] for param_column in param_columns]

    example_data = [] 
    for _, template_row in df_templates.iterrows():
        template_id = template_row["template_id"]
        template_text = template_row["template_text"]
        constraints = template_row["constraints"]
        label = template_row["label"]

        param_domains = [template_row[param_column] for param_column in param_columns]   
        param_domains_values = [domains[param_domain] if(type(param_domain) == str) else [{"name": "", "class": ""}] for param_domain in param_domains]    

        for param_values in itertools.product(*param_domains_values):
            param_id_value_map = dict(zip(param_ids, param_values))

            valid = True
            if(type(constraints) == str):
                for constraint in constraints.split("|"):
                    constraint = constraint.strip()
                    constraint_type = constraint.split("(", 1)[0]
                    if(constraint_type == "neq"):
                        constraint_arguments = constraint[len(constraint_type) + 1:-1]
                        value_1, value_2 = get_constraint_argument_values(constraint_arguments, param_id_value_map)
                        if(value_1 == value_2):
                            valid = False
                            break
             
            if(valid):
                example_row = {"template_id": template_id}
                example_prompt = template_text
                for param_id, param_value in param_id_value_map.items():
                    example_prompt = example_prompt.replace(f"#{param_id}", param_value["name"])
                    example_row[f"param_{param_id}_name"] = param_value["name"]
                    example_row[f"param_{param_id}_class"] = param_value["class"]
                
                example_row["prompt"] = f"{example_prompt} Yes or No?"
                example_row["label"] = label
                example_data.append(example_row)

    df_examples_columns = ["template_id"] + [f"{param_column}_name" for param_column in param_columns] + [f"{param_column}_class" for param_column in param_columns] + ["prompt", "label"]
    df_examples = pd.DataFrame(example_data, columns = df_examples_columns)
    os.makedirs(os.path.dirname(options.examples_file), exist_ok = True)
    df_examples.to_csv(options.examples_file, index = False)

if(__name__ == "__main__"):
    parser = argparse.ArgumentParser()
    
    parser.add_argument("-i,-t,--input,--templates", dest = "templates_file", type = str, required = True, help = "Input Templates File")
    parser.add_argument("-o,-e,--output,-examples", dest = "examples_file", type = str, required = True, help = "Output Examples File")
    
    options = parser.parse_args()
    generate_examples(options)

# python -m src.generate_examples -i "data/templates/disability.templates.csv" -o "data/examples/disability.examples.csv"
# python -m src.generate_examples -i "data/templates/gender.templates.csv" -o "data/examples/gender.examples.csv"
# python -m src.generate_examples -i "data/templates/religion.templates.csv" -o "data/examples/religion.examples.csv"
# python -m src.generate_examples -i "data/templates/race.templates.csv" -o "data/examples/race.examples.csv"