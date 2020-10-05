def randomBiasedAI(utt):
    from ai import RandomBiasedAI
    return RandomBiasedAI()

def randomAI(utt):
    from ai import RandomBiasedSingleUnitAI
    return RandomBiasedSingleUnitAI()

def passiveAI(utt):
    from ai import PassiveAI
    return PassiveAI()

def workerRushAI(utt):
    from ai.abstraction import WorkerRush
    return WorkerRush(utt)

def lightRushAI(utt):
    from ai.abstraction import LightRush
    return LightRush(utt)