from cifar10_unlabled_utils  import (
    precompute_clip_cifar10_train_image_embeddings,
    precompute_clip_cifar10_unlabeled_image_embeddings,
    precompute_clip_cifar10_test_image_embeddings,
    precompute_clip_cifar10_text_embeddings,
    train_resnet18_zero_shot,
    train_resnet18_linear_probe
)

def f_name(f):
    return f.__name__

precompute_clip_cifar10_train_image_embeddings()
precompute_clip_cifar10_unlabeled_image_embeddings()
precompute_clip_cifar10_test_image_embeddings()
precompute_clip_cifar10_text_embeddings()
train_resnet18_zero_shot()
train_resnet18_linear_probe()

