def _getAnalysisModule(oDesign):
    return oDesign.GetModule("AnalysisSetup")

def GetSetups(oAnalysis):
    return oAnalysis.GetSetups()

def GetSetupCount(oAnalysis):
    return oAnalysis.GetSetupCount()

def GetSweeps(oAnalysis):
    return oAnalysis.GetSweeps()

def GetSweepCount(oAnalysis):
    return oAnalysis.GetSweepCount()