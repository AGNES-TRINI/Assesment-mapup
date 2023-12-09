#q-1 Car Matrix Generation
import pandas as pd

def generate_car_matrix(datasets):
    df = pd.read_csv(datasets)
    # pivot
    matrix_df = df.pivot(index='id_1', columns='id_2', values='car')
    matrix_df = matrix_df.fillna(0)
    # sets diagonal values to 0
    for i in matrix_df.index:
        matrix_df.at[i, i] = 0
    return matrix_df

dataset_path = 'C:\MapUp-Data-Assessment-F\datasets\dataset-1.csv'
result_matrix = generate_car_matrix(dataset_path)
print(result_matrix)

#q-2 Car Type Count Calculation
import pandas as pd
import numpy as np
def get_type_count(dataset):
    df = pd.read_csv(dataset)

    conditions = [
        (df['car'] <= 15),
        (df['car'] > 15) & (df['car'] <= 25),
        (df['car'] > 25)
    ]
    choices = ['low', 'medium', 'high']
    df['car_type'] = pd.Series(np.select(conditions, choices, default='Unknown'))

    # each car_type occurenc
    type_count = df['car_type'].value_counts().to_dict()
    type_count = dict(sorted(type_count.items()))
    return type_count

dataset_path = 'C:\MapUp-Data-Assessment-F\datasets\dataset-1.csv'
result_count = get_type_count(dataset_path)
print(result_count)

#q-3 Bus Count Index Retrieval
import pandas as pd

def get_bus_indexes(dataset):
    df = pd.read_csv(dataset)

    mean_bus = df['bus'].mean()
    bus_indexes = df[df['bus'] > 2 * mean_bus].index.tolist()
    bus_indexes.sort()
    return bus_indexes

dataset_path = 'C:\MapUp-Data-Assessment-F\datasets\dataset-1.csv'
result_indexes = get_bus_indexes(dataset_path)
print(result_indexes)

#q-4 Route Filtering
import pandas as pd
def filter_routes(dataset):
    df = pd.read_csv(dataset)

    # calculate the average value
    route_avg_truck = df.groupby('route')['truck'].mean()
    filtered_routes = route_avg_truck[route_avg_truck > 7].index.tolist()
    filtered_routes.sort()
    return filtered_routes

dataset_path = 'C:\MapUp-Data-Assessment-F\datasets\dataset-1.csv'
result_routes = filter_routes(dataset_path)
print(result_routes)

#q-5 Matrix Value Modification
def multiply_matrix(input_matrix):
    modified_matrix = input_matrix.copy()

    # multiply values
    modified_matrix[modified_matrix > 20] *= 0.75
    modified_matrix[modified_matrix <= 20] *= 1.25
    # round decimal
    modified_matrix = modified_matrix.round(1)
    return modified_matrix

modified_result_matrix = multiply_matrix(result_matrix)
print(modified_result_matrix)

#q-6 Time check
import pandas as pd

def verify_timestamps(dataset):
    # combine date and time columns
    dataset['start_timestamp'] = pd.to_datetime(dataset['startDay'] + ' ' + dataset['startTime'])
    dataset['end_timestamp'] = pd.to_datetime(dataset['endDay'] + ' ' + dataset['endTime'])

    dataset['start_day_of_week'] = dataset['start_timestamp'].dt.dayofweek
    dataset['end_day_of_week'] = dataset['end_timestamp'].dt.dayofweek
    dataset['start_time'] = dataset['start_timestamp'].dt.time
    dataset['end_time'] = dataset['end_timestamp'].dt.time

    completeness_check = (
        dataset.groupby(['id', 'id_2'])
        .apply(lambda group: (
            (group['start_day_of_week'].nunique() == 7) and
            (group['end_day_of_week'].nunique() == 7) and
            (group['start_time'].min() == pd.Timestamp('00:00:00').time()) and
            (group['end_time'].max() == pd.Timestamp('23:59:59').time())
        ))
    )

    return completeness_check

dataset_path = 'C:\MapUp-Data-Assessment-F\datasets\dataset-2.csv'
dataset = pd.read_csv(dataset_path)
completeness_result = verify_timestamps(dataset).reset_index().set_index(['id', 'id_2'])

print(completeness_result)
