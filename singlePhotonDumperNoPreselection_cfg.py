##!/usr/bin/env cmsRun

import FWCore.ParameterSet.Config as cms
import FWCore.Utilities.FileUtils as FileUtils

process = cms.Process("Analysis")

process.load("FWCore.MessageService.MessageLogger_cfi")

from flashgg.MetaData.MetaConditionsReader import *
from flashgg.MetaData.JobConfig import customize
customize.metaConditions = MetaConditionsReader('$CMSSW_BASE/src/flashgg/MetaData/data/MetaConditions/Era2017_legacy_v1.json')

#process.source = cms.Source("PoolSource",
#                            fileNames=cms.untracked.vstring("/store/group/phys_higgs/cmshgg/sethzenz/flashgg/RunIIFall17-3_1_0/3_1_0/GJet_Pt-20toInf_DoubleEMEnriched_MGG-40to80_TuneCP5_13TeV_Pythia8/RunIIFall17-3_1_0-3_1_0-v0-RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/180606_161308/0000/myMicroAODOutputFile_10.root"
#))
process.source = cms.Source("PoolSource",
                            fileNames=cms.untracked.vstring("/store/group/phys_higgs/cmshgg/alesauva/flashgg/UL2017_2/10_6_4/GJets_DoubleEMEnriched_PtG-40MGG-80_TuneCP5_13TeV-madgraphMLM-pythia8/UL2017_2-10_6_4-v0-RunIISummer19UL17MiniAOD-106X_mc2017_realistic_v6-v2/200715_103912/0000/myMicroAODOutputFile_970.root"
))
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
process.MessageLogger.cerr.FwkReport.reportEvery = cms.untracked.int32( 1000 )
process.load("Configuration.StandardSequences.GeometryDB_cff")
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff")
process.GlobalTag.globaltag = '106X_mc2017_realistic_v7'

process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string("testWithPreselection.root")
)


# for MC puReweight has to be true for extra protection
process.load("flashgg.Taggers.globalVariables_cff")
#

from flashgg.Taggers.flashggDifferentialPhoIdInputsCorrection_cfi import setup_flashggDifferentialPhoIdInputsCorrection

process.globalVariables.puReWeight = cms.bool(True)

process.load("flashgg.Taggers.flashggDifferentialPhoIdInputsCorrection_cfi")
process.flashggDifferentialPhoIdInputsCorrection.effAreasConfigFile = cms.FileInPath("RecoEgamma/PhotonIdentification/data/Fall17/effAreaPhotons_cone03_pfPhotons_90percentBased_TrueVtx.txt")

process.flashggDifferentialPhoIdInputsCorrection.photonIdMVAweightfile_EE = cms.FileInPath("flashgg/MicroAOD/data/HggPhoId_94X_endcap_BDT_v2.weights.xml")
process.flashggDifferentialPhoIdInputsCorrection.photonIdMVAweightfile_EB = cms.FileInPath("flashgg/MicroAOD/data/HggPhoId_94X_barrel_BDT_v2.weights.xml")

setup_flashggDifferentialPhoIdInputsCorrection(process, customize.metaConditions)

#process.flashggUpdatedIdMVADiPhotons.photonIdMVAweightfile_EB_2017 = cms.FileInPath("flashgg/Model_0530_MD18LR03_M80Cut_PTM25Cut_UL17.xml")
#process.flashggUpdatedIdMVADiPhotons.photonIdMVAweightfile_EB_2017 = cms.FileInPath("flashgg/Model_0518_MD18_LR03_MassAndPTMCut_UL17.xml")
#process.flashggUpdatedIdMVADiPhotons.photonIdMVAweightfile_EB_2017 = cms.FileInPath("flashgg/Model_0604_MD18LR03_M80Cut_PTM25Cut_NoPreselection_UL17.xml")
#process.flashggUpdatedIdMVADiPhotons.photonIdMVAweightfile_EE_2017 = cms.FileInPath("flashgg/Model_0601_MD20LR04_M80Cut_PTM25Cut_UL17_ENDCAP.xml")
#process.flashggUpdatedIdMVADiPhotons.photonIdMVAweightfile_EE_2017 = cms.FileInPath("flashgg/Model_0601_MD20LR04_M80Cut_PTM25Cut_UL17_ENDCAP.xml")
#process.flashggUpdatedIdMVADiPhotons.photonIdMVAweightfile_EE_2017 = cms.FileInPath("flashgg/MicroAOD/data/XGB_Convert_TMVA_Endcap_SA_phoID_UL18_woCorr.xml")
#process.flashggUpdatedIdMVADiPhotons.photonIdMVAweightfile_EE_2017 = cms.FileInPath("flashgg/MicroAOD/data/XGB_Convert_TMVA_Endcap_SA_phoID_UL2017_woCorr.xml")

