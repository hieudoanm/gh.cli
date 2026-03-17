import json
import yaml
from requests import get, Response
import pandas


url = "https://raw.githubusercontent.com/github-linguist/linguist/master/lib/linguist/languages.yml"
response: Response = get(url)
languages_yaml: str = response.text


with open("./data/languages.yaml", "w") as file:
    file.write(languages_yaml)  # Output: apple, banana, cherry


with open("./data/languages.json", "w") as json_file:
    languages_json: dict = yaml.safe_load(
        languages_yaml
    )  # yaml_object will be a list or a dict
    json.dump(languages_json, json_file, indent=2)


languages_list: list[dict] = []
for key, value in languages_json.items():
    item = {**value, "language": key}
    print(item)
    languages_list.append(item)


data_frame = pandas.DataFrame(languages_list)
data_frame.to_csv("./data/languages.csv", index=False)
