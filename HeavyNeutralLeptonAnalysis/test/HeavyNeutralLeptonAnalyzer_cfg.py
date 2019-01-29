from os import path as path
import FWCore.ParameterSet.Config as cms

from PhysicsTools.PatUtils.tools.runMETCorrectionsAndUncertainties import runMetCorAndUncFromMiniAOD
from RecoEgamma.EgammaTools.EgammaPostRecoTools import setupEgammaPostRecoSeq
from RecoEgamma.ElectronIdentification.egmGsfElectronIDs_cfi import *
from PhysicsTools.SelectorUtils.centralIDRegistry import central_id_registry
from RecoEgamma.ElectronIdentification.ElectronMVAValueMapProducer_cfi import *
from HNL.HeavyNeutralLeptonAnalysis.ele_Sequence_cff import addElectronSequence

debugLevel    = -1 

isMC_         = True
isMCSignal_   = False
hasLHE_       = True #Only for MC with Matrix Element generators

algorithm     = "AK4PFchs"

GT_MC = '94X_mc2017_realistic_v10'#94X_mc2017_realistic_v14
GT_DATA = '92X_dataRun2_2017Repro_v4'#94X_dataRun2_v6

GT      =  GT_MC if isMC_ else GT_DATA


process = cms.Process("AnalysisProc")
process.load("RecoEgamma.ElectronIdentification.ElectronMVAValueMapProducer_cfi")
process.load("FWCore.MessageService.MessageLogger_cfi")
process.load('Configuration.EventContent.EventContent_cff')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')
process.load('Configuration.StandardSequences.Services_cff')
process.load("TrackingTools.TransientTrack.TransientTrackBuilder_cfi")

#b-tagging
process.load('RecoBTag/Configuration/RecoBTag_cff')

process.MessageLogger.cerr.FwkReport.reportEvery = 1

import FWCore.PythonUtilities.LumiList as LumiList
LumiList.LumiList().getVLuminosityBlockRange()

