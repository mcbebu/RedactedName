import numpy as np
from sklearn.cluster import AffinityPropagation
from k_means_constrained import KMeansConstrained
import matplotlib.pyplot as plt
import matplotlib.axes as axe
import csv
import os
from mapgenerator import generate_map

def k_means_constrained(file_path, min_orders, max_orders, num_drivers):

    data = []
    '''
    abstract 200 and 2 
    '''
    np_array = np.empty((200, 2))

    with open(file_path, mode='r') as file:
        rows = csv.reader(file, delimiter=',', quotechar ='"')
        for row in rows:
            if row[0] and row[1] :
                data.append([float(num) for num in row])
            
        np_array = np.asarray(data)

    propogator = KMeansConstrained (
        n_clusters = num_drivers,
        size_min = min_orders,
        size_max = max_orders,
        random_state = 0
    )
    propogator.fit_predict(np_array)

    return np_array, propogator.cluster_centers_ ,propogator.labels_


def return_path(image_path) :
    dirname = os.path.abspath("")
    image_path = os.path.join(dirname, image_path)
    return image_path


def draw_proximity_plot(data, cluster_centers, labels, num_drivers) :

    t1 = cluster_centers[labels]
    print(t1)
    t2 = np.hstack((data, t1))
    print(t2)

    t3 = np.hstack((data,labels.reshape((labels.size, 1))))
    print(t3)
    t4 = np.arange(0, num_drivers)
    t5 = np.zeros((num_drivers, 2))
    for x in t4 :
        fil = t2[t3[:, 2] == x]
        print(fil)
        t5[x] = np.max(np.sqrt(np.sum(np.power(fil[:, :2] - fil[:, 2:], 2), axis = 1)), axis = 0)



    centrepoint = data.mean(axis = 0)
    generate_map(centrepoint,t3)
    #print(centrepoint)

    np.random.seed(12334232)
    colors = np.random.rand(num_drivers)

    plt.scatter(data[:, 0], data [:, 1], c = labels, marker = 'v') 
    plt.scatter(cluster_centers[:, 0], cluster_centers[:, 1], s = t5[:, 1].astype(float) * 1020000, c = colors, alpha = 0.5, label='cluster centers')
    plt.savefig(return_path("images\Proximity_Plot.png"), transparent= True)
    plt.show()



