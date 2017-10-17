#ifndef TTPIXELTRACK_H
#define TTPIXELTRACK_H

/*
 *
 * Modified by G. Yu, 16 Oct 2017
 * from CMSSW_6_2_0_SLHC12:DataFormats/L1TrackTrigger/interface/TTPixelTrack.h
 * 
 * Original code by Anders Ryd
 */


#include "DataFormats/Common/interface/Ref.h"
#include "DataFormats/Common/interface/Ptr.h"
#include "DataFormats/L1Trigger/interface/L1Candidate.h"
#include "DataFormats/L1TrackTrigger/interface/TTTrack.h"
#include "DataFormats/L1TrackTrigger/interface/TTTypes.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"

class TTPixelTrack
{

public:
  TTPixelTrack();  // Constructors
  ~TTPixelTrack();  // Destructors

  // Track momentum
  GlobalVector getMomentum() const;
  
  /// Track curvature
  double getRInv() const;
  
  /// POCA
  GlobalPoint getPOCA() const;

  // L1Track
  edm::Ref<std::vector< TTTrack< Ref_Phase2TrackerDigi_> >, TTTrack< Ref_Phase2TrackerDigi_> >  getL1Track() const;

  //typedef TTTrack< Ref_Phase2TrackerDigi_ >  L1TTTrackType;
  //typedef std::vector< L1TTTrackType > L1TTTrackCollection;
  
  /// Chi2
  double       getChi2() const;
  double       getChi2Red() const;

  /// Errors
    
  double getSigmaRInv() const {return theSigmaRInv;}
  double getSigmaPhi0() const {return theSigmaPhi0;}
  double getSigmaD0() const {return theSigmaD0;}
  double getSigmaT() const {return theSigmaT;}
  double getSigmaZ0() const {return theSigmaZ0;}
  int getNhit() const {return thenhit;}

  void init(const edm::Ref<std::vector<TTTrack<Ref_Phase2TrackerDigi_> >, 
	    TTTrack<Ref_Phase2TrackerDigi_> >& aL1Track,	    
	    const GlobalVector& aMomentum,
	    const GlobalPoint&  aPOCA,
	    double aRInv,
	    double aChi2,
	    int nhit,
	    double sigmarinv,
	    double sigmad0,
	    double sigmaphi0,
	    double sigmat,
	    double sigmaz0);
  
  /// Information
  std::string print( unsigned int i = 0 ) const;


private:

  edm::Ref<std::vector<TTTrack< Ref_Phase2TrackerDigi_ > >, TTTrack< Ref_Phase2TrackerDigi_> > theL1Track;
  GlobalVector theMomentum;
  GlobalPoint  thePOCA;
  double       theRInv;
  double       theChi2;
  int          thenhit;
  double       theSigmaRInv;
  double       theSigmaPhi0;
  double       theSigmaD0;
  double       theSigmaT;
  double       theSigmaZ0;
};


 TTPixelTrack::TTPixelTrack()
{
  //theStubRefs.clear();
  theMomentum=GlobalVector(0.0,0.0,0.0);
  theRInv=0.0;
  thePOCA=GlobalPoint(0.0,0.0,0.0);
  theChi2=0.0;
}

/// Destructor
TTPixelTrack::~TTPixelTrack(){}

void TTPixelTrack::init(const edm::Ref<std::vector<TTTrack<Ref_Phase2TrackerDigi_> >, TTTrack<Ref_Phase2TrackerDigi_> >& aL1Track,	    
			const GlobalVector& aMomentum,
			const GlobalPoint&  aPOCA,
			double aRInv,
			double aChi2,
			int    anhit,
			double sigmarinv,
			double sigmad0,
			double sigmaphi0,
			double sigmat,
			double sigmaz0){

  theL1Track=aL1Track;
  theMomentum=aMomentum;
  thePOCA=aPOCA;
  theRInv=aRInv;
  theChi2=aChi2;
  thenhit=anhit;
  theSigmaRInv=sigmarinv;
  theSigmaPhi0=sigmad0;
  theSigmaD0=sigmaphi0;
  theSigmaT=sigmat;
  theSigmaZ0=sigmaz0;


}

edm::Ref<std::vector<TTTrack<Ref_Phase2TrackerDigi_> >, TTTrack<Ref_Phase2TrackerDigi_> > TTPixelTrack::getL1Track() const{

  return theL1Track;

}


GlobalVector TTPixelTrack::getMomentum() const{

  return theMomentum;

} 




double TTPixelTrack::getRInv() const {

  return theRInv;

}



GlobalPoint TTPixelTrack::getPOCA() const
{

  return thePOCA;

}


/// Chi2 
double TTPixelTrack::getChi2() const
{

  return theChi2;

}


/// Chi2 reduced
double TTPixelTrack::getChi2Red() const
{

  return 0.0;
  //return theChi25Par/( 2*theStubRefs.size() - 5 );
  //Need to fix when we also store pixel refs.

}



/// Information
std::string TTPixelTrack::print( unsigned int i ) const
{
  std::string padding("");
  for ( unsigned int j = 0; j != i; ++j )
  {
    padding+="\t";
  }

  std::stringstream output;
  output<<padding<<"TTPixelTrack:\n";
  padding+='\t';
  output << '\n';

  //unsigned int iStub = 0;
  //typename std::vector< edm::Ref< edmNew::DetSetVector< TTStub< T > >, TTStub< T > > >::const_iterator stubIter;
  //for ( stubIter = theStubRefs.begin();
  //      stubIter!= theStubRefs.end();
  //      ++stubIter )
  //{
  //  output << padding << "stub: " << iStub++ << ", DetId: " << ((*stubIter)->getDetId()).rawId() << '\n';
  //}

  output << ", z-vertex: " << thePOCA.z() << " (cm), transverse momentum " << theMomentum.perp() << " (GeV/c)";
  //output << ", red. chi2 " << this->getChi2Red() << '\n';

  return output.str();
}




std::ostream& operator << ( std::ostream& os, const TTPixelTrack& aTTPixelTrack ) { return ( os << aTTPixelTrack.print() ); }


#endif

