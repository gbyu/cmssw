#ifndef GEMPadDigiValidation_H
#define GEMPadDigiValidation_H

#include "Validation/MuonGEMHits/interface/GEMBaseValidation.h"
#include "DataFormats/GEMDigi/interface/GEMPadDigiCollection.h"

#include "DataFormats/Common/interface/Handle.h"
#include <TMath.h>
class GEMPadDigiValidation : public GEMBaseValidation
{
public:
  explicit GEMPadDigiValidation( const edm::ParameterSet& );
  ~GEMPadDigiValidation();
  void analyze(const edm::Event& e, const edm::EventSetup&);
  void bookHistograms(DQMStore::IBooker &, edm::Run const &, edm::EventSetup const &) override;
 private:

  MonitorElement* theCSCPad_xy[2][3][2];
  MonitorElement* theCSCPad_phipad[2][3][2];
  MonitorElement* theCSCPad[2][3][2];
  MonitorElement* theCSCPad_bx[2][3][2];
  MonitorElement* theCSCPad_zr[2][3][2];

};

#endif