process.flashggDifferentialPhoIdInputsCorrection.is2017 = cms.bool(True)
process.flashggDifferentialPhoIdInputsCorrection.reRunRegression = cms.bool(False)
process.flashggDifferentialPhoIdInputsCorrection.doNon5x5transformation = cms.bool(False)
process.flashggDifferentialPhoIdInputsCorrection.do5x5correction = cms.bool(False)
process.flashggDifferentialPhoIdInputsCorrection.doIsoCorrection = cms.bool(False)


from flashgg.Taggers.flashggPreselectedDiPhotons_cfi import flashggPreselectedDiPhotons
process.kinPreselDiPhotons = flashggPreselectedDiPhotons.clone(
#from flashgg.Taggers.flashggUpdatedIdMVADiPhotons_cfi import flashggUpdatedIdMVADiPhotons
#process.kinPreselDiPhotons = flashggUpdatedIdMVADiPhotons.clone(
src = cms.InputTag("flashggDifferentialPhoIdInputsCorrection"),
#src = cms.InputTag("flashggPreselectedDiPhotons"),
#WITH PRESELECTION
cut=cms.string(
#  *****      "mass > 95.0"
         "mass > 80.0"
# *****        "(leadingPhoton.hadronicOverEm < 0.08 && subLeadingPhoton.hadronicOverEm < 0.08)"
#        " && !(subLeadingPhoton.genMatchType == 1 && subLeadingPhoton.hasMatchedGenPhoton && (abs((subLeadingPhoton.matchedGenPhoton.pt - subLeadingPhoton.pt)/subLeadingPhoton.pt) > 0.05))"
#        " && !(leadingPhoton.genMatchType == 1 && leadingPhoton.hasMatchedGenPhoton && (abs((leadingPhoton.matchedGenPhoton.pt - leadingPhoton.pt)/leadingPhoton.pt) > 0.05))"
#        " && (leadingPhoton.pt > 25.0 && subLeadingPhoton.pt > 25.0)"
        " && (leadingPhoton.pt > 18.0 && subLeadingPhoton.pt > 18.0)"
       " && (leadingPhoton.pt/mass > 0.20 && subLeadingPhoton.pt/mass > 0.20)"
        "&& (abs(leadingPhoton.superCluster.eta)<2.5 && abs(subLeadingPhoton.superCluster.eta)<2.5)"
        " && (abs(leadingPhoton.superCluster.eta)<1.4442 || abs(leadingPhoton.superCluster.eta)>1.566)"
        " && (abs(subLeadingPhoton.superCluster.eta)<1.4442 || abs(subLeadingPhoton.superCluster.eta)>1.566)"
        " && (leadingPhoton.hadTowOverEm < 0.15 && (leadingPhoton.full5x5_r9>0.8 || leadingPhoton.chargedHadronIso<20 || leadingPhoton.chargedHadronIso<(0.3*leadingPhoton.pt)))"
        " && (subLeadingPhoton.hadTowOverEm < 0.15 && (subLeadingPhoton.full5x5_r9>0.8 || subLeadingPhoton.chargedHadronIso<20 || subLeadingPhoton.chargedHadronIso<(0.3*subLeadingPhoton.pt)))"
       )
)

process.flashggSinglePhotonViews = cms.EDProducer("FlashggSinglePhotonViewProducer",
                                                  DiPhotonTag=cms.InputTag('kinPreselDiPhotons'),                                         
                                                  maxCandidates = cms.int32(1)
                                                  )

process.load("flashgg.Taggers.photonViewDumper_cfi") ##  import diphotonDumper 
import flashgg.Taggers.dumperConfigTools as cfgTools

