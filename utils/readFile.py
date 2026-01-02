import yaml

from autoTest_ecshop.utils.getPath import get_yaml_path


def read_file(filename):
    yml_path = get_yaml_path(filename)
    with open(yml_path,"r",encoding="utf-8") as f:
        return yaml.safe_load(f)

if __name__ == "__main__":
    yaml_dir = get_yaml_path("login.yml")
    data = read_file("login.yml")
    print(yaml_dir)
    print(data.get("loginInfos")[0][1])

