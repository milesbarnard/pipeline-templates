#!/usr/bin/env python3

import argparse
import ruamel.yaml

def main():
    parser = argparse.ArgumentParser(description='Update image name or tag version in a Kubernetes manifest file')
    parser.add_argument("-c", "--cluster", help="Cluster to update i.e. <project_name>/dev", type=str, required=True)
    parser.add_argument("-i", "--image-key", help="Image key to update i.e. NGINX_PROXY", type=str, required=True)
    parser.add_argument("-s", "--substitute-value", help="Substitute value i.e. nginx:1.19.2", type=str, required=True)

    args = parser.parse_args()

    file_path = f"example_repo/{args.cluster}/apps.yaml"

def update_image(file_path: str, image_key: str, substitute_value: str):
    yaml = ruamel.yaml.YAML()
    yaml.width = 8192 # prevents line wrapping

    with open(file_path, 'r') as file:
        values = yaml.load(file)

    values["spec"]["postBuild"]["substitute"][image_key] = substitute_value

    with open(file_path, 'w') as file:
        yaml.dump(values, file)

if __name__ == "__main__":
    main()