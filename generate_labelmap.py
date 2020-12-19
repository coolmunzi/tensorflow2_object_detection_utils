import argparse
import os
parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', required=True, help='Path to txt file containing class names. For example ./class_names.txt')
parser.add_argument('-o', '--output', required=True, help='Path to output label map file. For example ./train_labelmap.pbtxt')

args = vars(parser.parse_args())

classnames_file = args['input']
protobuf_file = os.path.join(args['output'])

file  = open(classnames_file,'r')
output_dict ={}
classname = file.readline().strip()
count=1
while len(classname) >0 :
    output_dict[classname] = count
    classname = file.readline().strip()
    count+=1
file.close()

outfile = open(protobuf_file,'w+')
outfile.truncate(0)
for i in output_dict.keys():   
    outfile.write("item {\n"+"  id:"+ str(output_dict[i]) + '\n'+'  name:'+"'" +str(i)+"'" +'\n'+ "}\n")
outfile.close()

print("Successfully completed Label map file generation!!")