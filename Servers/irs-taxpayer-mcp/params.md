(1) taxYear
 Tax year used for the federal tax calculation.
 Required. No default value.

(2) filingStatus
 Filing status used for the tax calculation.
 Required. No default value.

(3) grossIncome
 Total gross income in USD.
 Required. No default value.

(4) w2Income
 W-2 wage income included in the calculation.
 Optional. No default value.

(5) selfEmploymentIncome
 Self-employment income included in the calculation.
 Optional. No default value.

(6) capitalGains
 Long-term capital gains or losses included in the calculation.
 Optional. No default value.

(7) capitalGainsLongTerm
 Flag indicating whether capital gains should be treated as long-term.
 Optional. Default: true.

(8) shortTermCapitalGains
 Short-term capital gains included in the calculation.
 Optional. No default value.

(9) qualifiedBusinessIncome
 Qualified Business Income used for the Section 199A deduction.
 Optional. No default value.

(10) aboveTheLineDeductions
 Above-the-line deductions included in the calculation.
 Optional. No default value.

(11) itemizedDeductions
 Total itemized deductions used instead of the standard deduction when higher.
 Optional. No default value.

(12) dependents
 Number of qualifying child dependents used for the Child Tax Credit.
 Optional. No default value.

(13) age65OrOlder
 Flag indicating whether the taxpayer is age 65 or older.
 Optional. No default value.

(14) blind
 Flag indicating whether the taxpayer is blind.
 Optional. No default value.

(15) isoExerciseSpread
 ISO exercise spread used for AMT calculation.
 Optional. No default value.

(16) stateTaxDeducted
 State or local taxes included in itemized deductions for AMT-related calculation.
 Optional. No default value.

(17) expectedAnnualIncome
 Expected total annual income used for quarterly tax estimation.
 Required. No default value.

(18) w2Withholding
 Expected total W-2 tax withholding for the year.
 Optional. No default value.

(19) otherCredits
 Expected other tax credits used in the estimate.
 Optional. No default value.

(20) stateCode
 Two-letter state code used for state tax calculation.
 Required. No default value.

(21) annualSalary
 Annual salary from the taxpayer's job used for W-4 withholding estimation.
 Required. No default value.

(22) payFrequency
 Pay frequency used to estimate per-paycheck withholding.
 Required. No default value.

(23) otherIncome
 Other annual income included in the withholding estimate.
 Optional. No default value.

(24) deductions
 Expected deductions used in the withholding estimate when they exceed the standard deduction.
 Optional. No default value.

(25) spouseWorks
 Flag indicating whether the taxpayer's spouse also works.
 Optional. No default value.

(26) multipleJobs
 Flag indicating whether the taxpayer holds multiple jobs simultaneously.
 Optional. No default value.

(27) category
 Category used to filter listed deductions or credits.
 Optional. Default: all.

(28) medicalExpenses
 Unreimbursed medical expenses used in the itemized deduction comparison.
 Optional. No default value.

(29) stateLocalTaxes
 State and local taxes paid used in the itemized deduction comparison.
 Optional. No default value.

(30) mortgageInterest
 Home mortgage interest paid used in the itemized deduction comparison.
 Optional. No default value.

(31) charitableDonations
 Charitable contributions used in the itemized deduction comparison.
 Optional. No default value.

(32) otherItemized
 Other itemized deductions included in the comparison.
 Optional. No default value.

(33) agi
 Adjusted Gross Income used for deduction threshold calculations.
 Required. No default value.

(34) filedElectronically
 Flag indicating whether the return was filed electronically.
 Optional. No default value.

(35) formNumber
 IRS form number used to retrieve form information.
 Required. No default value.

(36) refundableOnly
 Flag indicating whether only refundable tax credits should be listed.
 Optional. No default value.

(37) hasChildren
 Flag indicating whether the taxpayer has qualifying children under 17.
 Optional. No default value.

(38) numChildren
 Number of qualifying children used in credit eligibility screening.
 Optional. No default value.

