from past.builtins import execfile

# import random
# seeds = random.sample(range(10000, 10**5), 5)
# print(seeds)
# 962, 274, 2, 238, 589, 469, 497, 725, 894, 988, 733, 219, 164, 315, 161


seeds = [962, 274, 2, 238, 589, 469, 497, 725, 894, 988, 733, 219, 164, 315, 161]
stds = [.6 ] # .2, .3
d_vector = [1,2, 3, 4]

for seed in seeds:
    for d in d_vector:
        for std in stds:
            n_train = 2**d
            if n_train > 8:
                n_train = 8
            print(seed, d, n_train, std)
            execfile('quantum_ensemble.py')

