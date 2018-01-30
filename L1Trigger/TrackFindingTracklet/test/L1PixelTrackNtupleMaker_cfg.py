############################################################
# define basic process
############################################################

import FWCore.ParameterSet.Config as cms
import os
process = cms.Process("L1PixelTrackNtuple")

GEOMETRY = "D17"

from Configuration.StandardSequences.Eras import eras
process = cms.Process('RERUNL1',eras.Phase2_timing)


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

#if GEOMETRY == "D10": 
#    print "using geometry " + GEOMETRY + " (flat)"
#    process.load('Configuration.Geometry.GeometryExtended2023D10Reco_cff')
#    process.load('Configuration.Geometry.GeometryExtended2023D10_cff')
#elif GEOMETRY == "D13":
#    print "using geometry " + GEOMETRY + " (tilted)"
#    process.load('Configuration.Geometry.GeometryExtended2023D13Reco_cff')
#    process.load('Configuration.Geometry.GeometryExtended2023D13_cff')
#else:
#    print "this is not a valid geometry!!!"

process.load('Configuration.Geometry.GeometryExtended2023D17Reco_cff') ## this needs to match the geometry you are running on
process.load('Configuration.Geometry.GeometryExtended2023D17_cff')     ## this needs to match the geometry you are running on

process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:upgradePLS3', '')


############################################################
# input and output
############################################################

process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(-1))