(39) hasChildcare
 Flag indicating whether the taxpayer pays for childcare to work.
 Optional. No default value.

(40) isStudent
 Flag indicating whether the taxpayer is currently enrolled in post-secondary education.
 Optional. No default value.

(41) hasStudentLoans
 Flag indicating whether the taxpayer pays student loan interest.
 Optional. No default value.

(42) boughtEV
 Flag indicating whether the taxpayer purchased an electric vehicle this year.
 Optional. No default value.

(43) madeHomeImprovements
 Flag indicating whether the taxpayer made energy-efficient home improvements.
 Optional. No default value.

(44) installedSolar
 Flag indicating whether the taxpayer installed solar panels or other renewable energy.
 Optional. No default value.

(45) hasRetirementContributions
 Flag indicating whether the taxpayer made IRA or 401(k) contributions.
 Optional. No default value.

(46) hasMarketplaceInsurance
 Flag indicating whether the taxpayer bought health insurance through the ACA marketplace.
 Optional. No default value.

(47) hasEarnedIncome
 Flag indicating whether the taxpayer has earned income from work.
 Optional. No default value.

(48) paidForeignTax
 Flag indicating whether the taxpayer paid income tax to a foreign country.
 Optional. No default value.

(49) accountType
 Retirement account type used to filter returned account information.
 Optional. No default value.

(50) strategyId
 Retirement strategy identifier used to filter returned strategy information.
 Optional. No default value.

(51) earnedIncome
 Earned income used for EITC calculation.
 Required. No default value.

(52) qualifyingChildren
 Number of qualifying children used for EITC calculation.
 Required. No default value.

(53) investmentIncome
 Investment income used in EITC eligibility and amount calculation.
 Optional. No default value.

(54) taxableIncome
 State taxable income used for simplified state tax estimation.
 Required. No default value.

(55) states
 List of state codes used for comparing state tax across multiple jurisdictions.
 Required. No default value.

(56) estimatedIncome
 Expected total income for the year used in tax planning.
 Required. No default value.

(57) currentWithholding
 Total tax already withheld or paid year to date.
 Optional. No default value.

(58) hasRetirementPlan
 Flag indicating whether the taxpayer has access to a workplace retirement plan.
 Optional. No default value.

(59) currentRetirementContributions
 Year-to-date retirement contributions used in tax planning.
 Optional. No default value.

(60) hasHSA
 Flag indicating whether the taxpayer has an HSA-eligible health plan.
 Optional. No default value.

(61) currentHSAContributions
 Year-to-date HSA contributions used in tax planning.
 Optional. No default value.

(62) hasMortgage
 Flag indicating whether the taxpayer has a mortgage.
 Optional. No default value.

(63) estimatedItemizedDeductions
 Estimated total itemized deductions used in tax planning.
 Optional. No default value.

(64) hasCapitalGains
 Flag indicating whether the taxpayer expects capital gains.
 Optional. No default value.

(65) estimatedCapitalGains
 Estimated capital gains used in tax planning.
 Optional. No default value.

(66) hasCapitalLosses
 Flag indicating whether the taxpayer expects capital losses.
 Optional. No default value.

(67) isSelfEmployed
 Flag indicating whether the taxpayer is self-employed.
 Optional. No default value.

(68) charitableGiving
 Year-to-date charitable donations used in tax planning.
 Optional. No default value.

(69) grossRevenue
 Total business revenue used for self-employment tax estimation.
 Required. No default value.

(70) businessExpenses
 Total business expenses used for self-employment tax estimation.
 Required. No default value.

(71) otherW2Income
 W-2 income from other jobs included alongside self-employment activity.
 Optional. No default value.

(72) retirementContributions
 SEP IRA or Solo 401(k) contributions used in the self-employment estimate.
 Optional. No default value.

(73) healthInsurancePremiums
 Self-employed health insurance premiums used in the estimate.
 Optional. No default value.

