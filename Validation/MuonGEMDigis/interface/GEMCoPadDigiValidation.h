#ifndef GEMCoPadDigiValidation_H
#define GEMCoPadDigiValidation_H

#include "Validation/MuonGEMHits/interface/GEMBaseValidation.h"
#include "DataFormats/Common/interface/Handle.h"
#include "DataFormats/GEMDigi/interface/GEMCoPadDigiCollection.h"
#include <TMath.h>


class GEMCoPadDigiValidation : public GEMBaseValidation
{
public:
  explicit GEMCoPadDigiValidation( const edm::ParameterSet& );
  ~GEMCoPadDigiValidation();
  void analyze(const edm::Event& e, const edm::EventSetup&);
  void bookHistograms(DQMStore::IBooker &, edm::Run const &, edm::EventSetup const &) override;
 private:

  MonitorElement* theCSCCoPad_xy[2][3];

  MonitorElement* theCSCCoPad_phipad[2][3];

  MonitorElement* theCSCCoPad[2][3];

  MonitorElement* theCSCCoPad_bx[2][3];

  MonitorElement* theCSCCoPad_zr[2][3];

};

#endif
