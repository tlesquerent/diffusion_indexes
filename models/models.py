import os
import pickle


def save_model(my_model, file_name):  # ex : file_name = "trained_model.pickle"
    base_dir = 'models/'
    file_path = base_dir + file_name
    if os.path.exists(file_path):
        print("Model already exists")

    else:
        with open(file_name, "wb") as file:
            pickle.dump(file_name, file)
            print('ok')


def open_model(file_name):
    base_dir = '//models/'
    file_path = base_dir+file_name
    if os.path.exists(file_path):
        print("Loading Trained Model")
        model = pickle.load(open(file_path, "rb"))

    else:
        print('No model with this name, check this and retry')
        model = pickle.load(open(file_path, "rb"))

    return model