(74) propertyTaxes
 Annual property taxes paid used in the mortgage tax benefit analysis.
 Required. No default value.

(75) stateIncomeTaxes
 State or local income taxes paid used in the mortgage tax benefit analysis.
 Optional. No default value.

(76) mortgageBalance
 Current mortgage balance used in the mortgage tax benefit analysis.
 Optional. No default value.

(77) interestRate
 Mortgage interest rate used in the mortgage tax benefit analysis.
 Optional. No default value.

(78) tuitionPaid
 Tuition and qualified education expenses paid.
 Required. No default value.

(79) isUndergrad
 Flag indicating whether the student is in the first four years of undergraduate study.
 Required. No default value.

(80) yearsAOTCClaimed
 Number of years the American Opportunity Tax Credit has already been claimed.
 Optional. No default value.

(81) studentLoanInterest
 Student loan interest paid during the year.
 Optional. No default value.

(82) has529Plan
 Flag indicating whether the taxpayer is contributing to or using a 529 plan.
 Optional. No default value.

(83) contribution529
 Amount contributed to a 529 plan during the year.
 Optional. No default value.

(84) spouse1Income
 Gross income for spouse 1 used in MFJ versus MFS comparison.
 Required. No default value.

(85) spouse2Income
 Gross income for spouse 2 used in MFJ versus MFS comparison.
 Required. No default value.

(86) studentLoanInterestFlag
 Flag indicating whether either spouse is paying student loan interest.
 Optional. No default value.

(87) hasEducationCredits
 Flag indicating whether either spouse is claiming education credits.
 Optional. No default value.

(88) hasEITC
 Flag indicating whether either spouse would qualify for the Earned Income Tax Credit.
 Optional. No default value.

(89) hasIRAContributions
 Flag indicating whether either spouse is contributing to an IRA.
 Optional. No default value.

(90) age
 Taxpayer age used for age-based tax calculations or deductions.
 Optional. No default value.

(91) spouseAge
 Spouse age used for age-based tax calculations when filing jointly.
 Optional. No default value.

(92) tipIncome
 Annual tip income used for OBBB deduction analysis.
 Optional. No default value.

(93) overtimePay
 Annual overtime premium pay used for OBBB deduction analysis.
 Optional. No default value.

(94) autoLoanInterest
 Auto loan interest used for OBBB deduction analysis.
 Optional. No default value.

(95) marginalRate
 Marginal tax rate used to estimate tax savings from deductions.
 Optional. No default value.

(96) fromYear
 Earlier tax year used in a cross-year comparison.
 Required. No default value.

(97) toYear
 Later tax year used in a cross-year comparison.
 Required. No default value.

(98) interestIncome
 Interest income used in the full tax report.
 Optional. No default value.

(99) dividendIncome
 Ordinary dividend income used in the full tax report.
 Optional. No default value.

(100) qualifiedDividends
 Qualified dividends used in the full tax report.
 Optional. No default value.

(101) longTermCapitalGains
 Long-term capital gains or losses used in the full tax report.
 Optional. No default value.

(102) stateLocalTaxesPaid
 State, local, or property taxes paid used in the full tax report.
 Optional. No default value.

(103) federalWithheld
 Federal tax already withheld year to date.
 Optional. No default value.

(104) stateWithheld
 State tax already withheld year to date.
 Optional. No default value.

(105) estimatedPaymentsMade
 Estimated tax payments already made.
 Optional. No default value.

(106) forms
 Array of 1099 forms used in 1099 income processing.
 Required. No default value.

(107) payer
 Payer name associated with a 1099 form entry.
 Optional. No default value.

(108) amount
 Total amount reported on a 1099 form entry.
 Required. No default value.

(109) qualifiedDividendsForm
 Qualified dividends amount for a 1099-DIV form entry.
 Optional. No default value.

(110) longTerm
 Flag indicating whether a 1099-B gain is long-term.
 Optional. No default value.

(111) filedExtension
 Flag indicating whether the taxpayer filed an extension.
 Optional. No default value.

