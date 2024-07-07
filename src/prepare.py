import pandas as pd
import sys
from sklearn.model_selection import train_test_split
import os
import yaml

def main():
    params = yaml.safe_load(open("params.yaml"))["prepare"]

    if len(sys.argv) != 2:
        sys.stderr.write("Arguments error. Usage:\n")
        sys.stderr.write("\tpython prepare.py data-file\n")
        sys.exit(1)

    # Test data set split ratio
    test_split_ratio = params["split"]
    r_state = params["seed"]

    # Loading data
    input = sys.argv[1]
    data = pd.read_csv(input)
    
    # Data splitting
    train_df, test_df = train_test_split(data, random_state=r_state, test_size=test_split_ratio)
    
    output_train = os.path.join("data", "prepared", "train.csv")
    output_test = os.path.join("data", "prepared", "test.csv")

    os.makedirs(os.path.join("data", "prepared"), exist_ok=True)

    # Exporting data into "data\prepared\" folder
    train_df.to_csv(output_train, index=False)
    test_df.to_csv(output_test, index=False)
    
    
if __name__ == "__main__":
    main()