if GEOMETRY == "D10": 
    #D10 (flat barrel)
    Source_Files = cms.untracked.vstring(
    "/store/relval/CMSSW_9_1_0_pre3/RelValSingleMuPt10Extended/GEN-SIM-DIGI-RAW/91X_upgrade2023_realistic_v1_D10-v1/10000/044925F3-5F2E-E711-A92B-0CC47A7AB7A0.root",
    "/store/relval/CMSSW_9_1_0_pre3/RelValSingleMuPt10Extended/GEN-SIM-DIGI-RAW/91X_upgrade2023_realistic_v1_D10-v1/10000/42543260-602E-E711-A41C-0025905A48C0.root",
    "/store/relval/CMSSW_9_1_0_pre3/RelValSingleMuPt10Extended/GEN-SIM-DIGI-RAW/91X_upgrade2023_realistic_v1_D10-v1/10000/72D6B8B7-612E-E711-A727-0CC47A4D7692.root",
    "/store/relval/CMSSW_9_1_0_pre3/RelValSingleMuPt10Extended/GEN-SIM-DIGI-RAW/91X_upgrade2023_realistic_v1_D10-v1/10000/786DD1A7-612E-E711-84EB-0025905B855E.root",
    "/store/relval/CMSSW_9_1_0_pre3/RelValSingleMuPt10Extended/GEN-SIM-DIGI-RAW/91X_upgrade2023_realistic_v1_D10-v1/10000/9255C706-602E-E711-BDE0-0025905A609A.root",
    "/store/relval/CMSSW_9_1_0_pre3/RelValSingleMuPt10Extended/GEN-SIM-DIGI-RAW/91X_upgrade2023_realistic_v1_D10-v1/10000/BE75B044-602E-E711-8DC3-0CC47A4D7692.root",
    "/store/relval/CMSSW_9_1_0_pre3/RelValSingleMuPt10Extended/GEN-SIM-DIGI-RAW/91X_upgrade2023_realistic_v1_D10-v1/10000/EA054BA3-5F2E-E711-B7F4-0025905A6084.root",
)
elif GEOMETRY == "D13":
    #D13 (tilted barrel)
    Source_Files = cms.untracked.vstring(
#     "/store/user/jhkim/SingleMuon_Pt8to100_Eta3p1_CMSSW_9_1_0_pre3_NoPU/SingleMuon_Pt8to100_Eta3p1_NoPU_91X_upgrade2023_realistic_v3_GENSIM_DIGIRAW/170926_031256/0000/TSG-PhaseIISpring17D-00004_1.root"
        'file:/data8/Users/gbyu/SingleMuon/TSG-PhaseIISpring17D-00004_1.root',
        'file:/data8/Users/gbyu/SingleMuon/TSG-PhaseIISpring17D-00004_2.root',
        'file:/data8/Users/gbyu/SingleMuon/TSG-PhaseIISpring17D-00004_3.root',
        'file:/data8/Users/gbyu/SingleMuon/TSG-PhaseIISpring17D-00004_4.root',
        'file:/data8/Users/gbyu/SingleMuon/TSG-PhaseIISpring17D-00004_10.root',
        'file:/data8/Users/gbyu/SingleMuon/TSG-PhaseIISpring17D-00004_11.root',
        'file:/data8/Users/gbyu/SingleMuon/TSG-PhaseIISpring17D-00004_5.root',
        'file:/data8/Users/gbyu/SingleMuon/TSG-PhaseIISpring17D-00004_13.root',
        'file:/data8/Users/gbyu/SingleMuon/TSG-PhaseIISpring17D-00004_6.root',
        'file:/data8/Users/gbyu/SingleMuon/TSG-PhaseIISpring17D-00004_7.root',
        'file:/data8/Users/gbyu/SingleMuon/TSG-PhaseIISpring17D-00004_16.root',
        'file:/data8/Users/gbyu/SingleMuon/TSG-PhaseIISpring17D-00004_8.root',
        'file:/data8/Users/gbyu/SingleMuon/TSG-PhaseIISpring17D-00004_17.root',
        'file:/data8/Users/gbyu/SingleMuon/TSG-PhaseIISpring17D-00004_9.root',
        'file:/data8/Users/gbyu/SingleMuon/TSG-PhaseIISpring17D-00004_18.root',
        'file:/data8/Users/gbyu/SingleMuon/TSG-PhaseIISpring17D-00004_19.root',
        'file:/data8/Users/gbyu/SingleMuon/TSG-PhaseIISpring17D-00004_20.root',
        'file:/data8/Users/gbyu/SingleMuon/TSG-PhaseIISpring17D-00004_22.root',
        'file:/data8/Users/gbyu/SingleMuon/TSG-PhaseIISpring17D-00004_25.root',
        'file:/data8/Users/gbyu/SingleMuon/TSG-PhaseIISpring17D-00004_27.root',
        'file:/data8/Users/gbyu/SingleMuon/TSG-PhaseIISpring17D-00004_28.root',
        'file:/data8/Users/gbyu/SingleMuon/TSG-PhaseIISpring17D-00004_29.root',
        'file:/data8/Users/gbyu/SingleMuon/TSG-PhaseIISpring17D-00004_30.root',
        'file:/data8/Users/gbyu/SingleMuon/TSG-PhaseIISpring17D-00004_34.root'
#        "/store/relval/CMSSW_9_1_0_pre3/RelValSingleMuPt10Extended/GEN-SIM-DIGI-RAW/91X_upgrade2023_realistic_v1_D13-v1/10000/003A8F87-6A2E-E711-AFAC-003048FFCC16.root",
#    "/store/relval/CMSSW_9_1_0_pre3/RelValSingleMuPt10Extended/GEN-SIM-DIGI-RAW/91X_upgrade2023_realistic_v1_D13-v1/10000/20F6CC9B-692E-E711-B7B6-0CC47A4D76C6.root",
#    "/store/relval/CMSSW_9_1_0_pre3/RelValSingleMuPt10Extended/GEN-SIM-DIGI-RAW/91X_upgrade2023_realistic_v1_D13-v1/10000/308255CD-682E-E711-89BE-0025905B85CA.root",
#    "/store/relval/CMSSW_9_1_0_pre3/RelValSingleMuPt10Extended/GEN-SIM-DIGI-RAW/91X_upgrade2023_realistic_v1_D13-v1/10000/44734904-6B2E-E711-82BB-0025905B85B2.root",
#    "/store/relval/CMSSW_9_1_0_pre3/RelValSingleMuPt10Extended/GEN-SIM-DIGI-RAW/91X_upgrade2023_realistic_v1_D13-v1/10000/620FE305-6B2E-E711-A312-0025905A60BE.root",
#    "/store/relval/CMSSW_9_1_0_pre3/RelValSingleMuPt10Extended/GEN-SIM-DIGI-RAW/91X_upgrade2023_realistic_v1_D13-v1/10000/6CD6D66E-6A2E-E711-8F75-0025905A6136.root",
#    "/store/relval/CMSSW_9_1_0_pre3/RelValSingleMuPt10Extended/GEN-SIM-DIGI-RAW/91X_upgrade2023_realistic_v1_D13-v1/10000/888282CA-682E-E711-8DB0-0025905A4964.root",
#    "/store/relval/CMSSW_9_1_0_pre3/RelValSingleMuPt10Extended/GEN-SIM-DIGI-RAW/91X_upgrade2023_realistic_v1_D13-v1/10000/8A1BD86E-6A2E-E711-8DB6-0025905A4964.root",
#    "/store/relval/CMSSW_9_1_0_pre3/RelValSingleMuPt10Extended/GEN-SIM-DIGI-RAW/91X_upgrade2023_realistic_v1_D13-v1/10000/BCB8C8A5-692E-E711-BA94-0025905A612E.root",
#
    #"/store/relval/CMSSW_9_1_0_pre3/RelValTTbar_14TeV/GEN-SIM-DIGI-RAW/91X_upgrade2023_realistic_v1_D13-v2/10000/0E9A4F45-602E-E711-916C-0CC47A7C3430.root",
    #"/store/relval/CMSSW_9_1_0_pre3/RelValTTbar_14TeV/GEN-SIM-DIGI-RAW/91X_upgrade2023_realistic_v1_D13-v2/10000/12249F9F-5F2E-E711-849D-0CC47A4D76C6.root",
    #"/store/relval/CMSSW_9_1_0_pre3/RelValTTbar_14TeV/GEN-SIM-DIGI-RAW/91X_upgrade2023_realistic_v1_D13-v2/10000/4A2589F6-622E-E711-8EB2-0025905B85CC.root",
    #"/store/relval/CMSSW_9_1_0_pre3/RelValTTbar_14TeV/GEN-SIM-DIGI-RAW/91X_upgrade2023_realistic_v1_D13-v2/10000/4C511711-5F2E-E711-847A-0025905B857E.root",
    #"/store/relval/CMSSW_9_1_0_pre3/RelValTTbar_14TeV/GEN-SIM-DIGI-RAW/91X_upgrade2023_realistic_v1_D13-v2/10000/52EA294A-602E-E711-B368-0025905B85CA.root",
    #"/store/relval/CMSSW_9_1_0_pre3/RelValTTbar_14TeV/GEN-SIM-DIGI-RAW/91X_upgrade2023_realistic_v1_D13-v2/10000/5ECEC385-5E2E-E711-8E82-0CC47A7C3430.root",
    #"/store/relval/CMSSW_9_1_0_pre3/RelValTTbar_14TeV/GEN-SIM-DIGI-RAW/91X_upgrade2023_realistic_v1_D13-v2/10000/7A367D94-5D2E-E711-A3F2-0025905B8568.root",
    #"/store/relval/CMSSW_9_1_0_pre3/RelValTTbar_14TeV/GEN-SIM-DIGI-RAW/91X_upgrade2023_realistic_v1_D13-v2/10000/BAABF1B9-5E2E-E711-BE64-0025905A60E4.root",
    #"/store/relval/CMSSW_9_1_0_pre3/RelValTTbar_14TeV/GEN-SIM-DIGI-RAW/91X_upgrade2023_realistic_v1_D13-v2/10000/EC59F295-602E-E711-BAB5-0025905A48C0.root",
    #"/store/relval/CMSSW_9_1_0_pre3/RelValTTbar_14TeV/GEN-SIM-DIGI-RAW/91X_upgrade2023_realistic_v1_D13-v2/10000/ECC7C5F2-622E-E711-8704-0025905AA9F0.root",
)
else:
   Source_Files = cms.untracked.vstring(
#     "/store/user/jhkim/SingleMuon_Pt8to100_Eta3p1_CMSSW_9_1_0_pre3_NoPU/SingleMuon_Pt8to100_Eta3p1_NoPU_91X_upgrade2023_realistic_v3_GENSIM_DIGIRAW/170926_031256/0000/TSG-PhaseIISpring17D-00004_1.root"
        'file:/data8/Users/gbyu/SingleMuon_930/SingleMuon_Pt2to100_Eta2p6_NoPU_93X_upgrade2023_realistic_v2_D17_GENSIMDIGIRAW_1.root',
        'file:/data8/Users/gbyu/SingleMuon_930/SingleMuon_Pt2to100_Eta2p6_NoPU_93X_upgrade2023_realistic_v2_D17_GENSIMDIGIRAW_2.root',
        'file:/data8/Users/gbyu/SingleMuon_930/SingleMuon_Pt2to100_Eta2p6_NoPU_93X_upgrade2023_realistic_v2_D17_GENSIMDIGIRAW_3.root',
        'file:/data8/Users/gbyu/SingleMuon_930/SingleMuon_Pt2to100_Eta2p6_NoPU_93X_upgrade2023_realistic_v2_D17_GENSIMDIGIRAW_4.root',
        'file:/data8/Users/gbyu/SingleMuon_930/SingleMuon_Pt2to100_Eta2p6_NoPU_93X_upgrade2023_realistic_v2_D17_GENSIMDIGIRAW_5.root',
        'file:/data8/Users/gbyu/SingleMuon_930/SingleMuon_Pt2to100_Eta2p6_NoPU_93X_upgrade2023_realistic_v2_D17_GENSIMDIGIRAW_6.root',
        'file:/data8/Users/gbyu/SingleMuon_930/SingleMuon_Pt2to100_Eta2p6_NoPU_93X_upgrade2023_realistic_v2_D17_GENSIMDIGIRAW_7.root',
        'file:/data8/Users/gbyu/SingleMuon_930/SingleMuon_Pt2to100_Eta2p6_NoPU_93X_upgrade2023_realistic_v2_D17_GENSIMDIGIRAW_8.root',
        'file:/data8/Users/gbyu/SingleMuon_930/SingleMuon_Pt2to100_Eta2p6_NoPU_93X_upgrade2023_realistic_v2_D17_GENSIMDIGIRAW_9.root',
        'file:/data8/Users/gbyu/SingleMuon_930/SingleMuon_Pt2to100_Eta2p6_NoPU_93X_upgrade2023_realistic_v2_D17_GENSIMDIGIRAW_10.root',
#        'file:/data8/Users/gbyu/SingleMuon_930/SingleMuon_Pt2to100_Eta2p6_NoPU_93X_upgrade2023_realistic_v2_D17_GENSIMDIGIRAW_11.root',
#        'file:/data8/Users/gbyu/SingleMuon_930/SingleMuon_Pt2to100_Eta2p6_NoPU_93X_upgrade2023_realistic_v2_D17_GENSIMDIGIRAW_12.root',
#        'file:/data8/Users/gbyu/SingleMuon_930/SingleMuon_Pt2to100_Eta2p6_NoPU_93X_upgrade2023_realistic_v2_D17_GENSIMDIGIRAW_13.root',
#        'file:/data8/Users/gbyu/SingleMuon_930/SingleMuon_Pt2to100_Eta2p6_NoPU_93X_upgrade2023_realistic_v2_D17_GENSIMDIGIRAW_14.root',
#        'file:/data8/Users/gbyu/SingleMuon_930/SingleMuon_Pt2to100_Eta2p6_NoPU_93X_upgrade2023_realistic_v2_D17_GENSIMDIGIRAW_15.root',
#        'file:/data8/Users/gbyu/SingleMuon_930/SingleMuon_Pt2to100_Eta2p6_NoPU_93X_upgrade2023_realistic_v2_D17_GENSIMDIGIRAW_16.root',
#        'file:/data8/Users/gbyu/SingleMuon_930/SingleMuon_Pt2to100_Eta2p6_NoPU_93X_upgrade2023_realistic_v2_D17_GENSIMDIGIRAW_17.root',
#        'file:/data8/Users/gbyu/SingleMuon_930/SingleMuon_Pt2to100_Eta2p6_NoPU_93X_upgrade2023_realistic_v2_D17_GENSIMDIGIRAW_18.root',
#        'file:/data8/Users/gbyu/SingleMuon_930/SingleMuon_Pt2to100_Eta2p6_NoPU_93X_upgrade2023_realistic_v2_D17_GENSIMDIGIRAW_19.root',
#        'file:/data8/Users/gbyu/SingleMuon_930/SingleMuon_Pt2to100_Eta2p6_NoPU_93X_upgrade2023_realistic_v2_D17_GENSIMDIGIRAW_20.root',
#        'file:/data8/Users/gbyu/SingleMuon_930/SingleMuon_Pt2to100_Eta2p6_NoPU_93X_upgrade2023_realistic_v2_D17_GENSIMDIGIRAW_21.root',
#        'file:/data8/Users/gbyu/SingleMuon_930/SingleMuon_Pt2to100_Eta2p6_NoPU_93X_upgrade2023_realistic_v2_D17_GENSIMDIGIRAW_22.root',
#        'file:/data8/Users/gbyu/SingleMuon_930/SingleMuon_Pt2to100_Eta2p6_NoPU_93X_upgrade2023_realistic_v2_D17_GENSIMDIGIRAW_23.root',
#        'file:/data8/Users/gbyu/SingleMuon_930/SingleMuon_Pt2to100_Eta2p6_NoPU_93X_upgrade2023_realistic_v2_D17_GENSIMDIGIRAW_24.root',
#        'file:/data8/Users/gbyu/SingleMuon_930/SingleMuon_Pt2to100_Eta2p6_NoPU_93X_upgrade2023_realistic_v2_D17_GENSIMDIGIRAW_25.root',
#        'file:/data8/Users/gbyu/SingleMuon_930/SingleMuon_Pt2to100_Eta2p6_NoPU_93X_upgrade2023_realistic_v2_D17_GENSIMDIGIRAW_26.root',
#        'file:/data8/Users/gbyu/SingleMuon_930/SingleMuon_Pt2to100_Eta2p6_NoPU_93X_upgrade2023_realistic_v2_D17_GENSIMDIGIRAW_27.root',
#        'file:/data8/Users/gbyu/SingleMuon_930/SingleMuon_Pt2to100_Eta2p6_NoPU_93X_upgrade2023_realistic_v2_D17_GENSIMDIGIRAW_28.root',
#        'file:/data8/Users/gbyu/SingleMuon_930/SingleMuon_Pt2to100_Eta2p6_NoPU_93X_upgrade2023_realistic_v2_D17_GENSIMDIGIRAW_29.root',
#        'file:/data8/Users/gbyu/SingleMuon_930/SingleMuon_Pt2to100_Eta2p6_NoPU_93X_upgrade2023_realistic_v2_D17_GENSIMDIGIRAW_30.root',
#        'file:/data8/Users/gbyu/SingleMuon_930/SingleMuon_Pt2to100_Eta2p6_NoPU_93X_upgrade2023_realistic_v2_D17_GENSIMDIGIRAW_31.root',
#        'file:/data8/Users/gbyu/SingleMuon_930/SingleMuon_Pt2to100_Eta2p6_NoPU_93X_upgrade2023_realistic_v2_D17_GENSIMDIGIRAW_32.root',
#        'file:/data8/Users/gbyu/SingleMuon_930/SingleMuon_Pt2to100_Eta2p6_NoPU_93X_upgrade2023_realistic_v2_D17_GENSIMDIGIRAW_33.root',
#        'file:/data8/Users/gbyu/SingleMuon_930/SingleMuon_Pt2to100_Eta2p6_NoPU_93X_upgrade2023_realistic_v2_D17_GENSIMDIGIRAW_34.root',
#        'file:/data8/Users/gbyu/SingleMuon_930/SingleMuon_Pt2to100_Eta2p6_NoPU_93X_upgrade2023_realistic_v2_D17_GENSIMDIGIRAW_35.root',
#        'file:/data8/Users/gbyu/SingleMuon_930/SingleMuon_Pt2to100_Eta2p6_NoPU_93X_upgrade2023_realistic_v2_D17_GENSIMDIGIRAW_36.root',
#        'file:/data8/Users/gbyu/SingleMuon_930/SingleMuon_Pt2to100_Eta2p6_NoPU_93X_upgrade2023_realistic_v2_D17_GENSIMDIGIRAW_37.root',
#        'file:/data8/Users/gbyu/SingleMuon_930/SingleMuon_Pt2to100_Eta2p6_NoPU_93X_upgrade2023_realistic_v2_D17_GENSIMDIGIRAW_38.root',
#        'file:/data8/Users/gbyu/SingleMuon_930/SingleMuon_Pt2to100_Eta2p6_NoPU_93X_upgrade2023_realistic_v2_D17_GENSIMDIGIRAW_39.root',
#        'file:/data8/Users/gbyu/SingleMuon_930/SingleMuon_Pt2to100_Eta2p6_NoPU_93X_upgrade2023_realistic_v2_D17_GENSIMDIGIRAW_40.root',
#        'file:/data8/Users/gbyu/SingleMuon_930/SingleMuon_Pt2to100_Eta2p6_NoPU_93X_upgrade2023_realistic_v2_D17_GENSIMDIGIRAW_41.root',
#        'file:/data8/Users/gbyu/SingleMuon_930/SingleMuon_Pt2to100_Eta2p6_NoPU_93X_upgrade2023_realistic_v2_D17_GENSIMDIGIRAW_42.root',
#        'file:/data8/Users/gbyu/SingleMuon_930/SingleMuon_Pt2to100_Eta2p6_NoPU_93X_upgrade2023_realistic_v2_D17_GENSIMDIGIRAW_43.root',
#        'file:/data8/Users/gbyu/SingleMuon_930/SingleMuon_Pt2to100_Eta2p6_NoPU_93X_upgrade2023_realistic_v2_D17_GENSIMDIGIRAW_44.root',
#        'file:/data8/Users/gbyu/SingleMuon_930/SingleMuon_Pt2to100_Eta2p6_NoPU_93X_upgrade2023_realistic_v2_D17_GENSIMDIGIRAW_45.root',
#        'file:/data8/Users/gbyu/SingleMuon_930/SingleMuon_Pt2to100_Eta2p6_NoPU_93X_upgrade2023_realistic_v2_D17_GENSIMDIGIRAW_46.root',
#        'file:/data8/Users/gbyu/SingleMuon_930/SingleMuon_Pt2to100_Eta2p6_NoPU_93X_upgrade2023_realistic_v2_D17_GENSIMDIGIRAW_47.root',
#        'file:/data8/Users/gbyu/SingleMuon_930/SingleMuon_Pt2to100_Eta2p6_NoPU_93X_upgrade2023_realistic_v2_D17_GENSIMDIGIRAW_48.root',
#        'file:/data8/Users/gbyu/SingleMuon_930/SingleMuon_Pt2to100_Eta2p6_NoPU_93X_upgrade2023_realistic_v2_D17_GENSIMDIGIRAW_49.root',
#        'file:/data8/Users/gbyu/SingleMuon_930/SingleMuon_Pt2to100_Eta2p6_NoPU_93X_upgrade2023_realistic_v2_D17_GENSIMDIGIRAW_50.root'
)
process.source = cms.Source("PoolSource", fileNames = Source_Files)

