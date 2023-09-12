import splitfolders

splitfolders.ratio('inputs', # the input dataset location
    output="outputs", # the output train, validation and test folders output code
    seed=42, # The number of seed
    ratio=(.7, .2, .1), # The ratio of splited 70% for train, 20% for validation and 10% for test
    move=True # start moving the files
)

print('train, validation and test folders created successfully.')