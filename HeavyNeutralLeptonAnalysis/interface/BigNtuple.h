#ifndef HNL_HeavyNeutralLeptonAnalysis_BigNtuple
#define HNL_HeavyNeutralLeptonAnalysis_BigNtuple
/* 
	 Class: BigNtuple
	 Simple interface class to hide all the ROOT I/O from the plugin and make it more readable
*/

#include <vector>

#include "TTree.h"

#include "DataFormats/PatCandidates/interface/Muon.h"
#include "DataFormats/PatCandidates/interface/Electron.h"
#include "DataFormats/PatCandidates/interface/Jet.h"
#include "DataFormats/PatCandidates/interface/MET.h"
#include "FWCore/Common/interface/TriggerNames.h"
#include "DataFormats/Common/interface/TriggerResults.h"
#include "DataFormats/Math/interface/deltaR.h"
#include "DataFormats/VertexReco/interface/VertexFwd.h"
#include "FWCore/Framework/interface/Event.h"

class BigNtuple {
public:
	BigNtuple(){} //default, empty constructor

	void set_evtInfo(TTree* tree);
	void fill_evtInfo(const edm::EventID& id);

	void set_pvInfo(TTree* tree);
	void fill_pvInfo(const reco::VertexCollection& pvs);

	void set_trigInfo(TTree* tree);
	void fill_trigInfo(const edm::TriggerResults& triggerResults, const edm::TriggerNames& trigNames);

	void set_svInfo(TTree* tree);
        void fill_svInfo(const reco::Vertex& bestVertex, const reco::Vertex& pv);

	void set_muInfo(TTree* tree);
        void fill_muInfo(const pat::Muon& mu, const reco::Vertex& pv);
	
	void set_jetInfo(TTree* tree);
	void fill_jetInfo(const pat::Jet& jet);

        void set_metInfo(TTree* tree);
        void fill_metInfo(const pat::MET& met);
	 
	void reset() {
	  BigNtuple dummy; //create a new one
	  *this = dummy; //use assignment to reset
	}

private:
	unsigned int lumi_ = 0;
	unsigned int run_ = 0;
	unsigned long long evt_ = 0;
	
	// primary vertex infos  -- they shouldn't be vector 
	float pvX_ = -1000;
	float pvY_ = -1000;
	float pvZ_ = -1000;
	float pvXErr_ = -1000;
	float pvYErr_ = -1000;
	float pvZErr_ = -1000;
	float pvMass_ = -1000;
	float pvLxy_  = -1000;
	float pvLxyz_ = -1000;
	float pvLxySig_  = -1000;
	float pvLxyzSig_ = -1000;
	float pvChi2_ = -1000;
	int pvNTrack_ = -1000;
	float pvSumPtSq_ = -1000;
	int numberPV_    = -1000;

	//trigger infos

	bool passIsoTk18_  = 0;
	bool passIsoTk20_  = 0;
	bool passIsoTk22_  = 0;
	bool passIsoTk24_  = 0;
	bool passIsoTk27_  = 0;
	bool passIsoTk17e_ = 0;
	bool passIsoTk22e_ = 0;
	
	bool passIsoMu18_  = 0;
	bool passIsoMu20_  = 0;
	bool passIsoMu22_  = 0;
	bool passIsoMu24_  = 0;
	bool passIsoMu27_  = 0;
	bool passIsoMu17e_ = 0;
	bool passIsoMu22e_ = 0;
	bool passTkMu17_   = 0;
	bool passTkMu20_   = 0;
	
	bool passIsoMu24All_ = 0;
	bool passIsoMu27All_ = 0;
	
	bool passDoubleMu17TrkIsoMu8_     = 0;
	bool passDoubleMu17TrkIsoTkMu8_   = 0;
	bool passDoubleTkMu17TrkIsoTkMu8_ = 0;

 
	//secondary verteces info

