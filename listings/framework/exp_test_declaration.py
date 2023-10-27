EXPERIMENTS = [
    Experiment("wordnet_general", "WN18RR", ["TransE_l2","ComplEx"],200),
    Experiment("specific_rel_FB", "FB15K-237", ["TransE_l2"], 100, True, relation = "relation_name")
]

TESTS = [
    Test("wordnet_transE", "wordnet_general", ["TransE_l2"], 5000),
    Test("wordnet_complEx", "wordnet_general", ["ComplEx"], 10000),
    Test("FB_specific", "specific_rel_FB", ["TransE_l2"], 400),
]