#from Configuration.AlCa.GlobalTag import GlobalTag
from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, GT)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(100)
)
process.source = cms.Source("PoolSource", 
                            fileNames =  cms.untracked.vstring(
'root://xrootd-cms.infn.it///store/mc/RunIIFall17MiniAODv2/ttWJets_TuneCP5_13TeV_madgraphMLM_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v2/50000/FE8D896F-386C-E811-AAAB-001E6779264E.root' 
#store/mc/RunIIFall17MiniAOD/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/94X_mc2017_realistic_v10-v1/70000/FEFA6784-D0F6-E711-A31A-008CFAC93ECC.root'
#'root://cms-xrd-global.cern.ch//store/user/tomc/heavyNeutrinoMiniAOD/Fall17/displaced/HeavyNeutrino_lljj_M-5_V-0.00836660026534_mu_massiveAndCKM_LO/heavyNeutrino_1.root'
#'root://cms-xrd-global.cern.ch//store/user/tomc/heavyNeutrinoMiniAOD/Fall17/displaced/HeavyNeutrino_lljj_M-5_V-0.00836660026534_mu_massiveAndCKM_LO/heavyNeutrino_1.root',
#'root://cms-xrd-global.cern.ch//store/user/tomc/heavyNeutrinoMiniAOD/Fall17/displaced/HeavyNeutrino_lljj_M-5_V-0.00836660026534_mu_massiveAndCKM_LO/heavyNeutrino_1.root',
#'root://cms-xrd-global.cern.ch//store/user/tomc/heavyNeutrinoMiniAOD/Fall17/displaced/HeavyNeutrino_lljj_M-5_V-0.00836660026534_mu_massiveAndCKM_LO/heavyNeutrino_1.root',
#'root://cms-xrd-global.cern.ch//store/user/tomc/heavyNeutrinoMiniAOD/Fall17/displaced/HeavyNeutrino_lljj_M-5_V-0.00836660026534_mu_massiveAndCKM_LO/heavyNeutrino_1.root',
#'root://cms-xrd-global.cern.ch//store/user/tomc/heavyNeutrinoMiniAOD/Fall17/displaced/HeavyNeutrino_lljj_M-5_V-0.00836660026534_mu_massiveAndCKM_LO/heavyNeutrino_1.root',
#'root://cms-xrd-global.cern.ch//store/user/tomc/heavyNeutrinoMiniAOD/Fall17/displaced/HeavyNeutrino_lljj_M-5_V-0.00836660026534_mu_massiveAndCKM_LO/heavyNeutrino_1.root'
#'root://xrootd-cms.infn.it//store/mc/RunIIFall17MiniAOD/DYJetsToLL_M-50_Zpt-150toInf_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/RECOSIMstep_94X_mc2017_realistic_v10-v1/50000/EE9CC3E0-0DED-E711-BCAC-00E081CB560C.root'
#root://xrootd-cms.infn.it//WZTo3LNu_0Jets_MLL-4to50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM
#'root://xrootd-cms.infn.it//store/mc/RunIISummer16MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/4E597432-24BE-E611-ACBB-00266CFFBFC0.root'
#cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv2/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/4E597432-24BE-E611-ACBB-00266CFFBFC0.root'
#'root://cms-xrd-global.cern.ch//store/data/Run2016G/SingleMuon/MINIAOD/23Sep2016-v1/1110000/72446D9C-D89C-E611-9060-002590A3C984.root'
#'file:/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_lljj_M-2_V-0.00316227766017_mu_massiveAndCKM_LO/heavyNeutrino_40.root'
#'file:/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17_aug2018/displaced/HeavyNeutrino_lljj_M-8_V-0.004472135955_mu_massiveAndCKM_LO/heavyNeutrino_96.root'
#'file:/pnfs/iihe/cms/store/user/tomc/heavyNeutrinoMiniAOD/Moriond17/displaced/HeavyNeutrino_lljj_M-1_V-0.00836660026534_e_onshell_pre2017_leptonFirst_NLO/heavyNeutrino_96.root'
))
process.TFileService = cms.Service("TFileService", fileName = cms.string("Analysis_output.root"))
process.load('HNL.HeavyNeutralLeptonAnalysis.MetaNtuplizer_cfi')
process.metaTree.isMC = isMC_
process.metaTree.weightsSrc = cms.InputTag('externalLHEProducer')
process.metaTree.globalTag = GT
process.metaTree.args = cms.string('USELESS') #FILL ME!
process.metaTree.hasLHE = cms.bool(hasLHE_ and isMC_)

process.load('HNL.DisplacedAdaptiveVertexFinder.displacedInclusiveVertexing_cff')

addElectronSequence(process)

process.load("CondCore.CondDB.CondDB_cfi")

process.load("PhysicsTools.PatAlgos.producersLayer1.jetUpdater_cff")

process.jetCorrFactors = process.updatedPatJetCorrFactors.clone(
    src = cms.InputTag("slimmedJets"),
    levels = ['L1FastJet', 
              'L2Relative', 
              'L3Absolute',
              'L2L3Residual'],
    payload = 'AK4PFchs') 

process.slimmedJetsJEC = process.updatedPatJets.clone(
    jetSource = cms.InputTag("slimmedJets"),
    jetCorrFactorsSource = cms.VInputTag(cms.InputTag("jetCorrFactors"))
    )

runMetCorAndUncFromMiniAOD(process, isData = not(isMC_), jetCollUnskimmed = "slimmedJetsJEC", postfix="NewJEC")

from PhysicsTools.SelectorUtils.tools.vid_id_tools import DataFormat, switchOnVIDElectronIdProducer, setupAllVIDIdsInModule, setupVIDElectronSelection
switchOnVIDElectronIdProducer(process, DataFormat.MiniAOD)

process.egmGsfElectronIDs.physicsObjectSrc = "slimmedElectrons"

