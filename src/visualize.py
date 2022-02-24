import pandas as pd
from argparse import ArgumentParser
from sklearn import datasets
from myConvexHull import plot_convex_hull

# BATASAN: HANYA TERDEFINISI PADA DATASET CLASSIFICATION
# BATASAN: SEMUA DATA ATRIBUT HARUS DALAM BENTUK NUMERIK

# MAIN PROGRAM
if __name__ == "__main__":
    my_parser = ArgumentParser(description="Masukkan nama database serta atribut yang ingin divisualisasi")

    my_parser.add_argument("path", metavar="path", type=str, help="relative path menuju file database")
    my_parser.add_argument("first_argument", metavar="first_argument", type=str, help="atribut pertama yang ingin dievaluasi")
    my_parser.add_argument("second_argument", metavar="second_argument", type=str, help="atribut kedua yang ingin dievaluasi")
    my_parser.add_argument("-t", "--target", type=str, help="atribut yang dijadikan target", default="")
    my_parser.add_argument("-c", "--class-name", type=str, nargs="+",help="nama kelas pada atribut target", default=[])

    args = my_parser.parse_args()

    if args.path == "iris":
        data = datasets.load_iris()
        df = pd.DataFrame(data.data, columns=data.feature_names)
        df["Target"] = pd.DataFrame(data.target)

        if args.first_argument not in data.feature_names or args.second_argument not in data.feature_names or args.target != "" or args.class_name != []:
            print("Argumen tidak valid!")
            
        else:
            plot_convex_hull(df=df, first_argument=args.first_argument, second_argument=args.second_argument, target="Target", class_name=["Iris-Setosa", "Iris-Versicolour", "Iris-Virginica"])

    elif args.path == "wine":
        data = datasets.load_wine()
        df = pd.DataFrame(data.data, columns=data.feature_names)
        df["Target"] = pd.DataFrame(data.target)

        if args.first_argument not in data.feature_names or args.second_argument not in data.feature_names or args.target != "" or args.class_name != []:
            print("Argumen tidak valid!")
            
        else:
            plot_convex_hull(df=df, first_argument=args.first_argument, second_argument=args.second_argument, target="Target", class_name=["class_0", "class_1", "class_2"])

    elif args.path == "breast_cancer":
        data = datasets.load_breast_cancer()
        df = pd.DataFrame(data.data, columns=data.feature_names)
        df["Target"] = pd.DataFrame(data.target)

        if args.first_argument not in data.feature_names or args.second_argument not in data.feature_names or args.target != "" or args.class_name != []:
            print("Argumen tidak valid!")
            
        else:
            plot_convex_hull(df=df, first_argument=args.first_argument, second_argument=args.second_argument, target="Target", class_name=["WDBC-Malignant", "WDBC-Benign"])

    else:
        try:
            df = pd.read_csv(args.path)

            if args.first_argument not in df.columns or args.second_argument not in df.columns or args.target not in df.columns or args.class_name == []:
                print("Argumen tidak valid!")
            
            else:
                plot_convex_hull(df=df, first_argument=args.first_argument, second_argument=args.second_argument, target=args.target, class_name=args.class_name)

        except:
            print(f"Database dengan relative path {args.path} tidak ada!")