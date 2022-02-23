import pandas as pd
import matplotlib.pyplot as plt
from argparse import ArgumentParser
from sklearn import datasets
# from scipy.spatial import ConvexHull
from myConvexHull import ConvexHull

# BATASAN: SEMUA DATA MASUKKAN HARUS DALAM NUMERIK

# Class and Function
class Color():
    COLORS = ["blue", "orange", "green", "red", "purple", "brown", "pink", "gray", "olive", "cyan"]
    i = 0

    def get_color():
        new_color = Color.COLORS[Color.i % len(Color.COLORS)]
        Color.i += 1

        return new_color

def plot_convex_hull(df, first_argument, second_argument, target, class_name):
    plt.figure(figsize=(10, 6))
    plt.title(f"{first_argument} vs {second_argument}")
    plt.xlabel(first_argument)
    plt.ylabel(second_argument)

    for target_value in df[target].unique():
        bucket = df[df[target] == target_value]

        hull = ConvexHull(bucket[[first_argument, second_argument]].values)

        plt.scatter(bucket[first_argument].values, bucket[second_argument].values, label=class_name[target_value])
        color = Color.get_color()

        for simplex in hull.create_convex(): # hull.simplices adalah numpy.ndarray of numpy.ndarray yang berisi dua index dari titik-titik terluar data yang jika dihubungkan membentuk sisi pada convex hull
            # plt.plot([x1, x2], [y1, y2]) akan membentuk garis dari (x1, y1) ke (x2, y2)
            
            plt.plot(bucket[[first_argument, second_argument]].values[simplex, 0], bucket[[first_argument, second_argument]].values[simplex, 1], color)

    plt.legend()
    plt.show()

# Main Program
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