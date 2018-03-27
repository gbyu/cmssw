############################################################                                                                         
# define basic process                                                                                                               
############################################################                                                                         

import FWCore.ParameterSet.Config as cms
import os
process = cms.Process("L1PixelTrackNtuple")

GEOMETRY = "D17"

from Configuration.StandardSequences.Eras import eras

process = cms.Process('L1',eras.Phase2_timing)


############################################################                                                                         
# import standard configurations                                                                                                     
############################################################                                                                         
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('SimGeneral.MixingModule.mix_POISSON_average_cfi')
#process.load('Configuration.Geometry.GeometryExtended2023D4Reco_cff')
process.load('SimCalorimetry.HcalTrigPrimProducers.hcalTTPDigis_cff')
             
process.load('Configuration.StandardSequences.Services_cff')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.SimL1Emulator_cff')
process.load('Configuration.StandardSequences.L1TrackTrigger_cff')
process.load('Configuration.StandardSequences.DigiToRaw_cff')

if GEOMETRY == "D17":
    print "using geometry " + GEOMETRY + " (tilted)"
    process.load('Configuration.Geometry.GeometryExtended2023D17Reco_cff')
    process.load('Configuration.Geometry.GeometryExtended2023D17_cff')
elif GEOMETRY == "TkOnly":
    print "using geometry " + GEOMETRY + " (tilted)"
    process.load('L1Trigger.TrackTrigger.TkOnlyTiltedGeom_cff')
else:
    print "this is not a valid geometry!!!"

process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:upgradePLS3', '')


############################################################                                                                         
# input and output                                                 

process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(-1))

