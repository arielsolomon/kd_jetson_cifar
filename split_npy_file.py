import numpy as np
import os

root = '/Data/federated_learning/data/cifar10_c/'
file_path = os.path.join(root, os.listdir(root)[-7])
labels = True
def split_arr(file_path, root,labels=False):

    file = np.load(file_path)
    num_items = file.shape[0]
    frac_train, frac_test, frac_unlabeled = 0.15,0.05,0.8
    if not labels:
        arr_train, arr_test, arr_unlabeled = file[:int(frac_train*num_items),:,:,:],\
            file[int(frac_train*num_items):int(frac_train*num_items)+int(frac_test*num_items),:,:,:],\
            file[int(frac_train*num_items)+int(frac_test*num_items):,:,:,:]
        np.save(root+'train_X.npy',arr_train), np.save(root+'test_X.npy',arr_test), np.save(root+'unlabeled_X.npy',arr_unlabeled)
    else:
        file_path = os.path.join(root,'labels.npy')
        file = np.load(file_path)
        arr_train, arr_test = file[:int(frac_train*num_items)],\
            file[int(frac_train*num_items):int(frac_train*num_items)+int(frac_test*num_items)]
        np.save(root+'train_y.npy',arr_train), np.save(root+'test_y.npy',arr_test)
split_arr(file_path, root, True)

