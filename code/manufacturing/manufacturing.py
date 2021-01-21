import pandas as pd
import os
from pandasgui import show
import numpy as np

dfs = []

for p in os.listdir('.'):
    if p.startswith('exp'):
        d = pd.read_csv(p)
        d['Experiment'] = int(p.split('_')[1].split('.')[0])
        dfs.append(d)

df = pd.concat(dfs)

df['Machining_Process'] = df['Machining_Process'].replace(
    {
        'Layer 1 Up': "Layer 1",
        'Layer 1 Down': "Layer 1",
        'Layer 2 Up': "Layer 2",
        'Layer 2 Down': "Layer 2",
        'Layer 3 Up': "Layer 3",
        'Layer 3 Down': "Layer 3",
        'Repositioning': np.nan,
        'Starting': np.nan,
        'Prep': np.nan,
        'end': np.nan,
        'End': np.nan,
    })

df = df[df.Experiment.isin([1, 2])]
df = df.dropna(subset=['Machining_Process'])

df = df.rename(columns={
    "M1_CURRENT_FEEDRATE": "Feedrate",
    "S1_CommandAcceleration": "Acceleration",
    "Experiment": "Experiment",

    "M1_CURRENT_PROGRAM_NUMBER": "Test Program",
    "Machining_Process": "Process",

    "Y1_OutputPower": "Performance"
})

df.Acceleration[~df.Acceleration.isin([100,0])] = 50

final = df.pivot_table(index=["Experiment", "Feedrate", "Acceleration"],
                    columns=['Test Program', 'Process'],
                    values=['Performance'])
final = final.fillna(final.mean()).apply(lambda x: x + np.random.normal(x.mean(), 1, len(x)))
final.to_csv('manufacturing_multiindex.csv')