process.TFileService = cms.Service("TFileService", fileName = cms.string('Muon_2-100_PU0_pixtrk_fixdiskz0_test10.root'), closeFileFast = cms.untracked.bool(True))


############################################################
# L1 tracking
############################################################

# remake stubs 

# ===> IMPORTANT !!! stub window tuning as is by default in CMSSW is incorrect !!! <===


process.load('L1Trigger.TrackTrigger.TrackTrigger_cff')
from L1Trigger.TrackTrigger.TTStubAlgorithmRegister_cfi import *

#if GEOMETRY == "D10": 
#    TTStubAlgorithm_official_Phase2TrackerDigi_.zMatchingPS = cms.bool(False)
process.TTClusterStub = cms.Path(process.TrackTriggerClustersStubs)

process.load("L1Trigger.TrackFindingTracklet.L1TrackletTracks_cff")

#from L1Trigger.TrackFindingTracklet.Tracklet_cfi import *
#if GEOMETRY == "D10": 
#    TTTracksFromTracklet.trackerGeometry = cms.untracked.string("flat")
#TTTracksFromTracklet.asciiFileName = cms.untracked.string("evlist.txt")

# run only the tracking (no MC truth associators)
process.TTTracks = cms.Path(process.L1TrackletTracks)

# run the tracking AND MC truth associators)
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

