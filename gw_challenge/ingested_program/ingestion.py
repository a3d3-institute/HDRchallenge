import sys
import subprocess
import os
import re
import numpy as np
import pandas as pd
import time


# expected version pattern for requirements
VERSION_PATTERN = re.compile("^[N!]N(.N)*[{a|b|rc}N][.postN][.devN]$")

# Input directory to read test input from
input_dir = sys.argv[1]

# Output data directory to which to write predictions
output_dir = sys.argv[2]

submission_dir = sys.argv[3]

sys.path.append(output_dir)
sys.path.append(submission_dir)

def get_prediction_data():

    # set test data and solution file
    test_data_file = os.path.join(input_dir, 'ligo_blackbox.npz')

    # Read Test data
    with np.load(test_data_file) as file:
        X_test = file['data'].reshape((-1, 200, 2))

    return X_test

def save_prediction(prediction_prob):

    prediction_file = os.path.join(output_dir, 'test.predictions')

    predictions = np.array(prediction_prob)

    # predictions = tp_cut(predictions)

    with open(prediction_file, 'w') as f:
        for ind, lbl in enumerate(predictions):
            str_label = str(lbl)
            if ind < len(predictions)-1:
                f.write(str_label + "\n")
            else:
                f.write(str_label)

# def tp_cut(predictions):

#     # answers file
#     test_data_file = os.path.join(input_dir, 'ligo_blackbox.npz')

#     # Read solutions
#     with np.load(test_data_file) as file:
#         y_test = file['ids']
#         predictions = (predictions >= np.percentile(predictions[y_test == np.ones(len(y_test))], 90)).astype(int)

#     return predictions


def print_pretty(text):
    print("-------------------")
    print("#---",text)
    print("-------------------")


def install_from_whitelist(req_file):

    whitelist = open("/app/program/whitelist.txt", 'r').readlines()
    whitelist = [i.rstrip('\n') for i in whitelist]
    print(whitelist)

    for package in open(req_file, 'r').readlines():
        package = package.rstrip('\n')
        package_version = package.split("==")
        if len(package_version) > 2:
            # invalid format, don't use
            print(f"requested package {package} has invalid format, will install latest version (of {package_version[0]}) if allowed")
            package = package_version[0]
        elif len(package_version) == 2:
            version = package_version[1]
            if not VERSION_PATTERN.match(version):
                # invalid format of version, don't use
                print(f"requested package {package} has invalid version, will install latest version (of {package_version[0]}) if allowed")
                package = package_version[0]
        #print("accepted package name: ", package)
        #print("package name ", package_version[0])
        if package_version[0] in whitelist:
            # package must be in whitelist, so format check unnecessary
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
            print(f"{package_version[0]} installed")
        else:
            sys.exit(f"{package_version[0]} is not an allowed package. Please contact the organizers on GitHub to request acceptance of the package.")


def main():
    """
     Run the pipeline
     > Load
     > Predict
     > Save
    """

    start = time.time()

    requirements_file = os.path.join(submission_dir, "requirements.txt")
    if os.path.isfile(requirements_file):
        install_from_whitelist(requirements_file)

    duration = time.time() - start
    print_pretty(f'Duration of the package installation: {duration}')

    start = time.time()

    from model import Model

    print_pretty('Reading Data')
    X_test = get_prediction_data()

    print_pretty('Starting Learning')
    m = Model()
    m.load()

    print_pretty('Making Prediction')
    prediction_prob = m.predict(X_test)

    print_pretty('Saving Prediction')
    save_prediction(prediction_prob)

    duration = time.time() - start
    print_pretty(f'Total duration: {duration}')


if __name__ == '__main__':
    main()
