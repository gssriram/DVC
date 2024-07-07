import os
import sys
import pandas as pd
from sklearn.preprocessing import LabelEncoder



def generate_encoders(train_input, test_input, train_output, test_output):
    # initialising LabelEncoder
    le = LabelEncoder()

    df_train = pd.read_csv(train_input)
    df_test = pd.read_csv(test_input)

    for col in df_train.columns:
        combined_col = pd.concat([df_train[col], df_test[col]], axis=0)
        le.fit(combined_col)

        df_train[col] = le.transform(df_train[col])
        df_test[col] = le.transform(df_test[col])

    df_train.to_csv(train_output, index=False)
    df_test.to_csv(test_output, index=False)
    

def main():

    if len(sys.argv) != 3 and len(sys.argv) != 5:
        sys.stderr.write("Arguments error. Usage:\n")
        sys.stderr.write("\tpython featurization.py data-dir-path features-dir-path\n")
        sys.exit(1)

    in_path = sys.argv[1]
    out_path = sys.argv[2]

    train_input = os.path.join(in_path, "train.csv")
    test_input = os.path.join(in_path, "test.csv")
    train_output = os.path.join(out_path, "train_encoded.csv")
    test_output = os.path.join(out_path, "test_encoded.csv")

    os.makedirs(out_path, exist_ok=True)

    generate_encoders(train_input, test_input, train_output, test_output)

if __name__ == "__main__":
    main()
