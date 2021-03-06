import os
import glob
import pandas as pd
import xml.etree.ElementTree as ET
import argparse


def xml_to_csv(path):
    xml_list = []
    for xml_file in glob.glob(path + '/*.xml'):
        tree = ET.parse(xml_file)
        root = tree.getroot()

        for member in root.findall('object'):
            value = (root.find('filename').text,
                     int(root.find('size').find('width').text),
                     int(root.find('size').find('height').text),
                     member[0].text,
                     int(member.find("bndbox").find('xmin').text),
                     int(member.find("bndbox").find('ymin').text),
                     int(member.find("bndbox").find('xmax').text),
                     int(member.find("bndbox").find('ymax').text)
                     )

            xml_list.append(value)
    column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
    xml_df = pd.DataFrame(xml_list, columns=column_name)
    return xml_df


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-x', '--xml', required=True, help='Path to directory containing annotations (xml files)')
    parser.add_argument('-o', '--output', required=True,
                        help='Path to output csv file')
    args = vars(parser.parse_args())

    xml_path = args['xml']
    xml_df = xml_to_csv(xml_path)
    xml_df.to_csv(args['output'] , index=None)
    print('Successfully converted xml to csv.')


main()
