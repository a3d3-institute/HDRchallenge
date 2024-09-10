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

    solution_file = os.path.join(solutions, 'answer.npy')

    # Check if file exists
    if not os.path.isfile(solution_file):
        print('[-] Test solution file not found!')
        return

    test_labels = np.load(solution_file)
    
    return test_labels


def save_score(score):
    score_file = os.path.join(output_dir, 'scores.json')

    scores = {
        'accuracy': score,
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
    # Identify the 50 most anomalous events
    num_anomalous_events = 50
    anomalous_indices = np.argsort(prediction)[-num_anomalous_events:]
    prediction = solution[anomalous_indices]
    score = np.sum(prediction == 1) / num_anomalous_events
    print("Accuracy: ", score)

    # Write Score
    print_pretty('Saving prediction')
    save_score(score)


if __name__ == '__main__':
    main()
