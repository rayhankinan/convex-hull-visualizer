import pandas as pd
from argparse import ArgumentParser
from sklearn import datasets

# Constants
COLORS = ["blue", "orange", "green", "red", "purple", "brown", "pink", "gray", "olive", "cyan"]

if __name__ == "__main__":
    my_parser = ArgumentParser(description="Masukkan nama database serta atribut yang ingin divisualisasi")

    my_parser.add_argument("path", metavar="path", type=str, help="relative path menuju file database")
    my_parser.add_argument("first_argument", metavar="first_argument", type=str, help="atribut pertama yang ingin dievaluasi")
    my_parser.add_argument("second_argument", metavar="second_argument", type=str, help="atribut kedua yang ingin dievaluasi")
    my_parser.add_argument("-t", "--target", type=str, help="atribut yang dijadikan target")

    args = my_parser.parse_args()

    if args.path == "iris":
        data = datasets.load_iris()
        df = pd.DataFrame(data.data, columns=data.feature_names)
        df["Target"] = pd.DataFrame(data.target)

        print(df.head())

    elif args.path == "wine":
        data = datasets.load_wine()
        df = pd.DataFrame(data.data, columns=data.feature_names)
        df["Target"] = pd.DataFrame(data.target)

        print(df.head())

    elif args.path == "breast_cancer":
        data = datasets.load_breast_cancer()
        df = pd.DataFrame(data.data, columns=data.feature_names)
        df["Target"] = pd.DataFrame(data.target)

        print(df.head())

    else:
        pass