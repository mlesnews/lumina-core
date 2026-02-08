# 🚀 Startup Quick Start Guide

## First 24 Hours Checklist

### Hour 1-2: Legal & Financial
- [ ] Verify business registration
- [ ] Confirm EIN is documented
- [ ] Set up business bank account (if not done)
- [ ] Get business credit card application started

### Hour 3-4: Communication Setup
- [ ] Complete Twilio setup:
  - Get Account SID from: https://console.twilio.com/us1/develop/account
  - Get Auth Token from: https://console.twilio.com/us1/develop/account/settings/api-keys
  - Get trial phone number
  - Run: `python scripts/python/setup_twilio_credentials.py`
- [ ] Test SMS/voice functionality
- [ ] Set up email signature

### Hour 5-6: Operations Setup
- [ ] Run: `python scripts/python/setup_business_operations.py`
- [ ] Edit `config/business.json` with company info
- [ ] Store sensitive info in Azure Vault
- [ ] Review templates in `templates/` directory

### Hour 7-8: Documentation
- [ ] Create first SOP using `templates/sop_template.md`
- [ ] Set up client onboarding process
- [ ] Document current workflows

---

## First Week Priorities

### Day 1-2: Foundation
1. ✅ Legal structure verified
2. ✅ Financial accounts set up
3. ✅ Communication systems operational
4. ✅ Basic operations structure created

### Day 3-4: Systems
1. ✅ Task management system in place
2. ✅ Client database structure ready
3. ✅ Invoice template ready
4. ✅ Proposal template ready

### Day 5-7: Optimization
1. ✅ Automation workflows identified
2. ✅ Documentation started
3. ✅ Security audit completed
4. ✅ Backup systems verified

---

## Essential Commands

### Setup Commands
```powershell
# Setup business operations
python scripts/python/setup_business_operations.py

# Setup Twilio credentials
python scripts/python/setup_twilio_credentials.py

# Generate invoice
python scripts/python/generate_invoice.py

# Track expenses
python scripts/python/track_expenses.py
```

### File Locations
- **Business Config**: `config/business.json`
- **Client Database**: `data/clients/clients_database.json`
- **Tasks**: `data/tasks.json`
- **Expenses**: `data/financial/expenses.json`
- **Templates**: `templates/`

---

## Quick Reference

### Azure Vault Secrets
Store these in Azure Vault:
- `twilio-account-sid`
- `twilio-auth-token`
- `twilio-phone-number`
- `business-ein`
- `business-bank-account`
- `business-address`
- `business-phone`
- `business-email`

### Key URLs
- Twilio Console: https://console.twilio.com
- Twilio Account: https://console.twilio.com/us1/develop/account
- Twilio API Keys: https://console.twilio.com/us1/develop/account/settings/api-keys
- Twilio Phone Numbers: https://console.twilio.com/us1/develop/phone-numbers/manage/search

### Templates
- Invoice: `templates/invoice_template.html`
- Proposal: `templates/proposal_template.md`
- SOP: `templates/sop_template.md`
- Client Onboarding: `templates/client_onboarding_checklist.md`

---

## Emergency Contacts & Resources

### Support
- Twilio Support: https://support.twilio.com
- Azure Support: https://azure.microsoft.com/support

### Documentation
- Startup Action Plan: `docs/STARTUP_ACTION_PLAN.md`
- Week 1 Checklist: `docs/STARTUP_WEEK_1_CHECKLIST.md`
- Security Policy: `docs/SECURITY_REDACTION_POLICY.md`

---

## Success Metrics

Track these weekly:
- [ ] Expenses tracked
- [ ] Invoices sent
- [ ] Clients onboarded
- [ ] Tasks completed
- [ ] Revenue generated
- [ ] Systems operational

---

**Remember:** Start simple, iterate, and improve. Don't try to perfect everything on day one!
