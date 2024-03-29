# This scripts contains all the default training parameters pre-set for model training.
# Description about all the required parameters for training is mentioned below.

"""
All the recognition models available:

keras_models= ['xception', 'vgg16', 'vgg19', 'resnet50', 'inceptionv3',
                'inceptionresnetv2', 'nasnet_small','nasnet_large',
                'densenet121', 'densenet169', 'densenet201', 'mobilenet']
"""

#####################################   Essential Model Training parameters   ##########################################

# This is an identifier for training iteration name. This will be used as prefix to model logs folder.
# If not mentioned name of model logs folder will be same as "model name" used for training.
# REMEMBER TO CHANGE THIS NAME DURING DIFFERENT MODEL TRAINING ITERATIONS (of the same model).
ITERATION_NAME = "cats_n_dogs"

# path to training and validation directory
# path to training directory. Classes wise folders of images
TRAIN_DIR = "/Users/sanjyotzade/Documents/datasets/cats_n_dogs/Train"

# path to validation directory. Classes wise folders of images
VALID_DIR = "/Users/sanjyotzade/Documents/datasets/cats_n_dogs/Val"

# Initializing model parameters
IMG_WIDTH = None  # if None, default input image width as per model will be used

IMG_HEIGHT = None  # if None, default input image height as per model will be used

MODEL_NAME = "mobilenet"  # specify the model name from above list

# if "imagenet" then imagenet trained weight initialization is used for the model.
# However, in order to re-start training weights path can be specified here.
WEIGHTS = None  # ["imagenet", None, <path-to-intermediate-saved-weights>]

SAVE_LOCATION = "./"  # path to folder where model weights and logs will be saved

EPOCHS = 3  # number of epochs to train

BATCH_SIZE = 32  # batch size of training

# START_TRAINING parameter is mostly utilised to check pre-modeling parameters and model architecture check.
START_TRAINING = True  # if False, model summary & pre-training parameters will be displayed. "True" to start training.

POST_EVALUATION = True  # if False, post-training evaluation(elaborated in READ.ME) will be not be done.

TRAINING_TYPE = "train_all"
# There are three modes of training available:
# ["train_all","freeze_some","freeze_all"]
"""
Model is created by using architecture from keras application model and adding 2 extra dense layer on top of it. 

1. "train_all":
    This mode trains all the  model layers as well as added 2 dense layers. 

2. "freeze_some":
    This mode will freeze some of the layers in model(number of layers to freeze can be specified). 
    Rest of the  model layers and  2 dense layers will be trained. 

3. "freeze_all":
    None of the model layers will be trained. Only added last 2 dense layers will be trained.
"""

#  All the essential parameters can also be passed as run_time argument as mentioned in README


######################################   Advanced Model Training Parameters   ##########################################

# Number of initial layers to freeze in an model
NUMBER_OF_LAYERS_TO_FREEZE = 70  # if TRAINING_TYPE = "freeze_some"

# Available loss functions for categorical classification
#
# Best practices for loss usage
# Multi-Class Classification Loss Functions
# ["categorical_crossentropy", "sparse_categorical_crossentropy", "kullback_leibler_divergence"]
#
# Binary Classification Loss Functions (two classes)
# ["binary_crossentropy", "hinge", "squared_hinge"]
#
# other losses
# ["categorical_hinge", "logcosh", "poisson", "cosine_proximity", ]
#
# Note:
# 1. When using the sparse_categorical_crossentropy loss, your targets should be integer targets.
LOSS = "categorical_crossentropy"

# Available optimizers for categorical classification
#
# ["sgd", "adam", "adagrad", "adadelta", "rmsprop", "nadam"]
# Note: default parameters for optimizers will be used
OPTIMIZER = "sgd"

# Number of fully connected layers to add after pre-trained model
# As many values in NUM_NODES that many fully connected layers will be added after pre-trained model
# "NUM_DROPOUTS" specifies number of dropouts after each fully connected layers
# LENGTH OF NUM_NODES should be equal to LENGTH OF NUM_DROPOUTS (i.e dropout values w.r.t to each layer)
NUM_NODES = [1024, 512]  # This default value will add 2 fully connected layers with 1024, 512 nodes respectively.
NUM_DROPOUTS = [0.5, 0.5]  # This default value will add 2 dropout layers after each fully connected layer.

# To introduce early stopping
EARLY_STOPPING = False  # if "EARLY_STOPPING = True", below parameters.
ES_MONITOR = 'val_accuracy'  # either of ["val_accuracy", "val_loss"]
ES_MIN_DELTA = 0
ES_PATIENCE = 8
ES_VERBOSE = 1
ES_MODE = 'auto'
ES_RESTORE_BEST_WEIGHTS = True
# Arguments
# - ES_MONITOR: quantity to be monitored.
# - ES_MIN_DELTA: minimum change in the monitored quantity to qualify as an improvement,
#   i.e. an absolute change of less than min_delta, will count as no improvement.
# - ES_PATIENCE: number of epochs with no improvement after which training will be stopped.
# - ES_VERBOSE: verbosity mode.
# - ES_MODE: one of {auto, min, max}. min mode, training will stop when the quantity monitored has stopped decreasing;
#   in max mode it will stop when the quantity monitored has stopped increasing; in auto mode, the direction is
#   automatically inferred from the name of the monitored quantity.
# - ES_RESTORE_BEST_WEIGHTS: whether to restore model weights from the epoch with best value of the monitored quantity.
#   If False, the model weights obtained at the last step of training are used.

# Which value to be monitored for weight saving
SAVING_METRIC = "val_accuracy"  # either of ["val_accuracy", "val_loss"]

# Data Augmentation
HORIZONTAL_FLIP = True
ROTATION_RANGE = 30

# model training verbose parameters
# This parameters controls is model training logs are to printed during training
VERBOSE = 1  # Integer. 0, 1, or 2. Verbosity mode. 0 = silent, 1 = progress bar, 2 = one line per epoch.

# To show final model training plot as a graph
# This graph will also be saved in model repository
SHOW = False  # if True, after model training, graph will be displayed

# POST EVALUATION THRESHOLD
HOW_MANY_WEIGHTS_TO_TEST = 5  # How many best weights are to be evaluated for post-training analysis

# accuracy range (0,1]
ACCURACY_THRESHOLD = 0.8  # Accuracy above which predictions will be considered correct, for precision-recall calc.

# Not applicable parameter
# CLEAR_LOGS = True  # if True, will clear model training logs & weights from the folder
# Note: if re-starting model training the make sure that earlier weights are preserved by keeping "CLEAR_LOGS=False"
# Note: when re-starting model training with "CLEAR_LOGS=True".
#       1. If restarting from earlier saved weights those weights will not be deleted, everything else will be deleted
#       2. If restarting model training from beginning then everything in the folder will be deleted.
# Note: Model logs are only delete as per model name. If training a model with new name & "CLEAR_LOGS=True" then
#       then weights & logs other earlier model name will not be deleted.
