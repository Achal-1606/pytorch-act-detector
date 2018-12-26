import os
import os.path as osp
import sys


def add_path(path):
    if path not in sys.path:
        sys.path.insert(0, path)


root_dir = osp.abspath(osp.join(osp.dirname(__file__), '..', '..'))


class Config:
    # -------------------------data config ------------------------------#
    dataset = 'UCF101v2'
    # dataset = 'UCFSports'
    if dataset == 'UCF101v2':
        data_path = "/mnt/data/qzw/data/UCF101/"
    elif dataset == 'UCFSports':
        data_path = "/mnt/data/qzw/data/UCFSports/"
    else:
        print("dataset not found!!")
        exit(0)

    modality = 'rgb'
    init_model = "/mnt/data/qzw/model/pytorch-act-detector/{}/{}-init-model-{}-pytorch-single.pkl".format(dataset, dataset, modality)
    trained_model = "/mnt/data/qzw/model/pytorch-act-detector/{}/my_trained_pytorch_model_{}-{}.pkl".format(dataset, dataset, modality)
    new_trained_model = "/mnt/data/qzw/model/pytorch-act-detector/{}/my_new_trained_pytorch_model_{}-{}.pkl".format(dataset, dataset, modality)
    best_trained_model = "/mnt/data/qzw/model/pytorch-act-detector/{}/my_best_trained_pytorch_model_{}-{}.pkl".format(dataset, dataset, modality)

    variance = [0.1, 0.1, 0.2, 0.2]
    sequence_length = 6

    # -------------------------model config ------------------------------#

    base_model_name = 'vgg16'
    freeze_init = False

    # -------------------------train config ------------------------------#
    reinit_all = True
    use_gpu = True
    warm_up_epoch = 3
    warm_up_ratio = 1 / 10
    epochs = 200
    train_batch_size = 256
    valid_batch_size = 1
    workers = 16

    lr = 0.001
    momentum = 0.9
    weight_decay = 5e-4

    os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
    os.environ["CUDA_VISIBLE_DEVICES"] = "0,1"


config = Config()