# Project: Weakly supervised learning-- label noise and correction


### [Full Project Description](doc/project3_desc.md)

Term: Spring 2022

+ Team #1
+ Team members
	+ Aakanksha Agaewal
	+ Lichun He
	+ Kexin Tang
	+ Kaimin Wang
	+ Xinran Wang
	+ Jiaxin Yu

- Project summary: 
	+ For model 1, we first built predicting models including MobileNet, ResNet, CNN, and Vision Transformer to compare the running time and the validation accuracy. Taking the noisy labels as clean ones, the sophisticated models performed relatively better than the baseline model. \
	  ResNet showed that the validation accuracy was 45.76%, which is pretty high, but it took about 155 mins to train. \
	  The vision transformer model provided 43.86% accuracy. The model was trained 50 iterations, which took significantly longer time than the other ones.\
	  As for CNN, the validation accuracy was 43.36% with 12 mins' running time. \
	  The model with the best performance was MobileNet, which led to 60.34% accuracy with 13.32 mins' running time. \
          Therefore, we chose Mobilenet as our final decision of model 1. 
	+ For model 2, we have implemented the proposed model in [this](https://openaccess.thecvf.com/content_CVPR_2019/papers/Hu_Weakly_Supervised_Image_Classification_Through_Noise_Regularization_CVPR_2019_paper.pdf) paper using weakly supervised training through noise regularization. The model is consist of one clean net with clean labels and one residual net with noisy label. Both nets are sharing a common feature extractor through a state-of-art CNN classification model. The features will then be fed into both the networks. The residual net will work as a regularization term when training the clean net to assist clean net accuracy utilizing noisy labels.
	+ ![Model Structure](https://cdn.zhuanzhi.ai/images/wx/2ba6290f11e0725b5df22267cfc3a68e "Weakly Supervised Model")
	
- Contribution statement: 
	+ All team members contributed to building and testing the model 1. Aakanksha built the MobileNetV2 model. Kexin built the ResNet model. Kaimin built the vision transformer model. Xinran first built the full layer CNN model, when Lichun, Kexin and Kaimin further worked on improving and testing the CNN model.
	+ Aakanksha developed the weakly supervised data cleaning model, and Xinran also worked on developing another VGG16 model to further get the final choice. All team members contributed to improving and testing the model 2.
	+ Kaimin initially updated the README, and was later edited by Kexin. 
	+ Presentation for this project was made by Jessie and Aakanksha, with inputs from the entire team.
        

Following [suggestions](http://nicercode.github.io/blog/2013-04-05-projects/) by [RICH FITZJOHN](http://nicercode.github.io/about/#Team) (@richfitz). This folder is orgarnized as follows.

```
proj/
├── lib/
├── data/
├── doc/
├── figs/
└── output/
```

Please see each subfolder for a README file.
