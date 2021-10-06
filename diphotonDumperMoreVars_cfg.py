#!/usr/bin/env cmsRun

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
#                            fileNames=cms.untracked.vstring("/store/user/alesauva/flashgg/UL2017_4/10_6_4/ttHiggs0PMToGG_M125_TuneCP5_13TeV-JHUGenV7011-pythia8/UL2017_4-10_6_4-v0-RunIISummer19UL17MiniAOD-106X_mc2017_realistic_v6-v2/200720_165733/0000/myMicroAODOutputFile_1.root"
fileNames=cms.untracked.vstring("root://xrootd-cms.infn.it//store/user/alesauva/flashgg/UL2017_4/10_6_4/ttHiggs0PMToGG_M125_TuneCP5_13TeV-JHUGenV7011-pythia8/UL2017_4-10_6_4-v0-RunIISummer19UL17MiniAOD-106X_mc2017_realistic_v6-v2/200720_165733/0000/myMicroAODOutputFile_1.root"
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

from flashgg.Taggers.flashggMoreVarsDifferentialPhoIdInputsCorrection_cfi import setup_flashggMoreVarsDifferentialPhoIdInputsCorrection

process.globalVariables.puReWeight = cms.bool(True)

process.load("flashgg.Taggers.flashggMoreVarsDifferentialPhoIdInputsCorrection_cfi")
setup_flashggMoreVarsDifferentialPhoIdInputsCorrection(process, customize.metaConditions)

#process.flashggMoreVarsDifferentialPhoIdInputsCorrection.photonIdMVAweightfile_EE = cms.FileInPath("flashgg/Model_UL17_MD18LR03_NoPresel_DPT10_M80PTM20_ENDCAP_0829.xml")
#process.flashggMoreVarsDifferentialPhoIdInputsCorrection.photonIdMVAweightfile_EB = cms.FileInPath("flashgg/Model_UL17_MD18LR03_NoPresel_DPT10_M80PTM20_0829.xml")
process.flashggMoreVarsDifferentialPhoIdInputsCorrection.photonIdMVAweightfile_EE = cms.FileInPath("flashgg/EOS/models/Model_UL17_MD18LR03_NoPresel_M95PTM25_HovrE_DPT075_ENDCAP_0929.xml")
#process.flashggMoreVarsDifferentialPhoIdInputsCorrection.photonIdMVAweightfile_EB = cms.FileInPath("flashgg/EOS/models/Model_UL17_MD18LR03_WithPresel_M80PTM20_0906.xml")
process.flashggMoreVarsDifferentialPhoIdInputsCorrection.photonIdMVAweightfile_EB = cms.FileInPath("flashgg/EOS/models/Model_UL17_MD18LR03_NoPresel_M95PTM25_HovrE_DPT075_0929.xml")
#*****thisOne***process.flashggMoreVarsDifferentialPhoIdInputsCorrection.photonIdMVAweightfile_EB = cms.FileInPath("flashgg/Model_UL17_MD18LR03_NoPresel_AddedM80PTM20_DPT05_0815.xml")
#process.flashggMoreVarsDifferentialPhoIdInputsCorrection.photonIdMVAweightfile_EB = cms.FileInPath("flashgg/Model_UL17_WithBothHovrE_MD18LR03_M80PTM20_WithPreselection_0802.xml")

#process.flashggUpdatedIdMVADiPhotons.photonIdMVAweightfile_EB_2017 = cms.FileInPath("flashgg/Model_0530_MD18LR03_M80Cut_PTM25Cut_UL17.xml")
#process.flashggUpdatedIdMVADiPhotons.photonIdMVAweightfile_EB_2017 = cms.FileInPath("flashgg/Model_0518_MD18_LR03_MassAndPTMCut_UL17.xml")
#process.flashggUpdatedIdMVADiPhotons.photonIdMVAweightfile_EB_2017 = cms.FileInPath("flashgg/Model_0604_MD18LR03_M80Cut_PTM25Cut_NoPreselection_UL17.xml")
#process.flashggUpdatedIdMVADiPhotons.photonIdMVAweightfile_EE_2017 = cms.FileInPath("flashgg/Model_0601_MD20LR04_M80Cut_PTM25Cut_UL17_ENDCAP.xml")
#process.flashggUpdatedIdMVADiPhotons.photonIdMVAweightfile_EE_2017 = cms.FileInPath("flashgg/Model_0601_MD20LR04_M80Cut_PTM25Cut_UL17_ENDCAP.xml")
#process.flashggUpdatedIdMVADiPhotons.photonIdMVAweightfile_EE_2017 = cms.FileInPath("flashgg/MicroAOD/data/XGB_Convert_TMVA_Endcap_SA_phoID_UL18_woCorr.xml")
#process.flashggUpdatedIdMVADiPhotons.photonIdMVAweightfile_EE_2017 = cms.FileInPath("flashgg/MicroAOD/data/XGB_Convert_TMVA_Endcap_SA_phoID_UL2017_woCorr.xml")

process.flashggMoreVarsDifferentialPhoIdInputsCorrection.is2017 = cms.bool(True)
process.flashggMoreVarsDifferentialPhoIdInputsCorrection.reRunRegression = cms.bool(False)
process.flashggMoreVarsDifferentialPhoIdInputsCorrection.doNon5x5transformation = cms.bool(False)
process.flashggMoreVarsDifferentialPhoIdInputsCorrection.do5x5correction = cms.bool(False)
process.flashggMoreVarsDifferentialPhoIdInputsCorrection.doIsoCorrection = cms.bool(False)

from flashgg.Taggers.flashggPreselectedDiPhotons_cfi import flashggPreselectedDiPhotons
process.load("flashgg.Taggers.flashggPreselectedDiPhotons_cfi")
#process.flashggPreselectedDiPhotons.photonIdMVAweightfile_EB_2017 = cms.FileInPath("flashgg/Model_0626_MD18LR03_M80PTM20_Preselection_UL17.xml")

process.flashggPreselectedDiPhotons.is2017 = cms.bool(True)
process.flashggPreselectedDiPhotons.reRunRegression = cms.bool(False)
process.flashggPreselectedDiPhotons.doNon5x5transformation = cms.bool(False)
process.flashggPreselectedDiPhotons.do5x5correction = cms.bool(False)
process.flashggPreselectedDiPhotons.doIsoCorrection = cms.bool(False)

process.kinPreselDiPhotons = flashggPreselectedDiPhotons.clone(
#from flashgg.Taggers.flashggUpdatedIdMVADiPhotons_cfi import flashggUpdatedIdMVADiPhotons
#process.kinPreselDiPhotons = flashggUpdatedIdMVADiPhotons.clone(
src = cms.InputTag("flashggMoreVarsDifferentialPhoIdInputsCorrection"),
#src = cms.InputTag("flashggPreselectedDiPhotons"),
#WITH PRESELECTION
#cut=cms.string(
##  *****      "mass > 95.0"
##        #"mass > 55.0"
## *****        "(leadingPhoton.hadronicOverEm < 0.08 && subLeadingPhoton.hadronicOverEm < 0.08)"
##        " && !(subLeadingPhoton.genMatchType == 1 && subLeadingPhoton.hasMatchedGenPhoton && (abs((subLeadingPhoton.matchedGenPhoton.pt - subLeadingPhoton.pt)/subLeadingPhoton.pt) > 0.05))"
##        " && !(leadingPhoton.genMatchType == 1 && leadingPhoton.hasMatchedGenPhoton && (abs((leadingPhoton.matchedGenPhoton.pt - leadingPhoton.pt)/leadingPhoton.pt) > 0.05))"
##        " && (leadingPhoton.pt > 25.0 && subLeadingPhoton.pt > 25.0)"
#        " (leadingPhoton.pt > 18.0 && subLeadingPhoton.pt > 18.0)"
##  *****      " && (leadingPhoton.pt/mass > 0.33 && subLeadingPhoton.pt/mass > 0.25)"
#        "&& (abs(leadingPhoton.superCluster.eta)<2.5 && abs(subLeadingPhoton.superCluster.eta)<2.5)"
#        " && (abs(leadingPhoton.superCluster.eta)<1.4442 || abs(leadingPhoton.superCluster.eta)>1.566)"
#        " && (abs(subLeadingPhoton.superCluster.eta)<1.4442 || abs(subLeadingPhoton.superCluster.eta)>1.566)"
#        " && (leadingPhoton.hadTowOverEm < 0.15 && (leadingPhoton.full5x5_r9>0.8 || leadingPhoton.chargedHadronIso<20 || leadingPhoton.chargedHadronIso<(0.3*leadingPhoton.pt)))"
#        " && (subLeadingPhoton.hadTowOverEm < 0.15 && (subLeadingPhoton.full5x5_r9>0.8 || subLeadingPhoton.chargedHadronIso<20 || subLeadingPhoton.chargedHadronIso<(0.3*subLeadingPhoton.pt)))"
#       )
#WITHOUT PRESELECTION
cut=cms.string(
#        "mass > 95.0"
#        "mass > 55.0"
#        "(leadingPhoton.hadronicOverEm < 0.08 && subLeadingPhoton.hadronicOverEm < 0.08)"
#        " && !(subLeadingPhoton.genMatchType == 1 && subLeadingPhoton.hasMatchedGenPhoton && (abs((subLeadingPhoton.matchedGenPhoton.pt - subLeadingPhoton.pt)/subLeadingPhoton.pt) > 0.05))"
#        " && !(leadingPhoton.genMatchType == 1 && leadingPhoton.hasMatchedGenPhoton && (abs((leadingPhoton.matchedGenPhoton.pt - leadingPhoton.pt)/leadingPhoton.pt) > 0.05))"
#        " && (leadingPhoton.pt > 25.0 && subLeadingPhoton.pt > 25.0)"
#        "(leadingPhoton.pt > 18.0 && subLeadingPhoton.pt > 18.0)"
#        " && (leadingPhoton.pt/mass > 0.33 && subLeadingPhoton.pt/mass > 0.25)"
        "  (abs(leadingPhoton.superCluster.eta)<2.5 && abs(subLeadingPhoton.superCluster.eta)<2.5)"
        " && (abs(leadingPhoton.superCluster.eta)<1.4442 || abs(leadingPhoton.superCluster.eta)>1.566)"
        " && (abs(subLeadingPhoton.superCluster.eta)<1.4442 || abs(subLeadingPhoton.superCluster.eta)>1.566)"
#       a
        )
)

process.load("flashgg.Taggers.diphotonDumper_cfi") ##  import diphotonDumper
import flashgg.Taggers.dumperConfigTools as cfgTools

process.diphotonDumper.src = "kinPreselDiPhotons"
#process.diphotonDumper.src = "flashggDiPhotons"

process.diphotonDumper.dumpTrees = True
process.diphotonDumper.dumpWorkspace = False
process.diphotonDumper.quietRooFit = True
process.diphotonDumper.dumpGlobalVariables = cms.untracked.bool(True)
process.diphotonDumper.globalVariables = process.globalVariables

process.diphotonDumper.nameTemplate ="$PROCESS"
##DO XGB STUFF


## list of variables to be dumped in trees/datasets. Same variables for all categories
variables=["hggMass[320,100,180]       := mass",
            ##Leading Photon Variables
           "leadPfPhoIso03             := leadingPhoton.pfPhoIso03",
           "leadPfChgIsoWrtChosenVtx02 := leadingPhoton.pfChgIsoWrtChosenVtx02",
           "leadHadronicOverEm         := leadingPhoton.hadronicOverEm",
           "leadGenMatchType           := leadingPhoton.genMatchType",
           "leadPt                     := leadingPhoton.pt",
           "leadGenPt                  := ?leadingPhoton.hasMatchedGenPhoton?leadingPhoton.matchedGenPhoton.pt:0",
           "leadEnergy                 := leadingPhoton.energy",
           "leadGenEnergy              := ?leadingPhoton.hasMatchedGenPhoton?leadingPhoton.matchedGenPhoton.energy : 0",
           "leadEta                    := leadingPhoton.eta",
           "leadScEta                  := leadingPhoton.superCluster.eta",
           "leadPhi                    := leadingPhoton.phi",
           "leadScPhi                  := leadingPhoton.superCluster.phi",
           "leadSCRawE                 := leadingPhoton.superCluster.rawEnergy",
           "leadEtaWidth               := leadingPhoton.superCluster.etaWidth",
           "leadPhiWidth               := leadingPhoton.superCluster.phiWidth",
           "leadCovIphiIphi            := leadingPhoton.sipip",
           "leadChgIsoWrtWorstVtx      := leadingPhoton.pfChgIsoWrtWorstVtx03",
           "leadPhoIso03               := leadingPhoton.pfPhoIso03",
           "leadPhoIsoCorr             := leadingPhoton.pfPhoIso03Corr",
           "leadChgIsoWrtChosenVtx     := leadingView.pfChIso03WrtChosenVtx",
           "leadHcalTowerSumEtConeDR03 := leadingPhoton.hcalTowerSumEtConeDR03",
           "leadTrkSumPtHollowConeDR03 := leadingPhoton.trkSumPtHollowConeDR03",
           "leadHadTowOverEm           := leadingPhoton.hadTowOverEm",
           "leadChargedHadronIso       := leadingPhoton.chargedHadronIso",
           "leadIDMVA                  := leadingView.phoIdMvaWrtChosenVtx",
           "leadSigmaIetaIeta          := leadingPhoton.full5x5_sigmaIetaIeta",
           "leadR9                     := leadingPhoton.full5x5_r9",
           "leadEsEffSigmaRR           := leadingPhoton.esEffSigmaRR",
           "leadS4                     := leadingPhoton.s4",
           "leadCovIEtaIPhi            := leadingPhoton.sieip",
           "leadEsEnergy               := leadingPhoton.superCluster.preshowerEnergy",
           "leadEsEnergyOverRawE       := leadingPhoton.superCluster.preshowerEnergy/leadingPhoton.superCluster.rawEnergy",
           
           ##Sub-leading Photon Variables
           "subPfPhoIso03             := subLeadingPhoton.pfPhoIso03",
           "subPfChgIsoWrtChosenVtx02 := subLeadingPhoton.pfChgIsoWrtChosenVtx02",
           "subHadronicOverEm         := subLeadingPhoton.hadronicOverEm",
           "subGenMatchType           := subLeadingPhoton.genMatchType",
           "subPt                     := subLeadingPhoton.pt",
           "subGenPt                  := ?subLeadingPhoton.hasMatchedGenPhoton?subLeadingPhoton.matchedGenPhoton.pt:0",
           "subEnergy                 := subLeadingPhoton.energy",
           "subGenEnergy              := ?subLeadingPhoton.hasMatchedGenPhoton?subLeadingPhoton.matchedGenPhoton.energy : 0",
           "subEta                    := subLeadingPhoton.eta",
           "subScEta                  := subLeadingPhoton.superCluster.eta",
           "subPhi                    := subLeadingPhoton.phi",
           "subScPhi                  := subLeadingPhoton.superCluster.phi",
           "subSCRawE                 := subLeadingPhoton.superCluster.rawEnergy",
           "subEtaWidth               := subLeadingPhoton.superCluster.etaWidth",
           "subPhiWidth               := subLeadingPhoton.superCluster.phiWidth",
           "subCovIphiIphi            := subLeadingPhoton.sipip",
           "subChgIsoWrtWorstVtx      := subLeadingPhoton.pfChgIsoWrtWorstVtx03",
           "subPhoIso03               := subLeadingPhoton.pfPhoIso03",
           "subPhoIsoCorr             := subLeadingPhoton.pfPhoIso03Corr",
           "subChgIsoWrtChosenVtx     := subLeadingView.pfChIso03WrtChosenVtx",
           "subHcalTowerSumEtConeDR03 := subLeadingPhoton.hcalTowerSumEtConeDR03",
           "subTrkSumPtHollowConeDR03 := subLeadingPhoton.trkSumPtHollowConeDR03",
           "subHadTowOverEm           := subLeadingPhoton.hadTowOverEm",
           "subChargedHadronIso       := subLeadingPhoton.chargedHadronIso",
           "subIDMVA                  := subLeadingView.phoIdMvaWrtChosenVtx",
           "subSigmaIetaIeta          := subLeadingPhoton.full5x5_sigmaIetaIeta",
           "subR9                     := subLeadingPhoton.full5x5_r9",
           "subEsEffSigmaRR           := subLeadingPhoton.esEffSigmaRR",
           "subS4                     := subLeadingPhoton.s4",
           "subCovIEtaIPhi            := subLeadingPhoton.sieip",
           "subEsEnergy               := subLeadingPhoton.superCluster.preshowerEnergy",
           "subEsEnergyOverRawE       := subLeadingPhoton.superCluster.preshowerEnergy/subLeadingPhoton.superCluster.rawEnergy"
           ]

## list of histograms to be plotted
histograms=["CMS_hgg_mass>>mass(320,100,180)",
            "subleadPt:leadPt>>ptSubVsLead(180,20,200:180,20,200)",
            "minR9>>minR9(110,0,1.1)",
            "maxEta>>maxEta[0.,0.1,0.2,0.3,0.4,0.6,0.8,1.0,1.2,1.4442,1.566,1.7,1.8,2.,2.2,2.3,2.5]"
#            histograms=["dipho_mva>>dipho_mva(100,-1,1)",]
            #"r9>>r9(110,0,1.1)",
            #"scEta>>scEta(100,-2.5,2.5)",
            ]

## define categories and associated object to dump
cfgTools.addCategory(process.diphotonDumper,
                     "Reject",
                     "abs(leadingPhoton.superCluster.eta)>=1.4442&&abs(leadingPhoton.superCluster.eta)<=1.566||abs(leadingPhoton.superCluster.eta)>=2.5"
                     "||abs(subLeadingPhoton.superCluster.eta)>=1.4442 && abs(subLeadingPhoton.superCluster.eta)<=1.566||abs(subLeadingPhoton.superCluster.eta)>=2.5",
                     -1 ## if nSubcat is -1 do not store anythings
                     )
#DIPHOTON MVA
#cfgTools.addCategories(process.diphotonDumper,
#                       [("All","1", 0),],
#                       variables=["dipho_mva:=mvaValue"],
#                       histograms=["dipho_mva>>dipho_mva(100,-1,1)",]
#                       )
# interestng categories 
cfgTools.addCategories(process.diphotonDumper,
                       ## categories definition
                       # cuts are applied in cascade. Events getting to these categories have already failed the "Reject" selectio
#                      [("GJets","1 == 1",0),
#                       [("ggh_125","1 == 1",0),
                       [("vbf_125","1 == 1",0),
                        ],
#                        variables to be dumped in trees/datasets. Same variables for all categories
                       ## if different variables wanted for different categories, can add categorie one by one with cfgTools.addCategory
                       variables=variables,
                       ## histograms to be plotted. 
                       ## the variables need to be defined first
                       histograms=histograms,
                       )

process.p1 = cms.Path(process.flashggMoreVarsDifferentialPhoIdInputsCorrection*
                      process.kinPreselDiPhotons*
#                      process.d f*
                      process.diphotonDumper)
                      


from flashgg.MetaData.JobConfig import customize
customize.setDefault("maxEvents",10000)
customize(process)

