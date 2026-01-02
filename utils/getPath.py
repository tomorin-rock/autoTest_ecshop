import os


def get_yaml_path(filename):
    root_dir = os.path.dirname(os.path.dirname(__file__))
    yml_dir = os.path.join(root_dir,"data",filename)
    return yml_dir

def get_log_path():
    root_dir = os.path.dirname(os.path.dirname(__file__))
    log_dir = os.path.join(root_dir,"logs")
    return log_dir

if __name__ == '__main__':
    print(get_yaml_path("login.yml"))
    print(get_log_path())