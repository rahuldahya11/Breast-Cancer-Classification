import os

INPUT_DATASET = 'Dataset'

BASE_PATH = "Datasets/idc"
TRAIN_PATH = os.path.sep.join([BASE_PATH, "training"])
VAL_PATH = os.path.sep.join([BASE_PATH, "validation"])
TEST_PATH = os.path.sep.join([BASE_PATH, "test"])

TRAIN_SPLIT = 0.8
VAL_SPLIT = 0.1