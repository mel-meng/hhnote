import os
import pandas as pd



def load_result_csv(folder, run_name):
    """load csv exported from ICM into a dictionary

    Args:
        folder (string): folder path
        run_name (string): base name of the run

    Returns:
        dict: each item is csv file read into a dataframe
    """
    results = {}
    for f in os.listdir(folder):
        a, b = os.path.splitext(f)
        parts = a.split(run_name)
        if len(parts)==2:
            obj_type = parts[0].replace('_', '')
            p = parts[-1].replace('_', '')
            df = pd.read_csv(os.path.join(folder, f), parse_dates=True)
            df.index = df['Time']
            del df['Time']
            del df['Seconds']
            results['{}-{}'.format(obj_type, p)] = df
            # print('{}-{}'.format(obj_type, p))
    return results


def get_link_results(results, link_id, us_node_id, ds_node_id):
    """assemble a table for a link, similar to how you can show the results table for a link in ICM 

    Args:
        results (dictionary): results returned by the load_result_csv
        link_id (string): link id
        us_node_id (string): upstream id
        ds_node_id (string):downstream node id
    returns:
        dataframe: the results for the link
    """
    table = None
    for k, v in results.items():
        a, b = k.split('-')
        
        if table is None:
            col = v.columns[0]
            table = v.loc[:, [col]]

        if a == 'Link':
            fld = b
            table[fld] = v[link_id]
        else:
            if a == 'Node':
                us_node_fld = 'us_{}'.format(b)
                table[us_node_fld] = v[us_node_id]
                ds_node_fld = 'ds_{}'.format(b)
                table[ds_node_fld] = v[ds_node_id]
            else:
                print('not a valid type {}'.format(k))
                continue
    #     print(table)
    del table[col]
    return table
        
            
