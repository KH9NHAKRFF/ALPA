# ALPA text classification
## Requirements
We conducted experiments in the torch 1.10.1 environment. This environment with requirements is available at: 
```bash
conda env create -f alpa_glue.yaml
```
And then, install ALPA at [alpa](https://github.com/KH9NHAKRFF/ALPA).

## Finetune models 
### Benchmark accuracy
```bash
python run_glue.py --model_name_or_path ARCH
--task_name TASK --max_length 128 --per_device_train_batch_size 16 --per_device_eval_batch_size 128 --learning_rate 5e-5 --num_train_epochs 3 --pad_to_max_length  --output_dir log/TASK/LEVEL/ --alpa --bit BIT
```
The choices for TASK are {cola, mnli, mrpc, qnli, qqp, rte, sst2, stsb, wnli}. 

The choices for ARCH are defined in huggingface.co/models. In the paper, we experiment with ```distilbert-base-uncased```, ```bert-base-cased```, and ```bert-large-cased```.

To apply apla, add ```--alpa``` and ```--bit BIT```, choosing a average bit of activations. In the paper, we experimented with (2, 1.5, 1).

### Benchmark memory
Add `--get-mem` to the end of the command. For example, to get the training memory of auto precision 4 bit on bert-large-cased sst2 dataset, run the following command:
```bash
python run_glue.py --model_name_or_path ARCH
--task_name TASK --max_length 128 --per_device_train_batch_size 16 --per_device_eval_batch_size 128 --learning_rate 5e-5 --num_train_epochs 3 --pad_to_max_length  --output_dir log/TASK/LEVEL/ --alpa --bit BIT --get-mem
```







