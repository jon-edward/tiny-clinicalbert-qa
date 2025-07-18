base_model_name=nlpie/tiny-clinicalbert

# Quick train/eval for debugging. Use with --test flag
if [[ $* == *--test* ]]; then
  extra_args=(--max_train_samples 100 --max_eval_samples 100)
else
  extra_args=()
fi

dataset_location=./generated_dataset

python ./tiny_clinicalbert_qa/generate_dataset.py ${dataset_location}

python ./tiny_clinicalbert_qa/run_qa.py \
  --model_name_or_path ${base_model_name} \
  --dataset_name ${dataset_location} \
  --version_2_with_negative \
  --per_device_train_batch_size 16 \
  --learning_rate 3e-5 \
  --num_train_epochs 8 \
  --weight_decay 0.01 \
  --warmup_steps 500 \
  --num_train_epochs 5 \
  --max_seq_length 512 \
  --doc_stride 128 \
  --output_dir trained_model \
  --overwrite_output_dir \
  --save_strategy no \
  --do_train true \
  --do_eval true \
  --push_to_hub \
  --push_to_hub_token $(cat hub_token.txt) \
  --hub_model_id "jon-t/tiny-clinicalbert-qa" \
  --hub_dataset_names "Eladio/emrqa-msquad" "rajpurkar/squad_v2" \
  ${extra_args[@]}
