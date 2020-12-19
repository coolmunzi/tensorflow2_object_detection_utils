This repo contains utility scripts that will be useful during data processing for tensorflow object detection model training.

There are 3 scripts in the repo:
1. **generate_labelmap.py**: Script to convert txt based class names to labelmap of pbtxt type.
    
     Usage: `python generate_labelmap.py -i {Path to class-names.txt file} -o {Path where output labelmap file should be saved}`
     
     Example: `python generate_labelmap.py -i ./class-names.txt -o ./labelmap.pbtxt`
2. **generate_csv.py**: Script to generate a combined csv file from Pascal VOC based xml files
    
     Usage: `python generate_csv.py -x {Path to directory containing xml file} -o {Path where output csv file should be saved}`
 
     Example: `python generate_csv.py -x ./annotations/ -o ./output_csv.csv`
   
2. **generate_tfrecord.py**: Script to generate a tfrecord file from csv file
    
     Usage: `python generate_tfrecord.py --csv_input {Path to combined csv file} --image_dir {Path to directory containing jpg or png image dataset} --output_path {Path of the output tfrecord file should be stored} --class_path {Path of the txt file containing names of classes}`
 
     Example: `python generate_tfrecord.py --csv_input ./class-names.txt --image_dir ./images/ --output_path ./data.tfrecord --class_path ./class-names.txt`
