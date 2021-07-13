def _getAnalysisModule(oDesign):
    return oDesign.GetModule("AnalysisSetup")

def GetSetups(oAnalysis):
    setups = oAnalysis.GetSetups()
    return setups

def GetSetupCount(oAnalysis):
    cnt = oAnalysis.GetSetupCount()
    return cnt

def GetSweeps(oAnalysis):
    sweeps = oAnalysis.GetSweeps()
    return sweeps

def GetSweepCount(oAnalysis):
    cnt = oAnalysis.GetSweepCount()
    return cnt