import pandas as pd

simple_list = ['Sam', 'Bob', 'Joe', 'Mary', 'Sue', 'Sally']

named_column = {'Name': simple_list,
                'Favorite Color': ['Blue', 'Red', 'Green', 'Blue', 'Red', 'Green'],
                'Favorite Food': ['Italian', 'Mediterranean', 'Thai', 'Chinese', 'Mexican', 'Spanish']}

pd.set_option('display.max_columns', None)
pd.set_option('display.expand_frame_repr', False)

data = pd.DataFrame(named_column)

formula_result = []
for i in range(len(data)):
    formula_result.append(f'{data.iloc[i]["Name"]} likes {data.iloc[i]["Favorite Food"]}'
                          f' food and the color {data.iloc[i]["Favorite Color"]}')

data['About Me'] = formula_result

print(data)
