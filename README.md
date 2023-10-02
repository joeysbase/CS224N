# CS224N Assignments Code Solution
## Model performances report
### Dependency parser
* 
* 
* 
### LSTM CH2EN translator
* Training process seems to run into plateau, and training loss stop decreasing at 55 with perplexity around 12
* Model eventually achieved BLEU of 7
* More training details are in notebook
* Trained model's parameters here -> [parameters](https://drive.google.com/file/d/1-7hvM6dTyKLmn4fWTNQrIWVYn3NdkOvW/view?usp=drive_link "click me")
### miniGPT
* Finetuning on a simple "birth place" question answering task without pretraining achieved 2.19% acc on dev, whereas a single line of code outputing "London" have achieved 5% in comparison
* Pretraining on collected wiki text incorporateing information regarding famous people before finetuning had achieved 24% acc on dev. Considerable improvement.
* Pretraining took about 42 mins on T4 GPU
* After adapating perceiver, training speed improved by 1 sec per epoch 
* Model's parameters can be accessed here -> [pretraining parameters](https://drive.google.com/file/d/1--EZNwVJNczNRy4-snouftcOScTHNZMj/view?usp=drive_link)
* More training details can be seen in notebook