process.source = cms.Source("PoolSource",
   fileNames = cms.untracked.vstring('/store/relval/CMSSW_9_3_7/RelValSingleMuPt10/GEN-SIM-DIGI-RAW/93X_upgrade2023_realistic_v5_2023D17noPU-v2/10000/0EE7271D-9B2C-E811-B8EA-0025905A497A.root',
                                     ' /store/relval/CMSSW_9_3_7/RelValSingleMuPt10/GEN-SIM-DIGI-RAW/93X_upgrade2023_realistic_v5_2023D17noPU-v2/10000/C82F7851-9B2C-E811-95F0-0025905A611E.root',
                                     '/store/relval/CMSSW_9_3_7/RelValSingleMuPt10/GEN-SIM-DIGI-RAW/93X_upgrade2023_realistic_v5_2023D17noPU-v2/10000/EEC79D27-962C-E811-918D-0025905B8594.root',
                                     '/store/relval/CMSSW_9_3_7/RelValSingleMuPt10/GEN-SIM-DIGI-RAW/93X_upgrade2023_realistic_v5_2023D17noPU-v2/10000/F851E30C-9B2C-E811-9FD2-0CC47A7C353E.root',
                                     '/store/relval/CMSSW_9_3_7/RelValSingleMuPt10/GEN-SIM-DIGI-RAW/93X_upgrade2023_realistic_v5_2023D17noPU-v2/10000/0A598722-962C-E811-93E9-0CC47A7C354A.root',
                                     '/store/relval/CMSSW_9_3_7/RelValSingleMuPt10/GEN-SIM-DIGI-RAW/93X_upgrade2023_realistic_v5_2023D17noPU-v2/10000/229D1B19-9B2C-E811-B780-0025905B85D6.root',
                                     '/store/relval/CMSSW_9_3_7/RelValSingleMuPt10/GEN-SIM-DIGI-RAW/93X_upgrade2023_realistic_v5_2023D17noPU-v2/10000/C82F7851-9B2C-E811-95F0-0025905A611E.root',
                                     '/store/relval/CMSSW_9_3_7/RelValSingleMuPt10/GEN-SIM-DIGI-RAW/93X_upgrade2023_realistic_v5_2023D17noPU-v2/10000/26738BCE-962C-E811-9567-0CC47A7452D8.root',
                                     '/store/relval/CMSSW_9_3_7/RelValSingleMuPt10/GEN-SIM-DIGI-RAW/93X_upgrade2023_realistic_v5_2023D17noPU-v2/10000/504C20D7-962C-E811-BF76-0025905A60CE.root',
                                     '/store/relval/CMSSW_9_3_7/RelValSingleMuPt10/GEN-SIM-DIGI-RAW/93X_upgrade2023_realistic_v5_2023D17noPU-v2/10000/70C2D02C-962C-E811-88C9-0025905A611C.root',
                                     '/store/relval/CMSSW_9_3_7/RelValSingleMuPt10/GEN-SIM-DIGI-RAW/93X_upgrade2023_realistic_v5_2023D17noPU-v2/10000/7444AF73-9A2C-E811-A7EE-0025905AA9F0.root',
                                     '/store/relval/CMSSW_9_3_7/RelValSingleMuPt10/GEN-SIM-DIGI-RAW/93X_upgrade2023_realistic_v5_2023D17noPU-v2/10000/7A99A66C-9A2C-E811-91ED-0CC47A7C35A4.root',
                                     '/store/relval/CMSSW_9_3_7/RelValSingleMuPt10/GEN-SIM-DIGI-RAW/93X_upgrade2023_realistic_v5_2023D17noPU-v2/10000/88F15F1F-9B2C-E811-BD10-0025905A60FE.root'
   ),
   secondaryFileNames = cms.untracked.vstring(),
   inputCommands = cms.untracked.vstring("keep *", 
        "drop l1tHGCalTowerMapBXVector_hgcalTriggerPrimitiveDigiProducer_towerMap_HLT",
        "drop l1tEMTFHit2016Extras_simEmtfDigis_CSC_HLT",
        "drop l1tEMTFHit2016Extras_simEmtfDigis_RPC_HLT",
        "drop l1tEMTFHit2016s_simEmtfDigis__HLT",
        "drop l1tEMTFTrack2016Extras_simEmtfDigis__HLT",
        "drop l1tEMTFTrack2016s_simEmtfDigis__HLT")
#if GEOMETRY == "D17":
#    Source_Files = cms.untracked.vstring(
#       "/store/relval/CMSSW_9_3_7/RelValSingleMuPt10/GEN-SIM-DIGI-RAW/93X_upgrade2023_realistic_v5_2023D17noPU-v2/10000/0A598722-962C-E811-93E9-0CC47A7C354A.root",
)
    
#process.source = cms.Source("PoolSource", fileNames = Source_Files)

process.TFileService = cms.Service("TFileService", fileName = cms.string('test_CMSSW10_muon-10_PU0_pixtrk.root'), closeFileFast = cms.untracked.bool(True))


############################################################
# L1 tracking
############################################################

# remake stubs 

# ===> IMPORTANT !!! stub window tuning as is by default in CMSSW is incorrect !!! <===


process.load('L1Trigger.TrackTrigger.TrackTrigger_cff')
from L1Trigger.TrackTrigger.TTStubAlgorithmRegister_cfi import *
process.load("SimTracker.TrackTriggerAssociation.TrackTriggerAssociator_cff")

process.TTClusterStub = cms.Path(process.TrackTriggerClustersStubs)
process.TTClusterStubTruth = cms.Path(process.TrackTriggerAssociatorClustersStubs)

process.load("L1Trigger.TrackFindingTracklet.L1TrackletTracks_cff")
process.TTTracks = cms.Path(process.L1TrackletTracks)
process.TTTracksWithTruth = cms.Path(process.L1TrackletTracksWithAssociators)

###############################################################
# Add pixel stuff
################################################################
process.load('RecoLocalTracker.SiPixelClusterizer.SiPixelClusterizer_cfi')
process.pClusters = cms.Path(process.siPixelClusters)

process.L1simulation_step = cms.Path(process.SimL1Emulator)