(112) hasEmployer
 Flag indicating whether the taxpayer has W-2 employment.
 Optional. No default value.

(113) hasInvestments
 Flag indicating whether the taxpayer has investment accounts.
 Optional. No default value.

(114) hasRentalIncome
 Flag indicating whether the taxpayer has rental property income.
 Optional. No default value.

(115) grossPay
 Gross pay for the current pay period.
 Required. No default value.

(116) socialSecurityWithheld
 Social Security tax withheld for the current pay period.
 Optional. No default value.

(117) medicareWithheld
 Medicare tax withheld for the current pay period.
 Optional. No default value.

(118) retirement401k
 401(k) or 403(b) contribution amount used in the analysis.
 Optional. No default value.

(119) hsaContribution
 HSA contribution for the current pay period.
 Optional. No default value.

(120) currentIncome
 Current gross income used as the baseline for a tax scenario comparison.
 Required. No default value.

(121) currentState
 Current state code used as the baseline location in a tax scenario comparison.
 Optional. No default value.

(122) currentSelfEmployment
 Current self-employment income used as the baseline in a tax scenario comparison.
 Optional. No default value.

(123) currentCapitalGains
 Current capital gains used as the baseline in a tax scenario comparison.
 Optional. No default value.

(124) currentItemizedDeductions
 Current itemized deductions used as the baseline in a tax scenario comparison.
 Optional. No default value.

(125) currentDependents
 Current number of dependents used as the baseline in a tax scenario comparison.
 Optional. No default value.

(126) whatIfIncomeChange
 Hypothetical change in income used in a tax scenario comparison.
 Optional. No default value.

(127) whatIfNewState
 Hypothetical new state code used in a tax scenario comparison.
 Optional. No default value.

(128) whatIfFilingStatus
 Hypothetical filing status used in a tax scenario comparison.
 Optional. No default value.

(129) whatIfRothConversion
 Hypothetical Roth conversion amount used in a tax scenario comparison.
 Optional. No default value.

(130) whatIfAdditional401k
 Hypothetical additional 401(k) contribution used in a tax scenario comparison.
 Optional. No default value.

(131) whatIfNewDependents
 Hypothetical new number of dependents used in a tax scenario comparison.
 Optional. No default value.

(132) whatIfItemizedChange
 Hypothetical change in itemized deductions used in a tax scenario comparison.
 Optional. No default value.

(133) cashBusiness
 Flag indicating whether the taxpayer's business is cash-intensive.
 Optional. No default value.

(134) homeOfficeDeduction
 Flag indicating whether the taxpayer is claiming a home office deduction.
 Optional. No default value.

(135) charitableNonCash
 Non-cash charitable donations included in the audit risk profile.
 Optional. No default value.

(136) businessMeals
 Business meal deductions included in the audit risk profile.
 Optional. No default value.

(137) vehicleDeduction
 Vehicle or mileage deduction included in the audit risk profile.
 Optional. No default value.

(138) rentalLosses
 Rental property losses claimed in the audit risk profile.
 Optional. No default value.

(139) cryptoTransactions
 Flag indicating whether the taxpayer had cryptocurrency transactions.
 Optional. No default value.

(140) foreignAccounts
 Flag indicating whether the taxpayer has foreign bank accounts or assets.
 Optional. No default value.

(141) largeRefund
 Flag indicating whether the taxpayer expects a very large refund.
 Optional. No default value.

(142) eitcClaimed
 Flag indicating whether the taxpayer is claiming the Earned Income Tax Credit.
 Optional. No default value.

(143) roundNumbers
 Flag indicating whether most deductions are reported as round numbers.
 Optional. No default value.

(144) hasW2
 Flag indicating whether the taxpayer has W-2 employment.
 Optional. No default value.

(145) hasSelfEmployment
 Flag indicating whether the taxpayer has self-employment or freelance income.
 Optional. No default value.

(146) hasRentalProperty
 Flag indicating whether the taxpayer owns rental property.
 Optional. No default value.