	std::vector<int>   sv_TrackSize_;
	std::vector<float> sv_LXYSig_;
	std::vector<float> sv_LXYZSig_;
	std::vector<float> sv_LXY_;
	std::vector<float> sv_LXYZ_;
	std::vector<float> sv_mass_;
	std::vector<int>   sv_charge_;
	std::vector<float> sv_eta_;
	std::vector<float> sv_phi_;
	std::vector<float> sv_pt_;
	std::vector<float> sv_p_;
	std::vector<float> sv_Beta_;
	std::vector<float> sv_Gamma_;
	std::vector<float> sv_CTau0_;
	std::vector<float> sv_NDof_;
	std::vector<float> sv_Chi2_;
	std::vector<float> sv_Angle3D_;
	std::vector<float> sv_Angle2D_;

	std::vector<std::vector<int  > > sv_tracks_charge_;
	std::vector<std::vector<float> > sv_tracks_eta_;
	std::vector<std::vector<float> > sv_tracks_phi_;
	std::vector<std::vector<float> > sv_tracks_pt_;
	std::vector<std::vector<float> > sv_tracks_dxySig_;
	std::vector<std::vector<float> > sv_tracks_dxy_;
	std::vector<std::vector<float> > sv_tracks_dxyz_;

	std::vector<int  > sv_tracks_Sumcharge_;
	std::vector<float> sv_tracks_Sumpt_;


	//muon infos
	std::vector<float> mu_en_ ;
	std::vector<float> mu_pt_ ;
	std::vector<float> mu_eta_ ;
	std::vector<float> mu_phi_ ;
	std::vector<float> mu_et_ ;
	std::vector<float> mu_charge_ ;
	std::vector<float> mu_trackiso_ ;
	std::vector<float> mu_pfSumChargedHadronPt_ ;
	std::vector<float> mu_pfSumNeutralHadronEt_ ;
	std::vector<float> mu_PFSumPhotonEt_ ;
	std::vector<float> mu_pfSumPUPt_ ;
	std::vector<int>   mu_numberOfValidMuonHits_ ;
	std::vector<float> mu_emIso_ ;
	std::vector<float> mu_hadIso_ ;
	std::vector<float> mu_normalizedChi2_ ;
	std::vector<int>   mu_numberOfMatchedStations_ ;
	std::vector<int>   mu_numberOfValidPixelHits_ ;
	std::vector<int>   mu_numberOftrackerLayersWithMeasurement_ ;
	std::vector<int>   mu_numberOfpixelLayersWithMeasurement_ ;
	std::vector<int>   mu_TrackQuality_ ;
	std::vector<int>   mu_InnerTrackQuality_ ;
	std::vector<float> mu_pxTunePMuonBestTrack_ ;
	std::vector<float> mu_pyTunePMuonBestTrack_ ;
	std::vector<float> mu_pzTunePMuonBestTrack_ ;
	std::vector<float> mu_pTunePMuonBestTrack_ ;
	std::vector<float> mu_etaTunePMuonBestTrack_ ;
	std::vector<float> mu_LXYZ_ ;
	std::vector<float> mu_LXY_ ;
	std::vector<float> mu_ptTunePMuonBestTrack_ ;
	std::vector<float> mu_phiTunePMuonBestTrack_ ;
	std::vector<float> mu_thetaTunePMuonBestTrack_ ;
	std::vector<float> mu_chargeTunePMuonBestTrack_ ;
	std::vector<float> mu_dPToverPTTunePMuonBestTrack_ ;
	std::vector<float> mu_absdxyTunePMuonBestTrack_ ;
	std::vector<float> mu_absdxyErrorTunePMuonBestTrack_ ;
	std::vector<float> mu_absdxySigTunePMuonBestTrack_ ;
	std::vector<float> mu_absdzTunePMuonBestTrack_ ;
	std::vector<float> mu_absdzErrorTunePMuonBestTrack_ ;
	std::vector<float> mu_absdzSigTunePMuonBestTrack_ ;
	std::vector<float> mu_recoDeltaBeta_ ;
	std::vector<float> mu_recoiso_ ;
	std::vector<float> mu_isGlobalMuon_ ;
	std::vector<float> mu_isStandAloneMuon_ ;
	std::vector<float> mu_isPF_ ;
	std::vector<float> mu_isRPCMuon_ ;
	std::vector<float> mu_isTrackerMuon_ ;
	std::vector<float> mu_isGoodMuon_ ;
	std::vector<float> mu_isSoftMuon_ ;
	std::vector<float> mu_isLoose_ ;
	std::vector<float> mu_isTightMuon_ ;
	std::vector<int>    mu_STAnHits_ ;
	std::vector<int>    mu_STAnLost_ ;
	std::vector<int>    mu_STAnStationsWithAnyHits_ ;
	std::vector<int>    mu_STAnCscChambersWithAnyHits_ ;
	std::vector<int>    mu_STAnDtChambersWithAnyHits_ ;
	std::vector<int>    mu_STAnRpcChambersWithAnyHits_ ;
	std::vector<int>    mu_STAinnermostStationWithAnyHits_ ;
	std::vector<int>    mu_STAoutermostStationWithAnyHits_ ;
	std::vector<int>    mu_STAnStationsWithValidHits_ ;
	std::vector<int>    mu_STAnCscChambersWithValidHits_ ;
	std::vector<int>    mu_STAnDtChambersWithValidHit_ ;
	std::vector<int>    mu_STAnRpcChambersWithValidHits_ ;
	std::vector<int>    mu_STAnValidMuonHits_ ;
	std::vector<int>    mu_STAnValidCscHits_ ;
	std::vector<int>    mu_STAnValidDtHits_ ;
	std::vector<int>    mu_STAnValidRpcHits_ ;
	std::vector<int>    mu_STAinnermostStationWithValidHits_ ;
	std::vector<int>    mu_STAoutermostStationWithValidHits_ ;
	std::vector<float>  mu_STATofDirection_ ;
	std::vector<float>  mu_STATofNDof_ ;
	std::vector<float>  mu_STATofTimeAtIpInOut_ ;
	std::vector<float>  mu_STATofTimeAtIpInOutErr_ ;
	std::vector<float>  mu_STATofTimeAtIpOutIn_ ;
	std::vector<float>  mu_STATofTimeAtIpOutInErr_ ;
	//std::vector<float>  mu_SecondGenMatch_ ;
	//std::vector<float>  mu_FirstGenMatch_ ;

