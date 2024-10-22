export PYTHONIOENCODING=utf-8
export OMP_NUM_THREADS=16

id=$1
ranking_len=$2
CUDA_VISIBLE_DEVICES=2,3 accelerate launch infer_and_eval_main_generate.py \
    --index $id \
    --stage $ranking_len
    #--stage $ranking_len > ../logs/generate_infer_main_${id}_${ranking_len}.log 2>&1

CUDA_VISIBLE_DEVICES=2,3 accelerate launch  infer_and_eval_main_reward.py \
    --index $id \
    --stage $ranking_len
    #--stage $ranking_len > ../logs/reward_infer_main_${id}_${ranking_len}.log 2>&1

CUDA_VISIBLE_DEVICES=2,3 python -u infer_and_eval_main_score.py \
    --index $id \
    --stage $ranking_len
    #--stage $ranking_len > ../logs/score_infer_main_${id}_${ranking_len}.log 2>&1