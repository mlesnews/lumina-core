# Legal Verification Checklist

## Business Registration Verification

### Checklist
- [ ] Verify business entity is properly registered
- [ ] Confirm registration number/documentation
- [ ] Check registration expiration date (if applicable)
- [ ] Verify registered agent information
- [ ] Confirm business name is correct
- [ ] Check for any pending compliance issues

### Where to Check
- **State Secretary of State website**: Search business database
- **Business registration documents**: Review original filing
- **Registered agent**: Confirm contact information is current

### Estimated Time: 30 minutes

---

## EIN Verification

### Checklist
- [ ] Confirm EIN is obtained from IRS
- [ ] Verify EIN is documented
- [ ] Check EIN letter from IRS (CP 575)
- [ ] Store EIN securely in Azure Vault
- [ ] Verify EIN matches business name
- [ ] Confirm EIN is used on all business documents

### Storage
- ✅ Store in Azure Vault: `business-ein`
- ❌ Do NOT store in files or code

### Estimated Time: 15 minutes

---

## Business Licenses

### State License
- [ ] Check state business license requirements
- [ ] Verify if license is required for your business type
- [ ] Apply for license if needed
- [ ] Document license number
- [ ] Note expiration date
- [ ] Set reminder for renewal

### Local/City License
- [ ] Check city/county business license requirements
- [ ] Apply for local license if required
- [ ] Document license number
- [ ] Note expiration date

### Industry-Specific Licenses
- [ ] Research industry-specific license requirements
- [ ] Apply for required licenses
- [ ] Document all license numbers
- [ ] Set up renewal reminders

### Estimated Time: 1-2 hours (varies by location)

---

## Insurance

### General Liability Insurance
- [ ] Research coverage needs
- [ ] Get quotes from 3+ providers
- [ ] Compare coverage and costs
- [ ] Purchase policy
- [ ] Document policy number and expiration
- [ ] Store in Azure Vault

### Professional Liability (E&O)
- [ ] Determine if needed for your business
- [ ] Get quotes if applicable
- [ ] Purchase if required
- [ ] Document policy information

### Workers Compensation
- [ ] Required if you have employees
- [ ] Research state requirements
- [ ] Purchase if applicable

### Business Property Insurance
- [ ] Assess property/assets to insure
- [ ] Get quotes
- [ ] Purchase policy

### Cyber Liability Insurance
- [ ] Consider if handling customer data
- [ ] Get quotes if applicable
- [ ] Purchase if recommended

### Estimated Time: 2-3 hours

---

## Tax Registration

### State Tax Registration
- [ ] Register for state income tax (if applicable)
- [ ] Register for state sales tax (if applicable)
- [ ] Get state tax ID number
- [ ] Document registration numbers

### Local Tax Registration
- [ ] Check local tax requirements
- [ ] Register if required
- [ ] Document registration

### Sales Tax Permit
- [ ] Determine if you need sales tax permit
- [ ] Apply for permit if selling products/services
- [ ] Document permit number
- [ ] Set up sales tax collection system

### Employer Tax Registration
- [ ] Register for employer taxes (if hiring)
- [ ] Set up payroll tax system
- [ ] Document registration numbers

### Estimated Time: 1-2 hours

---

## Legal Verification Summary

### Priority 1 (Do First)
1. ✅ Business registration verification
2. ✅ EIN verification and storage
3. ✅ Required business licenses

### Priority 2 (Do Soon)
4. ⏳ General liability insurance
5. ⏳ Tax registrations
6. ⏳ Professional liability insurance (if applicable)

### Priority 3 (As Needed)
7. ⏳ Additional insurance types
8. ⏳ Industry-specific licenses
9. ⏳ Employer registrations (when hiring)

---

## Storage of Legal Documents

### In Azure Vault (Sensitive)
- EIN
- Tax ID numbers
- License numbers
- Insurance policy numbers

### In Secure File System
- Registration documents
- License certificates
- Insurance certificates
- Tax registration confirmations

### File Locations
- `data/legal/registration/` - Business registration docs
- `data/legal/licenses/` - License certificates
- `data/legal/insurance/` - Insurance documents
- `data/legal/taxes/` - Tax registration docs

---

## Compliance Reminders

### Set Up Reminders For
- License renewals
- Insurance renewals
- Tax filing deadlines
- Annual report filings
- Registration updates

### Recommended Tools
- Calendar reminders
- Task management system
- N8N automation workflows

---

**Created:** 2026-01-16T06:01:19.919094
**Next Review:** February 2026
