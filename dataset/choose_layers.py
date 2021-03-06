import sys, os
import subprocess
import shlex

if len(sys.argv) != 4:
    print "This script requires three command line arguments: a model name, a .txt file listing convolutional layers, and a dataset name"
else:
    models = {"googlenet": 'googlenet_mil-type_adagrad-lr_policy_fixed-iter_400000', "alexnet": 'caffe_reference_places365'}
    model = models[sys.argv[1]]
    datasets = {"ddsm": 'dataset/ddsm', "broden": 'dataset/broden1_227'}
    dataset = datasets[sys.argv[3]]

    with open(sys.argv[2], 'r') as input_file:
        all_layers = [word for line in input_file for word in line.split()]
        for i in range(len(all_layers)):
            try:
                my_layers = all_layers[i:i+3]
            except IndexError:
		my_layers = all_layers[i::]
            
            my_layers = ' '.join(my_layers) 

            try: 
                print "Beginning run"
                subprocess.call(shlex.split('nohup script/rundissect.sh --model ' + model + ' --layers  "' + my_layers + '" --dataset ' + dataset + ' --resolution 227 &'))
                print "Run complete"
            except:
                print "Failed run"

