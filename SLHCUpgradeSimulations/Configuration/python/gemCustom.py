import FWCore.ParameterSet.Config as cms
def customise2023(process):
  if hasattr(process,'digitisation_step') :
    process=customise_digitization(process)
  if hasattr(process,'L1simulation_step'):
    process=customise_L1Emulator2023(process)
  if hasattr(process,'validation_step'):
    process=customise_Validation(process)
  if hasattr(process,'dqmHarvesting'):
    process=customise_harvesting(process)
  return process

def customise_digitization(process):
  from SimMuon.GEMDigitizer.customizeGEMDigi import customize_digi_addGEM_muon_only
  process = customize_digi_addGEM_muon_only(process)
  process.simMuonGEMDigis.mixLabel = cms.string("mix")
  process.simMuonRPCDigis.digiModel = cms.string('RPCSimParam')
  #process.simMuonME0Digis.mixLabel = cms.string("mix")
  process.digitisation_step.remove(process.simMuonRPCDigis)
  return process

def customise_Validation(process):
  #process.load('Validation.MuonGEMHits.MuonGEMHits_cfi')
  process.load('Validation.MuonGEMHits.gemSimValid_cff')
  process.load('Validation.MuonGEMDigis.MuonGEMDigis_cfi')
  process.load('Validation.MuonGEMRecHits.MuonGEMRecHits_cfi')
  process.genvalid_all += process.gemSimValid
  process.genvalid_all += process.gemDigiValidation
  process.genvalid_all += process.gemRecHitsValidation
  return process

def customise_harvesting(process):
  #process.load('Validation.MuonGEMHits.MuonGEMHits_cfi')
  process.load('Validation.MuonGEMHits.gemPostValidation_cff')
  process.genHarvesting += process.gemPostValidation
  return process

def customise_L1Emulator2023(process) :
  from L1Trigger.CSCTriggerPrimitives.cscTriggerPrimitiveDigis_cfi import cscTriggerPrimitiveDigis
  process.simCscTriggerPrimitiveDigis = cscTriggerPrimitiveDigis
  process.simCscTriggerPrimitiveDigis.clctSLHC.clctNplanesHitPattern = 3
  process.simCscTriggerPrimitiveDigis.clctSLHC.clctPidThreshPretrig = 2
  process.simCscTriggerPrimitiveDigis.clctParam07.clctPidThreshPretrig = 2

  ## ME21 has its own SLHC processors
  process.simCscTriggerPrimitiveDigis.alctSLHCME21 = process.simCscTriggerPrimitiveDigis.alctSLHC.clone()
  process.simCscTriggerPrimitiveDigis.clctSLHCME21 = process.simCscTriggerPrimitiveDigis.clctSLHC.clone()
  process.simCscTriggerPrimitiveDigis.alctSLHCME21.alctNplanesHitPattern = 3
  process.simCscTriggerPrimitiveDigis.alctSLHCME21.runME21ILT = cms.bool(True)
  process.simCscTriggerPrimitiveDigis.clctSLHCME21.clctNplanesHitPattern = 3
  process.simCscTriggerPrimitiveDigis.clctSLHCME21.clctPidThreshPretrig = 2
  return process