	//jet info

	std::vector<float>   jet_charge_ ;
	std::vector<float>   jet_et_ ;
	std::vector<float>   jet_pt_ ;
	std::vector<float>   jet_eta_ ;
	std::vector<float>   jet_phi_ ;
	std::vector<float>   jet_theta_ ;
	std::vector<float>   jet_en_ ;
	std::vector<float>   jet_chargedEmEnergy_ ;
	std::vector<float>   jet_neutralEmEnergyFraction_ ;
	std::vector<float>   jet_chargedHadronEnergy_ ;
	std::vector<float>   jet_neutralHadronEnergyFraction_ ;
	std::vector<float>   jet_chargedMuEnergy_ ;
	std::vector<float>   jet_chargedMuEnergyFraction_ ;
	std::vector<float>   jet_chargedMultiplicity_ ;
	std::vector<float>   jet_numberOfDaughters_ ;
	std::vector<float>   jet_muonEnergy_ ;
	std::vector<float>   jet_muonEnergyFraction_ ;
	std::vector<float>   jet_muonMultiplicity_ ;
	std::vector<float>   jet_neutralEmEnergy_ ;
	std::vector<float>   jet_neutralHadronEnergy_ ;
	std::vector<float>   jet_neutralHadronMultiplicity_ ;
	std::vector<float>   jet_neutralMultiplicity_ ;

	//MET info
	
	float  pfMet_et_ = -1000;
	float  pfMet_pt_ = -1000;
	float  pfMet_phi_ = -1000;
	float  pfMet_en_ = -1000;
	float  pfMet_px_ = -1000;
	float  pfMet_py_ = -1000;
	float  pfMet_pz_ = -1000;
	float  pfMet_sumEt_ = -1000;
	float  caloMet_pt_ = -1000;
	float  caloMet_phi_ = -1000;

}; 


#endif
