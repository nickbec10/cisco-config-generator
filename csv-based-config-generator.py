import os, jinja2
from argparse import ArgumentParser

template_file = ""
csv_parameter_file = ""
config_parameters = []
output_directory = "output"


def get_args():
    global template_file
    global csv_parameter_file
    parser = ArgumentParser()
    parser.add_argument("-t", "--template", dest="template_file",
                        help="template file to write from", metavar="TEMPLATE")
    parser.add_argument("-c", "--csv", dest="csv_parameter_file",
                        help="parameter file to read from", metavar="CSV PARAMETERS")

    args = parser.parse_args()
    template_file = args.template_file
    csv_parameter_file = args.csv_parameter_file


def main():
    get_args()

    # 1. read the contents from the CSV files
    print("Read CSV parameter file...")
    f = open(csv_parameter_file)
    csv_content = f.read()
    f.close()

    # 2. for Jinja2, we need to convert the given CSV file into the a python
    # dictionary to get the script a bit more reusable, I will not statically
    # limit the possible header values (and therefore the variables)
    print("Convert CSV file to dictionaries...")
    csv_lines = csv_content.splitlines()
    headers = csv_lines[0].split(",")
    for i in range(1, len(csv_lines)):
        values = csv_lines[i].split(",")
        parameter_dict = dict()
        for h in range(0, len(headers)):
            parameter_dict[headers[h]] = values[h]
        config_parameters.append(parameter_dict)

    # 3. next we need to create the central Jinja2 environment and we will load
    # the Jinja2 template file
    print("Create Jinja2 environment...")
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(searchpath="."))
    template = env.get_template(template_file)

    # we will make sure that the output directory exists
    if not os.path.exists(output_directory):
        os.mkdir(output_directory)

    # 4. now create the templates
    print("Create templates...")
    for parameter in config_parameters:
        result = template.render(parameter)
        f = open(os.path.join(output_directory, parameter['site_id'] + "_4431VG.txt"), "w")
        f.write(result)
        f.close()
        print("Configuration '%s' created..." % (parameter['site_id'] + "_4431VG.txt"))
    print("DONE")

if __name__ == '__main__':
    main()
