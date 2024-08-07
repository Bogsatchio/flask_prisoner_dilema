
def get_population_evolution_query(experiment_id):
    return f"""
    select w.waveId, w.playerId, p.name, p.strategyType, p.strategyTemper
    from waveresult as w
    left join players as p
    on w.playerId = p.playerId
    where p.experimentId = '{experiment_id}'
    """

