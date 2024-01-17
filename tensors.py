import torch
import numpy as np


def init_directly_from_data():
    data = [[1, 2], [3, 4]]
    x_data = torch.tensor(data)
    print(f"Data Tensor: \n {x_data} \n")


def main():
    init_directly_from_data()


if __name__ == "__main__":
    main()