(147) hasEducationExpenses
 Flag indicating whether the taxpayer has tuition or other education expenses.
 Optional. No default value.

(148) hasHealthInsurance
 Flag indicating whether the taxpayer has health insurance relevant to tax filing.
 Optional. No default value.

(149) hasCharitableDonations
 Flag indicating whether the taxpayer made charitable donations.
 Optional. No default value.

(150) hasForeignAccounts
 Flag indicating whether the taxpayer has foreign bank accounts or foreign income.
 Optional. No default value.

(151) soldHome
 Flag indicating whether the taxpayer sold a home during the year.
 Optional. No default value.

(152) gotMarried
 Flag indicating whether the taxpayer got married during the year.
 Optional. No default value.

(153) gotDivorced
 Flag indicating whether the taxpayer got divorced during the year.
 Optional. No default value.

(154) hadBaby
 Flag indicating whether the taxpayer had a baby during the year.
 Optional. No default value.

(155) ordinaryIncome
 Ordinary income used as the baseline before capital-gains optimization.
 Required. No default value.

(156) lots
 Array of investment lots used in the capital-gains optimization analysis.
 Required. No default value.

(157) name
 Investment name within a lot entry.
 Required. No default value.

(158) shares
 Number of shares within a lot entry.
 Required. No default value.

(159) costBasis
 Total cost basis within a lot entry.
 Required. No default value.

(160) currentValue
 Current market value within a lot entry.
 Required. No default value.

(161) holdingMonths
 Number of months the investment lot has been held.
 Required. No default value.

(162) targetGainOrLoss
 Target net gain or loss to realize in the optimization analysis.
 Optional. No default value.

(163) traditionalBalance
 Traditional IRA or 401(k) balance used in retirement-withdrawal planning.
 Required. No default value.

(164) rothBalance
 Roth IRA or Roth 401(k) balance used in retirement-withdrawal planning.
 Required. No default value.

(165) taxableBalance
 Taxable brokerage account balance used in retirement-withdrawal planning.
 Required. No default value.

(166) socialSecurityIncome
 Annual Social Security income used in retirement-withdrawal planning.
 Optional. No default value.

(167) pensionIncome
 Annual pension income used in retirement-withdrawal planning.
 Optional. No default value.

(168) annualSpending
 Annual pre-tax spending need used in retirement-withdrawal planning.
 Required. No default value.

(169) rothConversionInterest
 Flag indicating whether the taxpayer wants to consider a Roth conversion strategy.
 Optional. No default value.

(170) currentAge
 Current age used as the starting point in a multi-year tax projection.
 Required. No default value.

(171) years
 Array of year-by-year tax projections used in a multi-year plan.
 Required. No default value.

(172) year
 Tax year within a multi-year projection entry.
 Required. No default value.

(173) expectedIncome
 Expected gross income within a multi-year projection entry.
 Required. No default value.

(174) plannedRothConversion
 Planned Roth conversion amount within a multi-year projection entry.
 Optional. No default value.

(175) planned401k
 Planned 401(k) contribution within a multi-year projection entry.
 Optional. No default value.

(176) plannedIRA
 Planned IRA contribution within a multi-year projection entry.
 Optional. No default value.

(177) fromState
 Current state code used as the starting jurisdiction in a relocation tax analysis.
 Required. No default value.

(178) toState
 Target state code used as the destination jurisdiction in a relocation tax analysis.
 Required. No default value.

(179) yearsToProject
 Number of years used to project relocation-related tax savings.
 Optional. No default value.

(180) incomeGrowthRate
 Annual income growth rate used in a relocation tax projection.
 Optional. No default value.

(181) retirementIRA
 IRA contribution amount used in the tax health check.
 Optional. No default value.

(182) hsaContributions
 HSA contribution amount used in the tax health check.
 Optional. No default value.

(183) topic
 Tax topic used to look up IRS rules, definitions, or common questions.
 Required. No default value.
