#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from torchvision.datasets import VisionDataset
import numpy as np
import cv2
from typing import Optional, Callable, Tuple, Any
import random
from PIL import Image

class myCIFAR10(VisionDataset):
    """
    Args:
        root (string): Root directory of dataset where directory
            ``cifar-10-batches-py`` exists or will be saved to if download is set to True.
        train (bool, optional): If True, creates dataset from training set, otherwise
            creates from test set.
        transform (callable, optional): A function/transform that takes in an PIL image
            and returns a transformed version. E.g, ``transforms.RandomCrop``
        target_transform (callable, optional): A function/transform that takes in the
            target and transforms it.
    """

    def __init__(
            self,
            root: str,
            train: bool = True,
            transform: Optional[Callable] = None,
            target_transform: Optional[Callable] = None,
            only_noisy = True,
            only_clean = False,
            train_size = 0.7,
    ) -> None:

        super(myCIFAR10, self).__init__(root, transform=transform,
                                      target_transform=target_transform)
        
        file_path = "C:/Users/aakan/OneDrive/Documents/Spring 2022/Applied Data Science/GitHub/spring-2022-prj3-group1/data/"

        self.train = train  # training set or test set
        
        n_img = 50000
        n_noisy = 40000
        n_clean_noisy = n_img - n_noisy
        imgs = np.empty((n_img,32,32,3))
        for i in range(n_img):
            img_fn = f'C:/Users/aakan/OneDrive/Documents/Spring 2022/Applied Data Science/GitHub/spring-2022-prj3-group1/data/images/{i+1:05d}.png'
            imgs[i,:,:,:] = cv2.cvtColor(cv2.imread(img_fn),cv2.COLOR_BGR2RGB)
            print(i,end="\r")

        # load the labels
        clean_labels = np.genfromtxt(file_path+'clean_labels.csv', delimiter=',', dtype="int8")
        noisy_labels = np.genfromtxt(file_path+'noisy_labels.csv', delimiter=',', dtype="int8")
        
        # The class-label correspondence
        self.classes = ('plane', 'car', 'bird', 'cat',
                   'deer', 'dog', 'frog', 'horse', 'ship', 'truck')
        
        if only_clean:
            self.data = imgs[:n_clean_noisy]
            self.targets = clean_labels[:n_clean_noisy]
            self.noisy_targets = noisy_labels[:n_clean_noisy]
        else:
            self.data = imgs
            self.targets = noisy_labels
        
        random.seed(42)
        
        indexes = np.arange(len(self.data))
        #random.shuffle(indexes)
        
        if train:
            self.data = self.data[indexes[:int(train_size*(len(indexes)))]]
            self.targets = self.targets[indexes[:int(train_size*(len(indexes)))]]
        else:
            self.data = self.data[indexes[int(train_size*(len(indexes))):]]
            self.targets = self.targets[indexes[int(train_size*(len(indexes))):]]

    def __getitem__(self, index: int) -> Tuple[Any, Any]:
        """
        Args:
            index (int): Index

        Returns:
            tuple: (image, target) where target is index of the target class.
        """
        img, target = self.data[index], self.targets[index]

        # doing this so that it is consistent with all other datasets
        # to return a PIL Image
        #img = Image.fromarray(img)

        if self.transform is not None:
            img = self.transform(img)

        if self.target_transform is not None:
            target = self.target_transform(target)

        return img, target


    def __len__(self) -> int:
        return len(self.data)


# In[ ]:





# In[ ]:





# In[ ]:




