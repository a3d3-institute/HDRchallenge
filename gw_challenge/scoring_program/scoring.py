import sys
import os
import json
import numpy as np

# Directory to read labels from
input_dir = sys.argv[1]
solutions = os.path.join(input_dir, 'ref')
prediction_dir = os.path.join(input_dir, 'res')

# Directory to output computed score into
output_dir = sys.argv[2]

def read_prediction():
    prediction_file = os.path.join(prediction_dir,'test.predictions')

    # Check if file exists
    if not os.path.isfile(prediction_file):
        print('[-] Test prediction file not found!')
        print(prediction_file)
        return


    f = open(prediction_file, "r")

    predicted_scores = f.read().splitlines()
    predicted_scores = np.array(predicted_scores,dtype=float)
    print(predicted_scores)

    return predicted_scores


def read_solution():
    print(os.listdir(solutions))

    solution_file = os.path.join(solutions, 'ligo_bb_50.npz')

    # Check if file exists
    if not os.path.isfile(solution_file):
        print('[-] Test solution file not found!')
        return

    test_labels = np.load(solution_file)['ids']
    
    return test_labels


def save_score(TNR):
    score_file = os.path.join(output_dir, 'scores.json')

    scores = {
        'TNR': TNR,
    }
    with open(score_file, 'w') as f_score:
        f_score.write(json.dumps(scores))
        f_score.close()


def print_pretty(text):
    print("-------------------")
    print("#---",text)
    print("-------------------")


    
def main():

    # Read prediction and solution
    print_pretty('Reading prediction')
    prediction = read_prediction()
    solution = read_solution()

    # Compute Score
    print_pretty('Computing score')
    tp = np.sum(np.logical_and(prediction == 1, solution == 1))
    tn = np.sum(np.logical_and(prediction == 0, solution == 0))
    fp = np.sum(np.logical_and(prediction == 1, solution == 0))
    fn = np.sum(np.logical_and(prediction == 0, solution == 1))   
    TNR = tn / (fp + tn) 
    print("TNR: ", TNR)

    # Avoid TNR = NaN
    if np.isnan(TNR):
        TNR = 0.0
        print("TNR is NaN, setting to 0.0")

    # Write Score
    print_pretty('Saving prediction')
    save_score(TNR)


if __name__ == '__main__':
    main()