process.load('RecoLocalTracker.SiPixelRecHits.SiPixelRecHits_cfi')
process.load('RecoLocalTracker.SiPixelRecHits.PixelCPEESProducers_cff')
#from RecoLocalTracker.SiPixelRecHits.SiPixelRecHits_cfi import *
#process.siPixelRecHits = siPixelRecHits

process.pixRec = cms.Path(
    process.siPixelRecHits
)

process.L1PixelTrackFit = cms.EDProducer("L1PixelTrackFit",
	L1TrackInputTag =  cms.InputTag("TTTracksFromTracklet", "Level1TTTracks"),
        SiPixRecHitInputTag = cms.InputTag("siPixelRecHits")
)

#tokenPixelRecHits_(consumes< SiPixelRecHitCollection > (iConfig.getParameter<edm::InputTag>("") ) )
process.pixTrk = cms.Path(process.L1PixelTrackFit);

############################################################
# Define the track ntuple process, MyProcess is the (unsigned) PDGID corresponding to the process which is run
# e.g. single electron/positron = 11
#      single pion+/pion- = 211
#      single muon+/muon- = 13 
#      pions in jets = 6
#      taus = 15
#      all TPs = 1
############################################################

process.L1PixelTrackNtuple = cms.EDAnalyzer('L1PixelTrackNtupleMaker',
                                       MyProcess = cms.int32(13),
                                       DebugMode = cms.bool(False),      # printout lots of debug statements
                                       SaveAllTracks = cms.bool(True),   # save *all* L1 tracks, not just truth matched to primary particle
                                       SaveStubs = cms.bool(False),      # save some info for *all* stubs
                                       L1Tk_nPar = cms.int32(5),         # use 4 or 5-parameter L1 track fit ??
                                       L1Tk_minNStub = cms.int32(4),     # L1 tracks with >= 4 stubs
                                       TP_minNStub = cms.int32(4),       # require TP to have >= X number of stubs associated with it
                                       TP_minNStubLayer = cms.int32(4),  # require TP to have stubs in >= X layers/disks
                                       TP_minPt = cms.double(2.0),       # only save TPs with pt > X GeV
                                       TP_maxEta = cms.double(2.4),      # only save TPs with |eta| < X
                                       TP_maxZ0 = cms.double(30.0),      # only save TPs with |z0| < X cm
                                       L1TrackInputTag = cms.InputTag("TTTracksFromTracklet", "Level1TTTracks"),               ## TTTrack input
                                       TTPixelTrackInputTag = cms.InputTag("L1PixelTrackFit", "Level1PixelTracks"),               ## TTTrack input
                                       MCTruthTrackInputTag = cms.InputTag("TTTrackAssociatorFromPixelDigis", "Level1TTTracks"), ## MCTruth input 
                                       # other input collections
                                       L1StubInputTag = cms.InputTag("TTStubsFromPhase2TrackerDigis","StubAccepted"),
                                       MCTruthClusterInputTag = cms.InputTag("TTClusterAssociatorFromPixelDigis", "ClusterAccepted"),
                                       MCTruthStubInputTag = cms.InputTag("TTStubAssociatorFromPixelDigis", "StubAccepted"),
                                       TrackingParticleInputTag = cms.InputTag("mix", "MergedTrackTruth"),
                                       TrackingVertexInputTag = cms.InputTag("mix", "MergedTrackTruth"),
                                       DoPixelTrack = cms.bool(True) 
                                       )
process.ana = cms.Path(process.L1PixelTrackNtuple)

#process.schedule = cms.Schedule(process.TTClusterStub,process.TTTracksWithTruth,process.pClusters,process.pixRec,process.pixTrk,process.ana)
#process.schedule = cms.Schedule(process.L1simulation_step,process.TTClusterStub,process.TTTracksWithTruth,process.pClusters,process.pixRec,process.pixTrk,process.ana)
process.schedule = cms.Schedule(process.L1simulation_step,process.pClusters,process.pixRec,process.TTClusterStub,process.TTTracksWithTruth,process.pixTrk,process.ana)