process.photonViewDumper.src = "flashggSinglePhotonViews"
process.photonViewDumper.dumpTrees = True
process.photonViewDumper.dumpWorkspace = False
process.photonViewDumper.quietRooFit = True

#process.photonViewDumper.nameTemplate ="$PROCESS"

## list of variables to be dumped in trees/datasets. Same variables for all categories
variables=["pfPhoIso03             := photon.pfPhoIso03",
           "pfChgIsoWrtChosenVtx02 := photon.pfChgIsoWrtChosenVtx02",
           "hadronicOverEm         := photon.hadronicOverEm",
           "genMatchType           := photon.genMatchType",
           "pt                     := photon.pt",
           "genPt                  := ?photon.hasMatchedGenPhoton?photon.matchedGenPhoton.pt:0",
           "energy                 := photon.energy",
           "genEnergy              := ?photon.hasMatchedGenPhoton?photon.matchedGenPhoton.energy : 0",
           "eta                    := photon.eta",
           "scEta                  := photon.superCluster.eta",
           "phi                    := photon.phi",
           "scPhi                  := photon.superCluster.phi",
           "SCRawE                 := photon.superCluster.rawEnergy",
           "etaWidth               := photon.superCluster.etaWidth",
           "phiWidth               := photon.superCluster.phiWidth",
           "covIphiIphi            := photon.sipip",
           "chgIsoWrtWorstVtx      := photon.pfChgIsoWrtWorstVtx03",
           "phoIso03               := photon.pfPhoIso03",
           "phoIsoCorr             := photon.pfPhoIso03Corr",
           "chgIsoWrtChosenVtx     := pfChIso03WrtChosenVtx",
           "hcalTowerSumEtConeDR03 := photon.hcalTowerSumEtConeDR03",
           "trkSumPtHollowConeDR03 := photon.trkSumPtHollowConeDR03",
           "hadTowOverEm           := photon.hadTowOverEm",
           "chargedHadronIso       := photon.chargedHadronIso",
           "idMVA                  := phoIdMvaWrtChosenVtx",
           "sigmaIetaIeta          := photon.full5x5_sigmaIetaIeta",
           "r9                     := photon.full5x5_r9",
           "esEffSigmaRR           := photon.esEffSigmaRR",
           "s4                     := photon.s4",
           "covIEtaIPhi            := photon.sieip",
           "esEnergy               := photon.superCluster.preshowerEnergy",
           "esEnergyOverRawE       := photon.superCluster.preshowerEnergy/photon.superCluster.rawEnergy"
           ]

## list of histograms to be plotted
histograms=["r9>>r9(110,0,1.1)",
            "scEta>>scEta(100,-2.5,2.5)"
            ]

## define categories and associated objects to dump
cfgTools.addCategory(process.photonViewDumper,
                     "Reject",
                     "abs(photon.superCluster.eta)>=1.4442&&abs(photon.superCluster.eta)<=1.566||abs(photon.superCluster.eta)>=2.5",
                     -1 ## if nSubcat is -1 do not store anythings
                     )

# interestng categories 
cfgTools.addCategories(process.photonViewDumper,
                       ## categories definition
                       ## cuts are applied in cascade. Events getting to these categories have already failed the "Reject" selection
#                       [("promptPhotonsPass","photon.genMatchType == 1 && photon.hasMatchedGenPhoton && (abs((photon.matchedGenPhoton.pt - photon.pt)/photon.pt) < 0.1)",0),
                        [("promptPhotons","photon.genMatchType == 1",0),
                        ("fakePhotons","photon.genMatchType != 1",0),
                        ],
                        
                        #[("hgg_125","1 == 1",0),
                        #],
                       ## variables to be dumped in trees/datasets. Same variables for all categories
                       ## if different variables wanted for different categories, can add categorie one by one with cfgTools.addCategory
                       variables=variables,
                       ## histograms to be plotted. 
                       ## the variables need to be defined first
                       histograms=histograms,
                       )

process.p1 = cms.Path(process.flashggDifferentialPhoIdInputsCorrection*
                      process.kinPreselDiPhotons*
                      process.flashggSinglePhotonViews*
                      process.photonViewDumper
                      )


from flashgg.MetaData.JobConfig import customize
customize.setDefault("maxEvents",10000)
customize(process)

