#q-1 Distance Matrix Calculation
import pandas as pd
def calculate_distance_matrix(dataset):
    df = pd.read_csv(dataset)
    locations = pd.concat([df['id_start'], df['id_end']]).unique()
    locations.sort()
    distance_matrix = pd.DataFrame(index=locations, columns=locations)

    distance_matrix.values[[range(len(locations))]*2] = 0

    # Populate the distance matrix with cumulative distances
    for _, row in df.iterrows():
        id_start, id_end, distance = row['id_start'], row['id_end'], row['distance']

        if pd.notna(distance_matrix.at[id_start, id_end]):
            distance_matrix.at[id_start, id_end] = min(distance_matrix.at[id_start, id_end], distance)
            distance_matrix.at[id_end, id_start] = min(distance_matrix.at[id_end, id_start], distance)
        else:
            distance_matrix.at[id_start, id_end] = distance
            distance_matrix.at[id_end, id_start] = distance

    # Use Floyd-Warshall algorithm to calculate cumulative distances(reffered ChatGPT)
    for k in locations:
        for i in locations:
            for j in locations:
                if pd.notna(distance_matrix.at[i, k]) and pd.notna(distance_matrix.at[k, j]):
                    if pd.isna(distance_matrix.at[i, j]) or distance_matrix.at[i, k] + distance_matrix.at[k, j] < distance_matrix.at[i, j]:
                        distance_matrix.at[i, j] = distance_matrix.at[i, k] + distance_matrix.at[k, j]
                        distance_matrix.at[j, i] = distance_matrix.at[i, j]

    return distance_matrix

dataset_path = 'C:\MapUp-Data-Assessment-F\datasets\dataset-3.csv'
result_distance_matrix = calculate_distance_matrix(dataset_path)
print(result_distance_matrix)
#q-2 Unroll Distance Matrix
import pandas as pd
from itertools import product

def unroll_distance_matrix(dataset_path):
    # Create an empty list to store the result
    result_data = []

    # Iterate over unique combinations of id_start and id_end
    for id_start, id_end in product(dataset_path['id'], repeat=2):
        # Skip same id_start and id_end combinations
        if id_start != id_end:
            # Extract the distance value from the input DataFrame
            distance = dataset_path.loc[dataset_path['id'] == id_start, id_end].values[0]
            
            # Append the values to the result list
            result_data.append({'id_start': id_start, 'id_end': id_end, 'distance': distance})

    # Create a DataFrame from the result list
    result_df = pd.DataFrame(dataset_path)

    return result_df

result_dataframe = unroll_distance_matrix(dataset_path)
print(result_dataframe)

def find_ids_within_ten_percentage_threshold(df, reference_id)->pd.DataFrame():
    """
    Find all IDs whose average distance lies within 10% of the average distance of the reference ID.

    Args:
        df (pandas.DataFrame)
        reference_id (int)

    Returns:
        pandas.DataFrame: DataFrame with IDs whose average distance is within the specified percentage threshold
                          of the reference ID's average distance.
    """
    # Write your logic here

    return df

#q-4 Calculate Toll Rate
import pandas as pd

def calculate_toll_rate(dataset_path):
    result_df = dataset_path.copy()
    rate_coefficients = {'moto': 0.8, 'car': 1.2, 'rv': 1.5, 'bus': 2.2, 'truck': 3.6}

    for vehicle_type, rate_coefficient in rate_coefficients.items():
        column_name = f'{vehicle_type}_rate'
        result_df[column_name] = result_df['distance'] * rate_coefficient

    return result_df
result_dataframe = calculate_toll_rate(dataset_path)
print(result_dataframe)



def calculate_time_based_toll_rates(df)->pd.DataFrame():
    """
    Calculate time-based toll rates for different time intervals within a day.

    Args:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame
    """
    # Write your logic here

    return df
