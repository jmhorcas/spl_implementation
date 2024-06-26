import os
import argparse
import csv
from typing import Any

import jinja2

from spl_implementation.utils import utils
from spl_implementation.models import VEngine

# CONSTANTS
CASE_STUDY = 'icecream'
BASE_PATH  = os.path.join('evaluation', 'case_studies')
FM_MODEL_PATH = os.path.join(BASE_PATH, CASE_STUDY, 'fm_models', f'{CASE_STUDY}_fm.uvl')
CONFIGURATION_PATH = os.path.join(BASE_PATH, CASE_STUDY, 'configurations', f'{CASE_STUDY}_fm_cone.uvl.json')
TEMPLATE_PATH = os.path.join(BASE_PATH, CASE_STUDY, 'templates', f'{CASE_STUDY}_template.txt.jinja')
MAPPING_MODEL_PATH = os.path.join(BASE_PATH, CASE_STUDY, 'mapping_models', f'{CASE_STUDY}_mapping.csv')


if __name__ == '__main__':
    # parser = argparse.ArgumentParser(description='Variability resolution with Jinja templates.')
    # parser.add_argument('-c', '--configs', dest='configs_dir', type=str, required=True, 
    #                     help='Directory with the configurations files (.json).')
    # parser.add_argument('-t', '--template', dest='template_file', type=str, required=True, 
    #                     help='Template file (.jinja) over which the variability is resolved.')
    # parser.add_argument('-m', '--mapping', dest='mapping_file', type=str, required=True, 
    #                     help='File with the mapping between the variation points and the templates (.csv).')
    # args = parser.parse_args()

    # # Get parameters
    # configurations_files = utils.get_filepaths(args.configs_dir, ['.json'])
    # template_file = args.template_file
    # mapping_file = args.mapping_file

    # print('CONFIGURATION FILES:')
    # for i, config_file in enumerate(configurations_files, 1):
    #     print(f'|-{i}: {config_file}')
    # if not configurations_files:
    #     print('|-Warning: No configurations files detected. Use a folder with .json files.')
    
    # print('TEMPLATE FILES:')
    # if template_file.endswith('.jinja'):
    #     print(f'|-{template_file}')
    # else:
    #     print('|-Error: Wrong template file extension. Use a .jinja file.')

    # print('MAPPING MODEL:')
    # if mapping_file.endswith('.csv'):
    #     print(f'|-{mapping_file}')
    # else:
    #     print('|-Error: Wrong mapping model file extension. Use a .csv file.')

    fm_model_path = FM_MODEL_PATH
    configuration_path = CONFIGURATION_PATH
    template_path = TEMPLATE_PATH
    mapping_model_path = MAPPING_MODEL_PATH
    vengine = VEngine()
    vengine.load_configuration(configuration_path)
    vengine.load_mapping_model(mapping_model_path)
    vengine.load_template(template_path)
    result = vengine.resolve_variability()
    print(result)