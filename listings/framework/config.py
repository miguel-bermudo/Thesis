config = {
    "available_cores": 8,
    "gpu_acceleration": True,
    "multithreaded_dist_reward": False, 
    "verbose": False, 
    "log_results": False,
    "debug": False, 
    "print_layers": False, 
    "restore_agent": False, 
    "guided_reward": True, 
    #"distance","terminal","embedding","shaping"
    "guided_to_compute":["terminal", "embedding"],
    "regenerate_embeddings":False,
    "normalize_embeddings":False,
    "use_LSTM": True,
    "use_episodes": False, 
    "episodes":0, 

    "alpha": 0.9, # [0.8-0.99] PPO prev step NN learning rate
    "gamma": 0.99, # [0.90-0.99] decay rate of past observations 
    "learning_rate": 1e-3, #[1e-3, 1e-5] NN learning rate.

    "activation":'leaky_relu', # relu, prelu, leaky_relu, elu, tanh
    "regularizers":['kernel'], #"kernel", "bias", "activity" 
    "algorithm": "PPO", #BASE, PPO
    "reward_type": "simple", # retropropagation, simple

    # "probability", "max"
    "action_picking_policy":"probability",

    #"max_percent", "one_hot_max", "straight"
    "reward_computation": "one_hot_max", 

    "path_length":3,
    "random_seed":True,
    "seed":0
}