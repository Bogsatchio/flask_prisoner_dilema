from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import seaborn as sns
import matplotlib.pyplot as plt
import os

mysql_user = os.getenv("MYSQL_USER")
mysql_pass = os.getenv("MYSQL_PASS")
#db_name = "simulation_dev"


def get_connection(db_name):
    connection_string = f"mysql+pymysql://homestead:secret@mysql:3306/{db_name}"
    engine = create_engine(connection_string)
    return sessionmaker(bind=engine)  # context manager for: (with Session() as session:)


def get_population_plots(df, experiment_id):
    os.makedirs(f"static/{experiment_id}", exist_ok=True)

    df_grouped = df.groupby(["waveId", "name"])["name"].count().reset_index(name='Count')
    plt.figure(figsize=(6, 3))
    ax = sns.lineplot(data=df_grouped, x='waveId', y='Count', hue='name', marker='.', linewidth=2.5)
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', prop={'size': 12}, )
    plt.xlabel('Wave', fontsize=11, labelpad=9)
    plt.ylabel('Count of players', fontsize=11, labelpad=9)
    plt.draw()
    plt.savefig(fr"static/{experiment_id}/players_evolution.svg", bbox_inches='tight')

    df_grouped = df.groupby(["waveId", "strategyType"])["strategyType"].count().reset_index(name='Count')
    plt.figure(figsize=(1.3, 0.7))
    sns.lineplot(data=df_grouped, x='waveId', y='Count', hue='strategyType', marker='.', linewidth=0.2)
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', prop={'size': 3})
    plt.xlabel('Wave', fontsize=3, labelpad=5)
    plt.ylabel('Count of players', fontsize=3, labelpad=5)
    plt.tick_params(axis='x', labelsize=2)
    plt.tick_params(axis='y', labelsize=2)
    plt.draw()
    plt.savefig(fr"static/{experiment_id}/types_evolution.svg", bbox_inches='tight')

    df_grouped = df.groupby(["waveId", "strategyTemper"])["strategyTemper"].count().reset_index(name='Count')
    plt.figure(figsize=(1.3, 0.7))
    sns.lineplot(data=df_grouped, x='waveId', y='Count', hue='strategyTemper', marker='.', linewidth=0.2)
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', prop={'size': 3})
    plt.xlabel('Wave', fontsize=3, labelpad=5)
    plt.ylabel('Count of players', fontsize=3, labelpad=5)
    plt.tick_params(axis='x', labelsize=2)
    plt.tick_params(axis='y', labelsize=2)
    plt.draw()
    plt.savefig(fr"static/{experiment_id}/tempers_evolution.svg", bbox_inches='tight')

