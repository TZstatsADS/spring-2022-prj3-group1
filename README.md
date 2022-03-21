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
	+ For model 1, we first built predicting models including Mobilnet, ResNet, CNN, and Vision Transformer to compare the running time and the validation accuracy. Taking the noisy labels as clean ones, the sophisticated models performed relatively better than the baseline model. \
	  ResNet showed that the validation accuracy was 45.76%, which is pretty higy, but it took about 155 mins to run which failed to meet our requirement of 30 mins limit. \
	  The vision transformer model provided 43.86% accuracy with 1 min's running time. \
	  As for CNN, the validation accuracy was 43.36% with 12 mins' running time. \
	  The model with the best performance was Mobilenet, which led to 60.34% accuracy with 13.32 mins' running time. \
          Therefore, we chose Mobilenet as our final decision of model 1. 
	+ For model 2,
	
- Contribution statement: 
	+ All team members contributed to building and testing the model 1. Aakanksha built the VGG19 model. Kexin built the ResNet model. Kaimin built the vision transformer model. Xinran first built the full layer CNN model, and Lichun and Kexin further worked on improving and testing the CNN model.
	+ Aakanksha developed the weakly supervised data cleaning model, and Xinran (and Jessi?) also worked on developing another model 2 to further get the final choice. All team members contributed to improving and testing the model 2.
	+ Kaimin initially updated the README, and was later edited by Kexin. 
        

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
