import json
from tqdm import tqdm
import numpy as np


def get_labels(fname):
    """
    Gets label data from a geojson label file

    Args:
        fname: file path to an xView geojson label file

    Output:
        Returns three array: coords, chips, and classes corresponding to the
        coordinates, file names, and classe for each ground truth.
    """
    with open(fname) as f:
        data = json.load(f)

    coords = np.zeros((len(data['features']), 4))
    chips = np.zeros((len(data['features'])), dtype="object")
    classes = np.zeros((len(data['features'])))

    for i in tqdm(range(len(data['features']))):
        if data['features'][i]['properties']['bounds_imcoords'] != []:
            b_id = data['features'][i]['properties']['image_id']
            val = np.array([int(num) for num in data['features'][i]['properties']['bounds_imcoords'].split(",")])
            chips[i] = b_id
            classes[i] = data['features'][i]['properties']['type_id']
            if val.shape[0] != 4:
                print("Isssues at %d!" % i)
            else:
                coords[i] = val
        else:
            chips[i] = 'None'

    return coords, chips, classes