id_modules = [
    'RecoEgamma.ElectronIdentification.Identification.cutBasedElectronID_Fall17_94X_V2_cff',
    'RecoEgamma.ElectronIdentification.Identification.mvaElectronID_Fall17_noIso_V1_cff',
    'RecoEgamma.ElectronIdentification.Identification.mvaElectronID_Fall17_iso_V1_cff'
    ]

for mod in id_modules:
    setupAllVIDIdsInModule(process, mod, setupVIDElectronSelection)

    setupEgammaPostRecoSeq(process,
                           runVID=False, #saves CPU time by not needlessly re-running VID, if you want the Fall17V2 IDs, set this to True or remove (default is True)
                           era='2017-Nov17ReReco')
    
process.HeavyNeutralLepton = cms.EDAnalyzer('HeavyNeutralLeptonAnalysis',
                                            debugLevel            = cms.int32(debugLevel),
                                            isMC                  = cms.bool(isMC_),
                                            isMCSignal            = cms.bool(isMCSignal_),
                                            vtxSrc                = cms.InputTag("offlineSlimmedPrimaryVertices"),
                                            rho                   = cms.InputTag("fixedGridRhoFastjetAll"),#cambiato tag?
                                            muonSrc               = cms.InputTag("slimmedMuons"),
                                            electronSrc           = cms.InputTag("slimmedElectrons"),
                                            recHitCollectionEBSrc = cms.InputTag("reducedEgamma","reducedEBRecHits"),
                                            recHitCollectionEESrc = cms.InputTag("reducedEgamma","reducedEERecHits"),
                                            tauSrc                = cms.InputTag("slimmedTaus"),
                                            packCandSrc           = cms.InputTag("packedPFCandidates"),
                                            jetSrc                = cms.InputTag("slimmedJetsJEC"),
                                            pfMETSrc              = cms.InputTag("slimmedMETs"),
                                            triggerResultSrc      = cms.InputTag("TriggerResults","","HLT"),
                                            metFilterResultSrc    = cms.InputTag("TriggerResults","","PAT"),
                                            genParticleSrc        = cms.InputTag("prunedGenParticles"),
                                            genEventInfoProduct   = cms.InputTag("generator"),
                                            PUInfo                = cms.InputTag("slimmedAddPileupInfo"),
                                            lheEventProducts      = cms.InputTag("externalLHEProducer"),
                                            SecondaryVertices     = cms.InputTag("displacedInclusiveSecondaryVertices"), 
                                            bDiscbb = cms.vstring("pfDeepCSVJetTags:probb"),
                                            bDiscbbb = cms.vstring("pfDeepCSVJetTags:probbb"),
                                            bDiscbc = cms.vstring("pfDeepCSVJetTags:probc"),
                                            #electronsMva          = cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-Fall17-94X-V2-veto"),#egmGsfElectronIDs:mvaEleID-Fall17-iso-V1-wp90 #egmGsfElectronIDs:cutBasedElectronID-Fall17-94X-V2-veto mvaEleID-Fall17-noIso-V1-wp90
                                            electronsVeto  = cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-Fall17-94X-V2-veto"),
                                            electronsLoose = cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-Fall17-94X-V2-loose"),
                                            electronsMedium= cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-Fall17-94X-V2-medium"),
                                            electronsTight = cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-Fall17-94X-V2-tight")
                                            )

process.p = cms.Path(
    #process.egmGsfElectronIDTask 
    process.egmGsfElectronIDSequence
    #*process.egammaPostRecoSeq
    #*process.egmGsfElectronIDs
    *process.electronMVAValueMapProducer
    #*process.egmGsfElectronIDs
    *process.btagging
    *process.metaTree
    *process.displacedInclusiveVertexing
    *process.ele_Sequence
    *process.jetCorrFactors
    *process.slimmedJetsJEC
    *process.HeavyNeutralLepton
    )
