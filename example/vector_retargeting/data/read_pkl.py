import pickle

with open("allegro_joints.pkl", "rb") as f:
    data = pickle.load(f)

print(data)
