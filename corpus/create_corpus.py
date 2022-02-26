import sys
sys.path.append('Utils')

import pandas as pd
import argparse
from Read_data import get_raw_data, unzip_texts

def create_dataset(phase_path, corpus_path, train=True):
    # Lectura de datos sin procesar
    if train == True:
        phase = 'train'
        p_labels, p_texts, _ = get_raw_data('{}parafrasis_entrenamiento.csv'.format(phase_path), 1)
        np_labels, np_texts, _ = get_raw_data('{}no_parafrasis_entrenamiento.csv'.format(phase_path), 0)
    else:
        phase = 'test'
        p_labels, p_texts, _ = get_raw_data('{}parafrasis_evaluacion.csv'.format(phase_path), 1)
        np_labels, np_texts, _ = get_raw_data('{}no_parafrasis_evaluacion.csv'.format(phase_path), 0)
    
    print('Fase: {}'.format(phase))
    print('------------------------------------------------')
    print('\tInstancias de paráfrasis: {}'.format(len(p_labels)))
    print('\tInstancias de no paráfrasis: {}'.format(len(np_labels)))
    print('Total = {}'.format(len(p_labels) + len(np_labels)))
    print('\n')
    
    # Creación de dataset
    df = pd.DataFrame()
    p_texts_1, p_texts_2 = unzip_texts(p_texts)
    np_texts_1, np_texts_2 = unzip_texts(np_texts)
    df['Text1'] = p_texts_1 + np_texts_1
    df['Text2'] = p_texts_2 + np_texts_2
    df['Label'] = p_labels + np_labels
    df = df.sample(frac=1).reset_index(drop=True)
    df.to_csv('{}parmex_{}.csv'.format(corpus_path, phase), encoding='utf8', index=False)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_path', help='ruta donde se encuentran los datos sin procesar')
    parser.add_argument('--output_path', help='ruta para guardar el corpus creado')
    parser.add_argument('--train', type=bool, default=False, help='indica si se crea corpus de entrenamiento o prueba')
    args = parser.parse_args()
    create_dataset(args.input_path, args.output_path, args.train)

if __name__ == '__main__':
    main()